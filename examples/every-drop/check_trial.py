"""Check this concrete trial's artifacts and captured browser observations; no external calls."""
from pathlib import Path
import copy
import json
import math
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).parent
html = (ROOT / 'preview.html').read_text(encoding='utf-8')
case = json.loads(re.search(r'<script type="application/json" id="case-data">(.*?)</script>', html, re.S).group(1))
svg_text = re.search(r'<template id="base-layout">(.*?)</template>', html, re.S).group(1)
svg = ET.fromstring(svg_text)
manifest = json.loads((ROOT / 'scenes/d01/scene.manifest.json').read_text(encoding='utf-8'))
observations = json.loads((ROOT / 'browser-checks.json').read_text(encoding='utf-8'))
checks = []

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def validate_content(root):
    ids = {e.attrib['id']: e for e in root.iter() if 'id' in e.attrib}
    require(len(ids) == sum('id' in e.attrib for e in root.iter()), 'Duplicate SVG ID')
    require(root.attrib['viewBox'] == '0 0 1920 1080', 'Wrong canvas')
    require(''.join(ids['headline'].itertext()) == case['title'], 'Title changed')
    require(''.join(ids['subtitle'].itertext()) == case['subtitle'], 'Subtitle changed')
    require(''.join(ids['edition'].itertext()) == case['edition'], 'Edition snapshot changed')
    require(''.join(ids['disclaimer'].itertext()) == case['note'], 'Missing synthetic-data disclaimer')
    require(sum(d['value'] for d in case['data']) == case['total'], 'Wrong total')
    mapping = case['mapping']
    require(mapping['plotWidth'] / mapping['maxValue'] == mapping['pxPerUnit'], 'Scale mismatch')
    for item in case['data']:
        bar = ids['bar-' + item['id']]
        require(float(bar.attrib['x']) == mapping['x'], 'Nonshared chart baseline')
        require(float(bar.attrib['width']) == item['value'] * mapping['pxPerUnit'], 'Wrong quantitative geometry')
        require(''.join(ids['label-' + item['id']].itertext()) == item['label'], 'Wrong category')
        require(''.join(ids['value-' + item['id']].itertext()).strip() == str(item['value']) + ' 份', 'Wrong value label')
    return ids

ids = validate_content(svg)
checks.append('Exact copy, synthetic-data label, total and quantitative geometry')
require((ROOT / 'B/static-export.svg').read_text(encoding='utf-8').strip() == svg_text.strip(), 'Static snapshot drifted from layout source')
checks.append('Static SVG export matches authoritative HTML layout')

def validate_handoff(obj):
    base = ROOT / 'scenes/d01'
    for key in ['layoutSource', 'staticSnapshot']:
        path = (base / obj[key]).resolve()
        require(path.is_relative_to(ROOT.resolve()) and path.is_file(), 'Missing or out-of-scope handoff file')
    require(obj['positionOrigin'] == 'top-left' and obj['pathBase'] == 'manifest-directory', 'Ambiguous positioning contract')
    for element in obj['elements']:
        require(element['id'] in ids and element['sourceSelector'] == '#' + element['id'], 'Unknown element target')
        node = ids[element['id']]
        for key in ['x', 'y', 'width', 'height']:
            require(math.isclose(float(node.attrib[key]), element[key]), 'Coordinate snapshot mismatch')
        require(element['anchor'] == 'top-left', 'Unexpected transform origin')
    require(obj['dataBasis']['values'] == case['data'], 'Handoff data differs from source')
    require(obj['audio']['mode'] == 'silent' and obj['audio']['durationSeconds'] == 8, 'Wrong sound/duration handoff')

validate_handoff(manifest)
checks.append('Manifest paths, identifiers, coordinates, data basis and silent timing')

require(observations['B']['edition'] == '2026.11 · 演练版', 'Editable date did not update')
require(observations['B']['widths'] == [480, 360, 240, 120], 'Date edit changed chart geometry')
require(observations['sharedEdition'] == observations['B']['edition'], 'Edit did not reach D')
checks.append('Captured B date edit preserves geometry and reaches D')
require(all(x['coversCanvas'] and x['hasOnlyOneFrame'] for x in observations['C']), 'Whole-frame preview lost coverage or added independent objects')
for box in observations['B']['textBounds']:
    # Conservative C end-frame bounds using the agreed centered scale and canvas-pixel translation.
    left = (box['x'] - 960) * 1.035 + 960 - 12
    top = (box['y'] - 540) * 1.035 + 540
    require(left >= 0 and top >= 0 and left + box['width'] * 1.035 <= 1920 and top + box['height'] * 1.035 <= 1080, 'Text crop at C end: ' + box['id'])
checks.append('Captured C image coverage and measured text bounds remain inside crop')
expected = [None, 'focus-bath', 'focus-kitchen', 'focus-laundry', 'focus-other', None, None, 'focus-bath']
require(len(observations['D']) == len(expected), 'Missing key-time observations')
for shot, target in zip(observations['D'], expected):
    require(shot['title'] == case['title'] and shot['widths'] == [480, 360, 240, 120] and shot['labels'] == ['40 份','30 份','20 份','10 份'], 'D changed exact content or geometry')
    visible = [item[0] for item in shot['emphasis'] if item[1] > 0.99]
    require(visible == ([] if target is None else [target]), 'Wrong independent emphasis at time ' + shot['time'])
require(observations['playback']['time'] == '8' and observations['playback']['button'] == '播放', 'Playback did not finish')
require(not observations['console'], 'Browser warning or error was recorded')
require(observations['A']['visible'] and observations['A']['images'] == 0, 'A falsely presents a generated image')
checks.append('Captured D keyframes, reverse seek, real playback endpoint and generation boundary')

negative = []
wrong = copy.deepcopy(svg)
next(e for e in wrong.iter() if e.attrib.get('id') == 'bar-bath').set('width', '470')
bad_id = copy.deepcopy(manifest)
bad_id['elements'][0]['id'] = 'not-created'
bad_path = copy.deepcopy(manifest)
bad_path['layoutSource'] = '../../title/not-generated.png'
for name, validator, data in [
    ('Wrong bar length rejected', validate_content, wrong),
    ('Missing element target rejected', validate_handoff, bad_id),
    ('Planned but nonexistent asset rejected', validate_handoff, bad_path),
]:
    try:
        validator(data)
    except AssertionError:
        negative.append(name)
    else:
        raise AssertionError('Negative fixture was incorrectly accepted: ' + name)

for href in re.findall(r'href="([^"]+)"', html):
    require((ROOT / href).is_file(), 'Broken preview link: ' + href)
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix in ['.md','.html','.svg','.json','.py']:
        data = path.read_bytes()
        require(not data.startswith(b'\xef\xbb\xbf'), 'UTF-8 BOM: ' + str(path))
        data.decode('utf-8', errors='strict')

result = {'status':'passed','artifact_checks':checks,'negative_cases':negative,
          'evidence_scope':'Static artifacts and previously captured browser observations; not a fresh browser run, generated-image test or video-render test.'}
(ROOT / 'check-results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
