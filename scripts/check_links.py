"""Check repository Markdown links, section anchors and image embeds.

The repository keeps no image files: paper notes and topics use text, tables or Mermaid instead.

Usage: python scripts/check_links.py
"""
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(!?)\[[^\]]*\]\(([^)\s]+)\)")
HTML_IMG = re.compile(r"<img\b", re.IGNORECASE)


def section_ids(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    ids, counts = set(), {}
    for title in re.findall(r"^#{1,6} (.+)$", text, re.M):
        title = re.sub(r"\s+#+\s*$", "", title)
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", title)
        title = re.sub(r"<[^>]+>", "", title).strip()
        slug = "".join(c for c in title.lower() if c in "_- " or unicodedata.category(c)[0] not in "PS").replace(" ", "-")
        n = counts.get(slug, 0)
        anchor = slug + (f"-{n}" if n else "")
        while anchor in ids:
            n += 1
            anchor = f"{slug}-{n}"
        counts[slug] = n + 1
        ids.add(anchor)
    return ids


def main():
    errors = []
    names = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT,
    ).decode().split("\0")
    files = {ROOT / name for name in names if name and (ROOT / name).is_file()}
    published = {path.resolve() for path in files}
    docs = {path: path.read_text() for path in files if path.suffix == ".md"}
    anchors = {}
    for md, text in docs.items():
        content = re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$", "", text, flags=re.M | re.S)
        anchors[md.resolve()] = section_ids(content) | set(re.findall(r'<a\s+id=["\']([^"\']+)["\']', content))
    for md, text in sorted(docs.items()):
        rel = md.relative_to(ROOT)
        if HTML_IMG.search(text):
            errors.append(f"{rel}: image embed (<img>) is not allowed")
        for bang, target in LINK.findall(text):
            if bang:
                errors.append(f"{rel}: image embed is not allowed: {target}")
                continue
            if md.name.startswith("_template") or re.match(r"^[a-z]+:", target):
                continue
            filename, _, fragment = unquote(target).partition("#")
            path = (md.parent / filename).resolve() if filename else md.resolve()
            if not path.exists():
                errors.append(f"{rel}: broken link {target}")
            elif path.is_file() and path not in published:
                errors.append(f"{rel}: link to a file outside repository content {target}")
            elif fragment and path in anchors and fragment not in anchors[path]:
                errors.append(f"{rel}: broken section link {target}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("ok: repository links and section anchors resolve, no image embeds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
