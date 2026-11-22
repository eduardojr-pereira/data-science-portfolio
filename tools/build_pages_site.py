#!/usr/bin/env python3
"""Build a responsive GitHub Pages showcase from approved project reports.

Run from any directory:
    python tools/build_pages_site.py --output /tmp/portfolio-pages-preview

Only report directories and verified generated outputs are published, never source
notebooks, raw data, or arbitrary project files. Project descriptions and topics
are editorial metadata; do not infer scientific claims from a filename.
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
REPO = "https://github.com/eduardojr-pereira/data-science-portfolio"
KNOWLEDGE = "https://github.com/eduardojr-pereira/data-science-knowledge-base"
WEBSITE = "https://eduardo-pereira.webflow.io/"
LOGO = "https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png"

# Add an entry after reviewing and approving each project; discovered reports
# without metadata are listed conservatively (no invented tools or findings).
PROJECT_METADATA = {
    "selected_projects/bike_sharing": {
        "name": "Bike Sharing — Demand & Operational Insights",
        "description": "Explore historical daily and hourly bicycle rental demand, rider segments, seasonal patterns, and time-aware model validation. Results are retrospective, not production forecasts.",
        "topics": ("Data Analytics", "Machine Learning"),
        "technologies": ("Python", "pandas", "scikit-learn", "Plotly"),
        "notebook": "bike_sharing_analysis.ipynb",
        "featured": True,
    },
}


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
    return sorted(report for collection in REPORT_COLLECTIONS
        if (ROOT / collection).is_dir()
        for report in (ROOT / collection).rglob("reports/index.html")
        if not any(part.startswith(".") for part in report.relative_to(ROOT).parts))


def ensure_valid_local_links(source_html: Path, parser: PageLinks) -> None:
    for url in parser.urls:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
            continue
        destination = (source_html.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(ROOT) or not destination.is_file():
            raise RuntimeError(f"Missing or unsafe local link in {source_html}: {url}")
        project = source_html.parent.parent
        if not (destination.is_relative_to(project / "reports") or destination.is_relative_to(project / "outputs")):
            raise RuntimeError(f"Link points outside published report assets: {url}")


def make_homepage(reports: list[dict[str, object]]) -> str:
    topics = sorted({t for p in reports for t in p["topics"]})
    filters = ['<button class="filter is-active" type="button" data-topic="all" aria-pressed="true">All projects</button>']
    filters += [f'<button class="filter" type="button" data-topic="{escape(t, quote=True)}" aria-pressed="false">{escape(t)}</button>' for t in topics]
    cards = []
    for p in reports:
        collection = str(p["collection"])
        kind = "Selected Project" if collection == "selected_projects" else "Learning Lab"
        topic_tags = "".join(f'<span class="pill">{escape(str(t))}</span>' for t in p["topics"])
        tech_tags = "".join(f'<span class="tech">{escape(str(t))}</span>' for t in p["technologies"])
        document_links = [f'<a href="{escape(str(p["report"]), quote=True)}">Interactive report <span aria-hidden="true">↗</span></a>']
        if p["readme"]:
            document_links.append(f'<a href="{escape(str(p["readme"]), quote=True)}">Documentation <span aria-hidden="true">↗</span></a>')
        if p["notebook"]:
            document_links.append(f'<a href="{escape(str(p["notebook"]), quote=True)}">Notebook <span aria-hidden="true">↗</span></a>')
        label = "Featured · " if p["featured"] else ""
        cards.append(f'''<article class="project-card" data-collection="{escape(collection, quote=True)}" data-topics="{escape('|'.join(p['topics']), quote=True)}">
  <div class="card-head"><span class="eyebrow">{label}{kind}</span></div>
  <h3>{escape(str(p['name']))}</h3>
  <p>{escape(str(p['description']))}</p>
  <div class="tag-row" aria-label="Project categories">{topic_tags}</div>
  <div class="tag-row technologies" aria-label="Technologies">{tech_tags}</div>
  <div class="card-links">{' '.join(document_links)}</div>
</article>''')
    markup = '\n'.join(cards)
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<meta name="description" content="Applied data science projects, reproducible notebooks, and interactive analytical reports.">
<title>Data Science Portfolio · Eduardo Junior Pereira</title>
<style>
:root{{--bg:#0c1525;--surface:#14243a;--line:#28445f;--ink:#e7eef9;--muted:#abc0d4;--aqua:#67d8e9;--orange:#ffc07a;color-scheme:dark;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--ink)}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;min-height:100vh;background:radial-gradient(ellipse at top right,#162a40 0%,#0c1525 65%)}}a{{color:inherit}}a:focus-visible,button:focus-visible{{outline:2px solid var(--orange);outline-offset:3px}}
.container{{max-width:1120px;margin:auto;padding-left:24px;padding-right:24px}}
.site-header{{border-bottom:1px solid #263b51;background:#0c1525e8}}.header-inner{{display:flex;align-items:center;justify-content:space-between;gap:22px;min-height:86px}}
.brand{{display:inline-flex;align-items:center;gap:12px;text-decoration:none;min-width:0}}.brand img{{width:48px;height:48px;object-fit:contain}}.brand-name{{font-weight:760;letter-spacing:.055em;font-size:13px;line-height:1.35}}.brand-name small{{display:block;font-size:10px;color:var(--aqua);letter-spacing:.1em}}
.top-nav{{display:flex;align-items:center;gap:22px;flex-wrap:wrap}}.top-nav a{{font-size:13px;color:#d8e4f2;text-decoration:none}}.top-nav a:hover,.top-nav a:focus-visible{{color:#fff}}
.hero{{padding-top:62px;padding-bottom:40px}}.intro-label,.eyebrow{{text-transform:uppercase;color:var(--aqua);font-size:12px;letter-spacing:.09em;font-weight:700}}h1{{font-size:clamp(36px,6vw,64px);letter-spacing:-.045em;margin:12px 0 14px}}.lead{{font-size:17px;max-width:750px;line-height:1.75;color:var(--muted)}}
.section{{margin-bottom:48px}}h2{{font-size:25px;letter-spacing:-.025em;margin:0 0 12px}}.section-subtitle{{font-size:14px;color:var(--muted);line-height:1.7;margin:0 0 20px}}.filters,.collection-filters,.tag-row{{display:flex;gap:9px;flex-wrap:wrap}}.filter{{border:1px solid #38546d;background:#182b40;color:var(--ink);border-radius:999px;padding:9px 15px;font:inherit;font-size:13px;cursor:pointer}}.filter:hover,.filter.is-active{{border-color:var(--aqua);background:#23445a;color:#e9fcff}}.collection-filters{{margin-top:12px}}

.collection-fieldset{{display:flex;flex-wrap:wrap;align-items:center;gap:13px 28px;border:0;padding:0 0 20px;margin:0 0 18px;border-bottom:1px solid var(--line)}}
.collection-fieldset legend{{font-size:13px;font-weight:700;margin-bottom:13px;color:#bdeeff}}
.collection-option{{display:inline-flex;align-items:center;gap:8px;font-size:13px;cursor:pointer;color:#d8e4f2}}
.collection-option input{{accent-color:var(--aqua);width:16px;height:16px;cursor:pointer}}
.collection-option:hover{{color:#fff}}.area-filters h3{{font-size:13px;color:#bdeeff;margin:0 0 12px}}
.projects{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}}.project-card{{display:flex;flex-direction:column;gap:12px;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:26px}}.project-card:hover{{border-color:#507593}}.project-card h3{{font-size:23px;line-height:1.3;letter-spacing:-.025em;margin:0}}.project-card p{{color:#bbccdd;line-height:1.65;font-size:14px;margin:0;flex:1}}.pill,.tech{{font-size:11px;padding:5px 9px;border-radius:6px;background:#233e56;color:#b6edff}}.tech{{background:#273345;color:#e2ebf5}}.technologies{{padding-bottom:6px}}.card-links{{display:flex;gap:12px 18px;flex-wrap:wrap;border-top:1px solid #34516a;padding-top:18px}}.card-links a{{font-size:13px;color:#bdeeff;text-decoration-color:var(--aqua);text-underline-offset:5px;font-weight:650}}.card-links a:hover{{color:#fff}}
.empty{{color:var(--muted);border:1px dashed #3c5368;border-radius:12px;padding:22px}}[hidden]{{display:none!important}}
.site-footer{{border-top:1px solid #263b51;text-align:center;padding:34px 16px 48px;color:var(--muted);font-size:13px}}.site-footer img{{width:72px;height:auto}}.site-footer p{{line-height:1.7}}.site-footer a{{color:#bdeeff;text-decoration-color:var(--aqua);text-underline-offset:3px}}.site-footer a:hover,.site-footer a:focus-visible{{color:#fff}}
@media(max-width:960px){{.projects{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media(max-width:700px){{.projects{{grid-template-columns:1fr}}.header-inner{{align-items:flex-start;flex-direction:column;padding-top:16px;padding-bottom:18px;gap:15px}}.top-nav{{gap:10px 18px}}.top-nav a{{font-size:12px}}.brand img{{width:43px;height:43px}}.hero{{padding-top:35px}}.project-card{{padding:21px}}}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style></head><body>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="https://eduardojr-pereira.github.io/data-science-portfolio/" aria-label="Data Science Portfolio home"><img src="{LOGO}" alt="EP logo"><span class="brand-name">EDUARDO PEREIRA<small>DATA SCIENCE</small></span></a>
<nav class="top-nav" aria-label="Main navigation"><a href="{KNOWLEDGE}">Knowledge Base</a><a href="{WEBSITE}">Website</a><a href="{REPO}">GitHub</a></nav>
</div></header>
<main class="container">
<section class="hero" id="home"><div class="intro-label">Data Science · Analytics · Applied Projects</div><h1>Data Science Portfolio</h1><p class="lead">Explore applied analyses, interactive reports and reproducible methods. Each project connects a practical question to evidence, results and limitations, with source code and documentation available on GitHub.</p></section>
<section class="section" aria-labelledby="explore-title"><h2 id="explore-title">Explore by category</h2><p class="section-subtitle">Filter projects by area or collection. Only published reports are shown.</p>
<fieldset class="collection-fieldset"><legend>Collection</legend>
<label class="collection-option"><input type="radio" name="collection" value="all" checked> All Projects</label>
<label class="collection-option"><input type="radio" name="collection" value="selected_projects"> Selected Projects</label>
<label class="collection-option"><input type="radio" name="collection" value="learning_labs"> Learning Labs</label>
</fieldset>
<div class="area-filters"><h3>Area</h3><div class="filters" role="group" aria-label="Project areas">{''.join(filters)}</div></div>
</section>
<section class="section" aria-labelledby="projects-title"><h2 id="projects-title">Projects &amp; reports</h2><p class="section-subtitle" id="result-count" aria-live="polite"></p><div class="projects" id="projects">{markup}</div><p class="empty" id="empty" hidden>No published projects match these filters. Choose another category or collection.</p></section>
</main>
<footer class="site-footer"><a href="{WEBSITE}" aria-label="Personal website"><img src="{LOGO}" alt="EP logo"></a><p><strong>Eduardo Junior Pereira</strong><br>Economics · Data Science · Python</p><p><a href="mailto:eduardojr.pereira@gmail.com">Email</a> · <a href="https://www.linkedin.com/in/eduardo-jr-pereira/">LinkedIn</a> · <a href="https://github.com/eduardojr-pereira">GitHub</a> · <a href="{WEBSITE}">Personal Website</a></p></footer>
<script>
(function() {{
let topic='all',collection='all';
const cards=Array.from(document.querySelectorAll('.project-card'));
function apply() {{let visible=0;cards.forEach(card=>{{const topics=card.dataset.topics.split('|');const show=(topic==='all'||topics.includes(topic))&&(collection==='all'||card.dataset.collection===collection);card.hidden=!show;if(show)visible++;}});document.getElementById('empty').hidden=visible!==0;document.getElementById('result-count').textContent=visible+' published '+(visible===1?'project':'projects')+' shown';}}
document.querySelectorAll('button[data-topic]').forEach(button=>button.addEventListener('click',()=>{{topic=button.dataset.topic;document.querySelectorAll('button[data-topic]').forEach(b=>{{let selected=b===button;b.classList.toggle('is-active',selected);b.setAttribute('aria-pressed',String(selected));}});apply();}}));document.querySelectorAll('input[name="collection"]').forEach(input=>input.addEventListener('change',()=>{{if(input.checked){{collection=input.value;apply();}}}}));apply();
}})();
</script></body></html>'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Destination for static Pages artifacts")
    args = parser.parse_args()
    output = args.output.expanduser().resolve()
    if output == ROOT or ROOT.is_relative_to(output) or output.is_relative_to(ROOT):
        raise SystemExit("Output directory must be outside the Git repository")
    reports = discover_reports()
    if not reports:
        raise SystemExit("No reports/index.html found under selected_projects/ or learning_labs/")
    parsed: list[tuple[Path, PageLinks]] = []
    for report in reports:
        page = PageLinks()
        page.feed(report.read_text(encoding="utf-8"))
        ensure_valid_local_links(report, page)
        parsed.append((report, page))
    if output.exists():
        if not (output / ".portfolio-pages-build").is_file():
            raise SystemExit(f"Refusing to overwrite an unmarked directory: {output}")
        shutil.rmtree(output)
    output.mkdir(parents=True)
    (output / ".portfolio-pages-build").touch()
    published: list[dict[str, object]] = []
    for report, page in parsed:
        project = report.parent.parent
        relative = project.relative_to(ROOT)
        name = relative.as_posix()
        for asset_root in (project / "reports", project / "outputs"):
            if asset_root.is_dir() and any(p.is_symlink() for p in asset_root.rglob("*")):
                raise RuntimeError(f"Symlinks are not allowed in published assets: {asset_root}")
        destination = output / relative
        shutil.copytree(project / "reports", destination / "reports")
        if (project / "outputs").is_dir():
            shutil.copytree(project / "outputs", destination / "outputs")
        meta = PROJECT_METADATA.get(name, {})
        report_title = " ".join(page.title_parts).split(" · ", 1)[0].strip()
        notebook = project / str(meta.get("notebook", "")) if meta.get("notebook") else None
        readme = project / "README.md"
        published.append({
            "name": str(meta.get("name") or report_title or project.name.replace('_',' ').title()),
            "description": str(meta.get("description") or "Explore the published interactive report and consult the project documentation for scope and limitations."),
            "topics": tuple(meta.get("topics") or ("Data Analytics" if relative.parts[0]=="selected_projects" else "Learning Labs",)),
            "technologies": tuple(meta.get("technologies") or ()),
            "collection": relative.parts[0],
            "featured": bool(meta.get("featured", False)),
            "report": name + "/reports/",
            "readme": REPO + "/blob/main/" + name + "/README.md" if readme.is_file() else None,
            "notebook": REPO + "/blob/main/" + name + "/" + notebook.name if notebook and notebook.is_file() else None,
        })
        print(f"Prepared: {name}/reports/index.html")
    published.sort(key=lambda p: (not p["featured"], p["name"]))
    (output / "index.html").write_text(make_homepage(published), encoding="utf-8")
    (output / ".nojekyll").touch()
    print(f"Ready for Pages: {len(published)} report(s), {output}")


if __name__ == "__main__":
    main()
