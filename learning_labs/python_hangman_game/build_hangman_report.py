#!/usr/bin/env python3
"""Build the standalone Hangman HTML report.

Default: validation only.
Use --apply to update reports/index.html.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

PROJECT = Path(__file__).resolve().parent
ROOT = PROJECT.parents[1]
REPORT = PROJECT / "reports/index.html"



def build_html() -> str:
    sys.path.insert(0,str(ROOT / 'tools'))
    from ep_brand import render_footer, logo_data_uri, render_project_links
    footer_html,_=render_footer()
    source=(PROJECT/'web/report.template.html').read_text(encoding='utf-8')
    replacements={
      '__EP_FOOTER_HTML__':footer_html,
      '__EP_PROJECT_LINKS__':render_project_links('https://github.com/eduardojr-pereira/data-science-portfolio/tree/main/learning_labs/python_hangman_game', back_to_portfolio=False),

      '__EP_LOGO__':logo_data_uri(),
      '__GAME_CSS__':(PROJECT/'web/report.css').read_text(encoding='utf-8'),
      '__GAME_JS__':(PROJECT/'web/report.js').read_text(encoding='utf-8'),
      '__KEYS__': '\n'.join(f'<button type="button" class="key" data-letter="{ch}" aria-label="{ch}">{ch}</button>' for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    }
    for key,val in replacements.items():
        if source.count(key)!=1:raise RuntimeError(f'Expected one {key} placeholder')
        source=source.replace(key,val)
    if re.search(r'__[A-Z_]+__',source):raise RuntimeError('Unresolved template placeholder')
    if '<footer class="ep-footer"' not in source:raise RuntimeError('Shared EP footer not found')
    return source.replace("../../../../index.html", "../../../index.html")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    required = [
        ROOT / "tools/ep_brand.py",
        PROJECT / "hangman.py",
        PROJECT / "tests/test_hangman.py",
        PROJECT / "web/report.template.html",
        PROJECT / "web/report.css",
        PROJECT / "web/report.js",
    ]

    for path in required:
        if not path.is_file():
            raise SystemExit(f"Missing: {path}")

    html = build_html()
    changed = (
        not REPORT.is_file()
        or REPORT.read_text(encoding="utf-8") != html
    )

    print("VALIDATION OK")
    print("Report requires update:", "yes" if changed else "no")

    if not args.apply:
        print("Dry run: no files modified.")
        return

    if changed:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(html, encoding="utf-8")

    print("Report ready:", REPORT)


if __name__ == "__main__":
    main()
