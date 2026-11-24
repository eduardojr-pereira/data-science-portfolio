"""EP web component renderer, synchronized from sibling ep-brand-assets snapshot."""
from pathlib import Path
import base64
import datetime
import json
import mimetypes
import os
import re

def _canonical_root() -> Path:
    """Find the actual EP Brand checkout; never silently use vendored copies."""
    portfolio = Path(__file__).resolve().parents[1]
    configured = os.environ.get("EP_BRAND_ASSETS_ROOT")
    candidates = (
        [Path(configured).expanduser()] if configured else [
            portfolio / ".ep-brand-assets-build",  # GitHub Actions checkout
            portfolio.parent / "ep-brand-assets",  # Local sibling repository
        ]
    )
    for candidate in candidates:
        root = candidate.resolve()
        if all((root / relative).is_file() for relative in (
            "config/brand.json",
            "components/web/footer.html",
            "components/web/footer.css",
        )):
            return root
    checked = ", ".join(str(p) for p in candidates)
    raise FileNotFoundError(
        "Canonical ep-brand-assets checkout not found or incomplete. "
        f"Checked: {checked}. Place it beside 04_Projetos, or use the "
        "GitHub Actions .ep-brand-assets-build checkout. "
        "EP_BRAND_ASSETS_ROOT can explicitly override the location."
    )


ROOT = _canonical_root()

def _values():
    brand=json.loads((ROOT/'config/brand.json').read_text(encoding='utf-8'))
    values=dict(brand)
    for key, rel in {'logo_src':'logos/logo_initials.png', 'gmail_src':'icons/gmail_icon.svg', 'linkedin_src':'icons/linkedin_icon.svg'}.items():
        payload=(ROOT/'assets'/rel).read_bytes()
        mime=mimetypes.guess_type(rel)[0] or 'application/octet-stream'
        values[key]=f'data:{mime};base64,'+base64.b64encode(payload).decode('ascii')
    values['year']=str(datetime.date.today().year)
    return values

def _sub(template, values):
    def replace(m):
        k=m.group(1)
        if k not in values:raise ValueError('Unknown EP placeholder: '+k)
        return str(values[k])
    result=re.sub(r'\{\{([a-z_]+)\}\}',replace,template)
    if '{{' in result or '}}' in result:raise ValueError('Unresolved EP placeholders')
    return result

def logo_data_uri():
    return _values()['logo_src']

def render_footer():
    values=_values()
    html=_sub((ROOT/'components/web/footer.html').read_text(encoding='utf-8'),values)
    css_paths = [
        ROOT / 'styles' / 'colors.css',
        ROOT / 'styles' / 'typography.css',
        ROOT / 'styles' / 'layout.css',
        ROOT / 'components/web/footer.css',
    ]
    css = '\n'.join(
        path.read_text(encoding='utf-8').rstrip()
        for path in css_paths
    ) + '\n'
    return html,css



def render_header(projects):
    """Render the shared EP header for the generated portfolio showcase."""
    from html import escape
    values = _values()
    menu = []
    for project in projects:
        href = escape(str(project.get("report", "#projects")), quote=True)
        label = escape(str(project.get("name", "Project")))
        menu.append(f'<a href="{href}">{label}</a>')
    values["projects_menu"] = "\n          ".join(menu)
    template = (ROOT / "components" / "web" / "header.html").read_text(encoding="utf-8")
    markup = _sub(template, values)
    css = "\n".join([
        (ROOT / "components" / "web" / "header.css").read_text(encoding="utf-8"),
        (ROOT / "styles" / "portfolio-theme.css").read_text(encoding="utf-8"),
    ])
    return markup, css


def copy_shared_assets(output):
    """Copy the validated theme/i18n runtime and animation assets into Pages output."""
    import shutil
    destination = output / "assets"
    files = (
        "styles/theme-tokens.css", "styles/typography-v2.css", "styles/portfolio-theme.css",
        "scripts/theme-init.js", "scripts/theme.js", "scripts/i18n.js", "scripts/header.js",
    )
    for relative in files:
        source = ROOT / relative
        if not source.is_file():
            raise FileNotFoundError(f"Missing shared EP asset: {source}")
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    animations = ROOT / "assets" / "animations"
    if animations.is_dir():
        shutil.copytree(animations, destination / "animations", dirs_exist_ok=True)
