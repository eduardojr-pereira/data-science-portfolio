<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Data Science Portfolio

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white&style=for-the-badge) ![Data Science](https://img.shields.io/badge/Data-Science-21618C?style=for-the-badge)

*Selected applied projects, learning experiments and original academic exercises in Data Science.*

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

**Current status:** Two projects are available in the portfolio: **Bike Sharing**, a selected applied data-analysis case study, and **Hangman Game**, an interactive Python and JavaScript Learning Lab. Both have project documentation and browser-based demonstrations. Bike Sharing presents retrospective analyses rather than production forecasts; notebook rerun limitations remain documented in its project README.

**Languages:** the portfolio and both current projects provide English and Brazilian Portuguese documentation. The Hangman browser game also includes a bilingual interface.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="contents"></a>

## Contents

### Project Collections

| Collection | Purpose |
|---|---|
| [Selected Projects](./selected_projects/README.md) | Curated projects with a business question, evidence, limitations and reproducible outputs |
| [Learning Labs](./learning_labs/README.md) | Smaller notebooks and technique-focused studies, regardless of academic origin |
| [Independent Experiments](./independent_experiments/README.md) | Exploratory investigations not yet promoted to curated case studies |

### Published Projects

| Project | Collection | Online experience | Source / documentation |
|---|---|---|---|
| **Bike Sharing — Demand & Operational Insights** | Selected Projects | [Interactive report](https://eduardojr-pereira.github.io/data-science-portfolio/selected_projects/bike_sharing/reports/) | [README](./selected_projects/bike_sharing/README.md) · [Notebook](./selected_projects/bike_sharing/bike_sharing_analysis.ipynb) |
| **Hangman Game — Python Learning Lab** | Learning Labs | [Play Hangman](https://eduardojr-pereira.github.io/data-science-portfolio/learning_labs/python_hangman_game/reports/index.html) | [README](./learning_labs/python_hangman_game/README.md) · [Python game](./learning_labs/python_hangman_game/hangman.py) |

[Explore the interactive portfolio showcase](https://eduardojr-pereira.github.io/data-science-portfolio/).

### Browse by Topic

The published projects currently cover **demand analytics and regression/model evaluation** (Bike Sharing) and **Python programming fundamentals and browser interactivity** (Hangman). Other topics will appear only when relevant projects are published.

### Directory Organization

~~~text
data-science-portfolio/
├── README.md / README.pt-BR.md
├── selected_projects/
│   ├── README.md / README.pt-BR.md
│   └── bike_sharing/
│       ├── bike_sharing_analysis.ipynb
│       ├── datasets/ and outputs/
│       └── reports/index.html
├── learning_labs/
│   ├── README.md / README.pt-BR.md
│   └── python_hangman_game/
│       ├── hangman.py and tests/
│       ├── web/
│       └── reports/index.html
├── independent_experiments/
└── tools/
~~~

Bike Sharing and Hangman are the first published entries in their respective collections. Historical source materials remain preserved separately; new projects will be included only after review.

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
ls independent_experiments
~~~

There is **no repository-wide `requirements.txt`**. Bike Sharing documents its Python dependencies and execution requirements; Hangman uses the Python standard library for its CLI and HTML/CSS/JavaScript for its browser game. Follow each project README rather than assuming a shared environment.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="usage"></a>

## How to Use

Start with [Selected Projects](./selected_projects/README.md) for applied analysis, or [Learning Labs](./learning_labs/README.md) for smaller programming projects. The [interactive showcase](https://eduardojr-pereira.github.io/data-science-portfolio/) links directly to both browser experiences.

Before publication, candidate work is reviewed for authorship, dataset provenance and redistribution rights, sensitive information, reproducibility, output integrity and documentation. Third-party teaching materials are not published as original work. The original historical collections remain preserved separately.

Future project entries will describe their purpose, source data, setup, methods, results, limitations and applicable licenses.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="validation"></a>

## Testing and Validation

| Verification | Recorded status |
|---|---|
| Repository structure and bilingual index | Available on `main` |
| Selected applied projects | Bike Sharing source and interactive report included |
| Learning labs | Hangman source, interactive game and eight passing Python unit tests |
| Bike Sharing reproducibility | Data validation, evaluation results and notebook execution caveats documented in the [project README](./selected_projects/bike_sharing/README.md) |
| New projects | Reviewed individually before inclusion |

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
