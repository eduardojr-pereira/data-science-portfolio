"""Adapter to the canonical EP Brand component renderers."""
from pathlib import Path
import importlib
import os
import sys

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
            "tools/render_footer.py",
            "tools/render_header.py",
            "tools/publish_assets.py",
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


def _canonical_module(name):
    """Import a module exclusively from the resolved EP Brand checkout."""
    tools_dir = ROOT / "tools"
    sys.path.insert(0, str(tools_dir))
    try:
        module = importlib.import_module(name)
        expected = (tools_dir / f"{name}.py").resolve()
        actual = Path(module.__file__).resolve()
        if actual != expected:
            raise ImportError(
                f"Unexpected EP module: {actual}; expected {expected}"
            )
        return module
    finally:
        sys.path.remove(str(tools_dir))


_footer = _canonical_module("render_footer")
_header = _canonical_module("render_header")
_assets = _canonical_module("publish_assets")


def logo_data_uri():
    return _header.logo_data_uri()


def render_footer():
    return (
        _footer.render_web_footer(embed=True),
        _footer.render_web_css(),
    )


def render_header(projects, **kwargs):
    return _header.render_header(projects, **kwargs)


def copy_shared_assets(output):
    return _assets.copy_shared_assets(output)

def render_references(data):
    return _canonical_module("render_references").render_references(data)

def render_outputs(data):
    return _canonical_module("render_outputs").render_outputs(data)


def render_project_links(repository, *, back_to_portfolio=False):
    return _canonical_module("render_project_links").render_project_links(repository, back_to_portfolio=back_to_portfolio)
