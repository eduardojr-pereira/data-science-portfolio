#!/usr/bin/env python3
"""Integrate the validated Hangman Learning Lab into the EP showcase.

Run at repository root:
    python tools/integrar_jogo_da_forca.py           # dry run
    python tools/integrar_jogo_da_forca.py --apply   # modify generator + render report

Does not commit/push or create backups inside the Git repository.
"""
from __future__ import annotations
import argparse
import datetime
import importlib.util
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / 'tools/build_pages_site.py'
PROJECT = ROOT / 'learning_labs/python/jogo_da_forca'
REPORT = PROJECT / 'reports/index.html'
ENTRY = '''    "learning_labs/python/jogo_da_forca": {
        "name": "Hangman Game — Python Fundamentals",
        "description": "Play an interactive bilingual Hangman game. Explore a tested Python implementation with single-player and two-player modes, input validation, and unit tests.",
        "topics": ("Python Programming",),
        "technologies": ("Python", "JavaScript", "HTML", "CSS"),
        "featured": False,
    },
'''

def build_html() -> str:
    sys.path.insert(0,str(ROOT / 'tools'))
    from ep_brand import render_footer, logo_data_uri
    footer_html,footer_css=render_footer()
    source=(PROJECT/'web/game.template.html').read_text(encoding='utf-8')
    replacements={
      '__EP_FOOTER_CSS__':footer_css,
      '__EP_FOOTER_HTML__':footer_html,
      '__EP_LOGO__':logo_data_uri(),
      '__GAME_CSS__':(PROJECT/'web/game.css').read_text(encoding='utf-8'),
      '__EP_MOTION_CSS__':(PROJECT/'web/ep_footer_motion.css').read_text(encoding='utf-8'),
      '__GAME_JS__':(PROJECT/'web/game.js').read_text(encoding='utf-8'),
      '__KEYS__': '\n'.join(f'<button type="button" class="key" data-letter="{ch}" aria-label="{ch}">{ch}</button>' for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    }
    for key,val in replacements.items():
        if source.count(key)!=1:raise RuntimeError(f'Expected one {key} placeholder')
        source=source.replace(key,val)
    if re.search(r'__[A-Z_]+__',source):raise RuntimeError('Unresolved template placeholder')
    if '<footer class="ep-footer"' not in source:raise RuntimeError('Shared EP footer not found')
    return source

def patch_generator(raw: str) -> tuple[str,bool]:
    key='"learning_labs/python/jogo_da_forca"'
    if key in raw:return raw,False
    anchor='PROJECT_METADATA = {\n'
    if raw.count(anchor)!=1:raise RuntimeError('Unexpected PROJECT_METADATA layout. No changes made.')
    return raw.replace(anchor,anchor+ENTRY,1),True

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--apply',action='store_true')
    args=p.parse_args()
    for path in [GENERATOR,ROOT/'tools/ep_brand.py',PROJECT/'forca.py',PROJECT/'tests/test_forca.py',PROJECT/'README.md',PROJECT/'README.pt-BR.md',PROJECT/'web/game.template.html',PROJECT/'web/game.js',PROJECT/'web/game.css',PROJECT/'web/ep_footer_motion.css']:
        if not path.is_file():raise SystemExit(f'Missing: {path}')
    old=GENERATOR.read_text(encoding='utf-8')
    new,added=patch_generator(old)
    html=build_html()
    compile(new,str(GENERATOR),'exec')
    report_changed=not REPORT.is_file() or REPORT.read_text(encoding='utf-8')!=html
    print('SIMULAÇÃO OK' if not args.apply else 'VALIDAÇÃO OK')
    print('New metadata:', 'yes' if added else 'already present')
    print('Report requires update:', 'yes' if report_changed else 'no')
    if not args.apply:
        print('No files modified. Run with --apply to write.')
        return
    # No extra backup files inside repo. Preserve only tracked changes for Git review.
    if added:GENERATOR.write_text(new,encoding='utf-8')
    if report_changed:
        REPORT.parent.mkdir(parents=True,exist_ok=True)
        REPORT.write_text(html,encoding='utf-8')
    print('APLICADO: metadata and standalone HTML ready for local Pages build.')

if __name__=='__main__':main()
