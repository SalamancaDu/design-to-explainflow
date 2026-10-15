"""Validate the document/Skill bundle using only the Python standard library.

Checks references and structures, not model behavior or production tool results.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import argparse
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {"layout-design", "image-style", "title-text-design", "motion-style", "design-review"}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".html", ".svg", ".py"}
EXCLUDED = {".git", ".local", "__pycache__", ".venv", "node_modules", "runs", "outputs"}
errors = []
counts = {"text_files": 0, "local_links": 0, "skill_references": 0, "json_files": 0, "svg_files": 0}

def require(condition, message):
    if not condition:
        errors.append(message)

def label(path):
    return path.relative_to(ROOT).as_posix()

def read(path):
    data = path.read_bytes()
    require(not data.startswith(b"\xef\xbb\xbf"), "UTF-8 BOM: " + label(path))
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        errors.append("Invalid UTF-8: " + label(path) + ": " + str(error))
        return ""
    require("\x00" not in text and "\ufffd" not in text, "Invalid text character: " + label(path))
    return text

def without_fences(text, path):
    visible = []
    active = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if active:
            if match and match.group(1)[0] == active[0] and len(match.group(1)) >= len(active) and not match.group(2).strip():
                active = None
        elif match:
            active = match.group(1)
        else:
            visible.append(line)
    require(active is None, "Unclosed code fence: " + label(path))
    return "\n".join(visible)

def slug(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text).replace("`", "").replace("*", "").strip().lower()
    text = "".join(c for c in text if c in " _-" or not unicodedata.category(c).startswith(("P", "S")))
    return text.replace(" ", "-")

def anchors(path):
    text = path.read_text(encoding="utf-8")
    found = set(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    seen = {}
    if path.suffix == ".md":
        for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, flags=re.M):
            key = slug(heading)
            number = seen.get(key, 0)
            found.add(key if number == 0 else key + "-" + str(number))
            seen[key] = number + 1
    return found

def link(source, reference):
    reference = reference.strip().strip("<>")
    url = urlsplit(reference)
    if url.scheme or url.netloc:
        return
    decoded = unquote(url.path)
    if not decoded and not url.fragment:
        return
    target = (source.parent / decoded).resolve() if decoded else source.resolve()
    require(target.is_relative_to(ROOT), "Link escapes repository: " + label(source) + " -> " + reference)
    if not target.is_relative_to(ROOT):
        return
    require(target.exists(), "Missing target: " + label(source) + " -> " + reference)
    if target.is_file() and url.fragment and target.suffix in {".md", ".html", ".svg"}:
        require(unquote(url.fragment) in anchors(target), "Missing anchor: " + label(source) + " -> " + reference)
    counts["local_links"] += 1

class HtmlReferences(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                link(self.source, value)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", action="store_true", help="Also require a final LICENSE and removal of publication-draft notices.")
    args = parser.parse_args()
    paths = [path for path in ROOT.rglob("*") if path.is_file() and not any(part in EXCLUDED for part in path.relative_to(ROOT).parts)]
    skill_dirs = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    require(skill_dirs == SKILLS, "Expected exactly the five documented Skill entrypoints.")
    for path in paths:
        if path.suffix not in TEXT_SUFFIXES:
            continue
        text = read(path)
        counts["text_files"] += 1
        if path.suffix in {".md", ".yaml", ".yml", ".json", ".html", ".svg"}:
            private = re.search(r"(?:[A-Za-z]:[\\/](?:Users|C_Documents)[\\/]|codex-thread-[0-9a-f-]{16,}|\[\[[^\]\n]+\]\])", text)
            require(private is None, "Private machine path, session ID or vault-only link: " + label(path))
            secret = re.search(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|sk-[A-Za-z0-9_-]{32,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)", text)
            require(secret is None, "Potential credential material: " + label(path))
        if path.suffix == ".md":
            visible = without_fences(text, path)
            for ref in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", visible):
                link(path, ref)
            HtmlReferences(path).feed(visible)
            relative = path.relative_to(ROOT).parts
            if len(relative) >= 3 and relative[0] == "skills":
                base = ROOT / "skills" / relative[1]
                for ref in set(re.findall(r"(?<![\w./-])(references/[A-Za-z0-9_-]+\.md)", visible)):
                    require((base / ref).is_file(), "Missing Skill reference: " + label(path) + " -> " + ref)
                    counts["skill_references"] += 1
            if path.name == "SKILL.md":
                front = re.match(r"\A---\r?\n(.*?)\r?\n---", text, re.S)
                require(front is not None, "Missing Skill frontmatter: " + label(path))
                if front:
                    match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", front.group(1), re.M)
                    require(match is not None and match.group(1) == path.parent.name, "Skill name mismatch: " + label(path))
                    require(re.search(r"^description:\s*\S", front.group(1), re.M) is not None, "Missing Skill description: " + label(path))
                require((path.parent / "agents/openai.yaml").is_file(), "Missing UI metadata: " + label(path))
        elif path.suffix == ".html":
            HtmlReferences(path).feed(text)
        elif path.suffix == ".json":
            try:
                json.loads(text)
                counts["json_files"] += 1
            except json.JSONDecodeError as error:
                errors.append("Invalid JSON: " + label(path) + ": " + str(error))
        elif path.suffix == ".svg":
            try:
                svg = ET.fromstring(text)
                require(svg.tag == "{http://www.w3.org/2000/svg}svg", "Invalid SVG root: " + label(path))
                require("viewBox" in svg.attrib, "Missing SVG viewBox: " + label(path))
                counts["svg_files"] += 1
            except ET.ParseError as error:
                errors.append("Invalid SVG: " + label(path) + ": " + str(error))
    final_license = ROOT / "LICENSE"
    if args.release:
        require(final_license.is_file() and final_license.stat().st_size > 100, "Publication requires a finalized LICENSE.")
        for name in ("README.md", "README.en.md", "NOTICE.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            require("待作者确认" not in text and "尚未声明" not in text and "no open-source license is declared yet" not in text,
                    "Publication draft notice remains: " + name)
    result = {"status": "passed" if not errors else "failed", "checks": counts, "skills": len(skill_dirs),
              "license_file_present": final_license.is_file(), "release_check": args.release,
              "scope": "Local references and file structures; not a fresh browser run, model evaluation or generation/export test.",
              "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
