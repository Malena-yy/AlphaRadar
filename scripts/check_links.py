"""Check that relative Markdown links resolve and that no Markdown embeds an image.

The repository keeps no image files: paper notes and topics use text, tables or Mermaid instead.

Usage: python scripts/check_links.py
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(!?)\[[^\]]*\]\(([^)\s]+)\)")
HTML_IMG = re.compile(r"<img\b", re.IGNORECASE)


def main():
    errors = []
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        rel = md.relative_to(ROOT)
        text = md.read_text()
        if HTML_IMG.search(text):
            errors.append(f"{rel}: image embed (<img>) is not allowed")
        for bang, target in LINK.findall(text):
            if bang:
                errors.append(f"{rel}: image embed is not allowed: {target}")
                continue
            if md.name.startswith("_template") or re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = (md.parent / unquote(target.split("#", 1)[0])).resolve()
            if not path.exists():
                errors.append(f"{rel}: broken link {target}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("ok: all relative links resolve, no image embeds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
