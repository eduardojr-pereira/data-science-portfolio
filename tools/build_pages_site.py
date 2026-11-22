#!/usr/bin/env python3
"""Build a static GitHub Pages site from approved portfolio HTML reports.

Usage:
    python tools/build_pages_site.py --output "$HOME/Downloads/portfolio_pages_preview"

The published site contains only project reports and their outputs, not raw
source datasets, Jupyter notebooks, or arbitrary project-root files.
"""

from __future__ import annotations

import argparse
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import shutil
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPORT_COLLECTIONS = ("selected_projects", "learning_labs")


class PageLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.title_parts: list[str] = []
        self.inside_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "title":
            self.inside_title = True
        key = "href" if tag in {"a", "link"} else "src" if tag in {"script", "img"} else None
        if key and attributes.get(key):
            self.urls.append(str(attributes[key]))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.inside_title = False

    def handle_data(self, data: str) -> None:
        if self.inside_title:
            self.title_parts.append(data)


def discover_reports() -> list[Path]:
    return sorted(
        report
        for collection in REPORT_COLLECTIONS
        if (ROOT / collection).is_dir()
        for report in (ROOT / collection).rglob("reports/index.html")
        if not any(part.startswith(".") for part in report.relative_to(ROOT).parts)
    )


def ensure_valid_local_links(source_html: Path, parser: PageLinks) -> None:
    for url in parser.urls:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
            continue
        destination = (source_html.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(ROOT) or not destination.is_file():
            raise RuntimeError(f"Missing or unsafe local link in {source_html}: {url}")
        # This builder deliberately publishes only reports and outputs.
        project = source_html.parent.parent
        if not (destination.is_relative_to(project / "reports") or destination.is_relative_to(project / "outputs")):
            raise RuntimeError(f"Link points outside published report assets: {url}")


def make_homepage(reports: list[tuple[str, str, str]]) -> str:
    cards = []
    for label, category, url in reports:
        cards.append(
            '<a class="card" href="' + escape(url, quote=True) + '">'
            '<span class="eyebrow">' + escape(category) + '</span>'
            '<h2>' + escape(label) + '</h2>'
            '<span class="open">Explore interactive report &rarr;</span>'
            '</a>'
        )
    rendered_cards = "\n".join(cards)
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>Data Science Portfolio · EP</title>
<style>
:root { color-scheme: dark; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #0C1525; color: #E7EEF9; }
* { box-sizing: border-box; }
body { margin: 0; min-height: 100vh; background: radial-gradient(ellipse at top right, #162A40 0%, #0C1525 60%); }
header, main, footer { max-width: 1050px; margin: auto; padding: 28px 24px; }
header { border-bottom: 1px solid #263B51; font-weight: 750; letter-spacing: .09em; font-size: 13px; }
header span { color: #67D8E9; }
h1 { margin: 42px 0 10px; font-size: clamp(34px, 5vw, 60px); letter-spacing: -.04em; }
p { color: #ABBDD0; font-size: 16px; line-height: 1.75; max-width: 680px; }
.projects { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 36px; }
.card { display: block; text-decoration: none; color: #FFF; background: #14243A; border: 1px solid #28445F; border-radius: 16px; padding: 27px; transition: border-color .24s, transform .24s, box-shadow .24s; }
.card:hover, .card:focus-visible { border-color: #FF9F43; box-shadow: 0 10px 32px #0005; transform: translateY(-3px); outline: none; }
.card h2 { margin: 15px 0 24px; font-size: 23px; }
.eyebrow { color: #67D8E9; font-size: 12px; letter-spacing: .06em; text-transform: uppercase; }
.open { border-bottom: 2px solid #FF9F43; padding-bottom: 5px; font-size: 13px; font-weight: 650; }
footer { color: #9FB5CA; border-top: 1px solid #263B51; margin-top: 80px; font-size: 13px; }
footer a { color: #E7EEF9; margin-right: 14px; text-decoration-color: #FF9F43; }
</style>
</head>
<body>
<header>EP <span>/</span> DATA SCIENCE</header>
<main>
<h1>Data Science Portfolio</h1>
<p>Explore applied analyses and learning experiments through interactive reports. Source code, methods and scientific limitations are documented in the linked GitHub repository.</p>
<section class="projects" aria-label="Project reports">
""" + rendered_cards + """
</section>
</main>
<footer>
<a href="https://github.com/eduardojr-pereira/data-science-portfolio">GitHub Portfolio</a>
<a href="https://github.com/eduardojr-pereira/data-science-knowledge-base">Knowledge Base</a>
<a href="https://eduardo-pereira.webflow.io/">Personal Website</a>
</footer>
</body>
</html>
"""


def main() -> None:
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument("--output", type=Path, required=True, help="Destination for static Pages artifacts")
    args = argparser.parse_args()
    output = args.output.expanduser().resolve()
    if output == ROOT or ROOT.is_relative_to(output) or output.is_relative_to(ROOT):
        raise SystemExit("Output directory must be outside the Git repository")
    reports = discover_reports()
    if not reports:
        raise SystemExit("No reports/index.html found under selected_projects/ or learning_labs/")

    parsed: list[tuple[Path, PageLinks]] = []
    for report in reports:
        parsed_html = PageLinks()
        parsed_html.feed(report.read_text(encoding="utf-8"))
        ensure_valid_local_links(report, parsed_html)
        parsed.append((report, parsed_html))

    # Never delete an unrelated existing directory.
    if output.exists():
        if not (output / ".portfolio-pages-build").is_file():
            raise SystemExit(f"Refusing to overwrite an unmarked directory: {output}")
        shutil.rmtree(output)
    output.mkdir(parents=True)
    (output / ".portfolio-pages-build").touch()
    published = []
    for report, parser in parsed:
        project = report.parent.parent
        relative = project.relative_to(ROOT)
        destination = output / relative
        for asset_root in (project / "reports", project / "outputs"):
            if asset_root.is_dir() and any(p.is_symlink() for p in asset_root.rglob("*")):
                raise RuntimeError(f"Symlinks are not allowed in published assets: {asset_root}")
        shutil.copytree(project / "reports", destination / "reports")
        if (project / "outputs").is_dir():
            shutil.copytree(project / "outputs", destination / "outputs")
        title = " ".join(parser.title_parts).split(" · ", 1)[0].strip() or project.name.replace("_", " ").title()
        category = "Selected project" if relative.parts[0] == "selected_projects" else "Learning lab"
        url = relative.as_posix() + "/reports/"
        published.append((title, category, url))
        print(f"Prepared: {relative}/reports/index.html")
    (output / "index.html").write_text(make_homepage(published), encoding="utf-8")
    (output / ".nojekyll").touch()
    print(f"Ready for Pages: {len(published)} report(s), {output}")


if __name__ == "__main__":
    main()
