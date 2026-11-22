<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Data Science Portfolio

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white&style=for-the-badge) ![Data Science](https://img.shields.io/badge/Data-Science-21618C?style=for-the-badge)

*A bilingual collection of selected applied projects, learning experiments and original academic exercises in Data Science.*

</div>

---

## On This Page

<div align="center">

[Overview](#overview) • [Contents](#contents) • [Setup and Installation](#setup) • [How to Use](#usage)

[Testing and Validation](#validation) • [References](#references) • [License](#license) • [Contact](#contact)

</div>

---

<a id="overview"></a>

## Overview

This repository is the practical project companion to the [Data Science Knowledge Base](https://github.com/eduardojr-pereira/data-science-knowledge-base). It distinguishes selected applied work from learning exercises, so visitors can explore projects according to their purpose and maturity.

**Current status:** Bike Sharing has been promoted locally to the first Selected Project. Its daily and hourly datasets reconcile, the prior 57-cell notebook executed (a fresh post-migration run remains pending), and the interactive report is under final review. Publication of the new path is pending; the models are retrospective analyses, not production forecasts.

**Languages:** this overview is available in English and Brazilian Portuguese. Future project material may use either language; its README will describe the actual content.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="contents"></a>

## Contents

### Project Collections

| Collection | Purpose |
|---|---|
| [Selected Projects](./selected_projects/README.md) | Curated projects with a business question, evidence, limitations and reproducible outputs |
| [Learning Labs](./learning_labs/README.md) | Smaller notebooks and technique-focused studies, regardless of academic origin |
| [Independent Experiments](./learning_labs/independent_experiments/README.md) | Exploratory investigations not yet promoted to curated case studies |

### Featured Selected Project

| Project | Interactive Report (after publication) | Notebook |
|---|---|---|
| Bike Sharing — Demand & Operational Insights | [GitHub Pages](https://eduardojr-pereira.github.io/data-science-portfolio/selected_projects/bike_sharing/reports/) | [Open notebook](./selected_projects/bike_sharing/bike_sharing_analysis.ipynb) |

### Browse by Topic

Topics such as regression, classification, NLP and demand analytics are navigational categories, not empty filesystem folders. More projects will be indexed here as they are validated.

### Directory Organization

~~~text
data-science-portfolio/
├── README.md / README.pt-BR.md
├── selected_projects/
│   ├── README.md / README.pt-BR.md
│   └── bike_sharing/
│       ├── bike_sharing_analysis.ipynb
│       ├── report_builder.py
│       ├── datasets/ (day.csv, hour.csv)
│       ├── outputs/ (daily and hourly)
│       └── reports/index.html
└── learning_labs/
    ├── README.md / README.pt-BR.md
    └── independent_experiments/
~~~

Bike Sharing is now the first locally promoted Selected Project. Historic materials remain preserved separately; future Learning Labs entries will be added only after review.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="setup"></a>

## Setup and Installation

**1. Clone this repository:**

~~~bash
git clone https://github.com/eduardojr-pereira/data-science-portfolio.git
cd data-science-portfolio
~~~

**2. Browse the available collections:**

~~~bash
ls selected_projects
ls learning_labs
ls learning_labs/independent_experiments
~~~

There is **no repository-wide `requirements.txt`**. The Bike Sharing pilot has its own dependencies and execution instructions. Consult each project README rather than assuming all projects share one Python environment.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="usage"></a>

## How to Use

Start with **Selected Projects** for applied problem-solving and conclusions. Use **Learning Labs** for smaller experiments and original academic exercises that illustrate individual techniques.

Before publication, candidate work is reviewed for authorship, dataset provenance and redistribution rights, sensitive information, reproducibility, output integrity and documentation. Third-party teaching materials are not published as original work. The original historical collections remain preserved separately.

Future project entries will describe their purpose, source data, setup, methods, results, limitations and applicable licenses.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="validation"></a>

## Testing and Validation

| Verification | Recorded status |
|---|---|
| Repository directories and placeholders | Published |
| Bilingual repository overview | Available |
| Selected applied projects | Bike Sharing promoted locally; publication pending |
| Learning labs | Dedicated section retained for future studies |
| Notebook execution or project-level reproducibility | Bike Sharing validation and limitations documented in its README |

**Publishing a pilot does not validate future projects.** Each project README documents its actual execution, reproducibility status and methodological limitations.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="references"></a>

## References

| Resource | Link |
|---|---|
| Data Science Knowledge Base | [Study notebooks and technical references](https://github.com/eduardojr-pereira/data-science-knowledge-base) |
| EP Brand Assets | [Shared logo and contact icons](https://github.com/eduardojr-pereira/ep-brand-assets) |
| JupyterLab | [Official documentation](https://jupyterlab.readthedocs.io/en/stable/) |
| Python | [Official documentation](https://docs.python.org/3/) |

Project-specific references will be documented alongside the relevant work.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="license"></a>

## License

A repository-wide license has **not yet been assigned** to this portfolio. Before releasing projects, original code, documentation and third-party data will be reviewed and the applicable licensing terms documented. Do not assume that the licenses of the separate Knowledge Base automatically apply here.

External datasets, images, libraries and brand assets retain their respective rights and terms.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="contact"></a>

## Contact

<div align="center">

<a href="https://eduardo-pereira.webflow.io/" title="Personal website — Eduardo Junior Pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="EP logo — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**

*Economics • Data Science • Python*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="Email" height="27"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;
<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Let's connect on LinkedIn to exchange ideas and opportunities.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Knowledge Base**](https://github.com/eduardojr-pereira/data-science-knowledge-base) &nbsp;•&nbsp; [**Personal Website**](https://eduardo-pereira.webflow.io/)

</div>

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---
