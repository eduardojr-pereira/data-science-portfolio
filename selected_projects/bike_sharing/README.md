<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Bike Sharing Demand Analysis

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white&style=for-the-badge) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=for-the-badge)

*Historical daily and hourly demand, rider behavior, chronological model validation, and interactive operational insights.*

</div>

<p align="center">
  <a href="../README.md">Back to Selected Projects</a> &nbsp;·&nbsp; <a href="../../README.md">Portfolio home</a> &nbsp;·&nbsp; <a href="https://eduardojr-pereira.github.io/data-science-portfolio/">Interactive showcase</a>
</p>

<p align="center">
  <a href="https://eduardojr-pereira.github.io/data-science-portfolio/selected_projects/bike_sharing/reports/index.html"><strong>▶ Open interactive HTML report in browser</strong></a>
</p>

---

## On This Page

<div align="center">

[Overview](#overview) • [Business Context](#business-context) • [Contents](#contents) • [Technologies](#technologies) • [Setup and Installation](#installation) • [Testing and Validation](#validation)
[How to Use](#usage) • [References](#references) • [License](#license) • [Contact](#contact)

</div>

---

<a id="overview"></a>

## Overview

**Business problem:** How do bike rentals vary across the day, calendar and rider segments, and which patterns could inform fleet operations? This case study examines the Capital Bikeshare system (Washington, D.C., 2011–2012) using **731 daily observations and 17,379 hourly records** from the same UCI source.

**Portfolio status:** Published as a Selected Project in the GitHub repository, with an interactive HTML report in the portfolio showcase. The daily and hourly datasets were reconciled, and an earlier version of the 57-cell notebook executed without errors. A complete rerun of the notebook after the report-building migration remains to be verified; publication does not imply that this rerun has occurred.

**Model evidence:** The daily Polynomial ridge (degree 2) model has a chronological holdout R² of **-0.257**. The hourly Random forest reaches R² **0.695** on its historical holdout. Their RMSE/MAE values have different units (rentals per day versus rentals per hour) and should not be compared directly.

**Scope:** Models use observed same-day or same-hour weather. This is **retrospective conditional demand estimation**, not verified day-ahead/hour-ahead forecasting or a causal model. Reuse of a previously inspected holdout across revisions limits independent generalization claims.

**Knowledge Base:** [Machine Learning](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/05_machine_learning) · [Data Analysis & Visualization](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/02_data_analysis_visualization).

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="business-context"></a>

## Business Context and Operational Insights

| Business question | Evidence and potential decision support |
|---|---|
| When is system-wide activity concentrated? | The largest average rental count per recorded hour occurs at **17:00–18:00**, averaging **461.5** rentals over recorded observations at that clock hour. Examine peak windows when planning *when* to rebalance fleets, subject to station-level validation. |
| Is demand changing over time? | Average daily rentals increased **64.4%** from 2011 to 2012. Capacity planning based only on early-period volume may undershoot later needs; this difference is descriptive, not causal. |
| Do rider segments matter? | Daily and hourly breakdowns distinguish casual and registered activity. Compare time-of-day and workday patterns before deciding whether commuting-oriented service or recreational availability deserves attention. |
| Can predictive models be deployed? | **Not on this evidence alone.** Daily RMSE 2,101.4, MAE 1,968.9, R² -0.257; hourly RMSE 121.8, MAE 84.9, R² 0.695. Weather is contemporaneously observed, and holdout reuse is acknowledged. |

**Decision boundaries:** Data describe system-level activity and do **not** identify individual stations, operational stockouts, actual rebalancing costs or customer wait times. Proposed staffing and redistribution actions are hypotheses to validate—not measured business impacts. Missing recorded clock hours are not automatically imputed as zero-demand observations.

<a id="contents"></a>

## Contents

### Project Files

| Resource | Description |
|---|---|
| [Notebook](./bike_sharing_analysis.ipynb) | One notebook for daily and hourly analyses |
| [Interactive HTML report](./reports/index.html) | Daily and hourly Plotly dashboard with limitations |
| [Daily dataset](./datasets/day.csv) | Original UCI daily records (731 days) |
| [Hourly dataset](./datasets/hour.csv) | Original UCI hourly records (17,379 hours) |
| [Dependencies](./requirements.txt) | Python dependencies |
| [Report generator](./report_builder.py) | Build the HTML from validated exports |
| [Daily model metrics](./outputs/metrics.json) | Daily model and method details |
| [Hourly model metrics](./outputs/hourly/metrics.json) | Hourly model and method details |
| [Hourly comparisons](./outputs/hourly/tables/hourly_model_comparison.csv) | Chronological cross-validation scores |
| [Daily comparison](./outputs/tables/model_comparison.csv) | Chronological cross-validation scores |

### Directory Structure

```text
bike_sharing/
├── README.md / README.pt-BR.md
├── bike_sharing_analysis.ipynb
├── report_builder.py
├── requirements.txt
├── datasets/
│   ├── day.csv
│   └── hour.csv
├── outputs/
│   ├── metrics.json
│   ├── figures/ and tables/
│   └── hourly/
│       ├── metrics.json
│       ├── figures/
│       └── tables/
└── reports/
    └── index.html

```

Both UCI aggregation files are included and verified against each other. Jupyter checkpoints, local backups and duplicate archives are excluded from publication. Plotly is bundled offline in the report; externally linked brand artwork may require network access.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="technologies"></a>

## Technologies

| Technology | Purpose |
|---|---|
| Python 3 | Executable analysis |
| pandas / NumPy | Data validation and numerical processing |
| scikit-learn | Time-series CV, preprocessing pipelines and regression |
| Matplotlib | Reproducible PNG figures |
| Plotly | Offline interactive HTML visuals |
| JupyterLab | Execution and inspection of the notebook |

No unneeded machine-learning frameworks or external dashboards are required.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="installation"></a>

## Setup and Installation

Run these commands **from the project directory** after placing it inside `04_Projetos`:

```bash
python -m pip install -r requirements.txt
python -m pip check
jupyter lab
```

Use the existing `jupyter-env` if configured. Open `bike_sharing_analysis.ipynb` and choose **Restart Kernel → Run All Cells**. The notebook also supports execution from the repository root and does not require an internet connection for the analysis. Installation may require internet access.

The last controlled execution used **Python 3.13.5, pandas 2.2.3, scikit-learn 1.8.0, Matplotlib 3.10.8 and Plotly 6.5.2**. Python 3.14 must be validated separately in the user's local environment.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="validation"></a>

## Testing and Validation

| Check | Recorded result |
|---|---|
| Source data integrity | 731 daily + 17,379 hourly records (2011–2012); no missing values or duplicate date-hour pairs; sums agree |
| Target consistency | `casual + registered = cnt` for all rows |
| Source dataset hash | SHA-256 `a6bcf826782d3c0fbfdcbeead17cd0884185a0dafe8ff10cd48a874ee7ba18be` |
| Train/test method | Chronological 584-day development / 147-day holdout |
| Model selection | `TimeSeriesSplit(n_splits=4)` on each development period only |
| Hourly validation | 13,891 training rows; 3,488 chronological holdout rows; Random Forest R² 0.695 |
| Preprocessing | `Pipeline` and fold-local `ColumnTransformer` |
| Best development CV | **Polynomial ridge (degree 2)**, mean RMSE **1,431.31** |
| Final holdout | RMSE **2,101.41**, MAE **1,968.90**, R² **-0.257** |
| Notebook execution | Previous version: 57 cells, 25 code cells executed without errors. Fresh rerun required after moving HTML build |
| HTML report | Generated from the notebook outputs |
| Local execution | Completed in the existing `jupyter-env`; exact Python version should be checked separately |

**Cross-version caution:** The same chronological holdout was inspected in the earlier v1 pilot. Thus, while this notebook keeps model selection inside development CV, this period is no longer an entirely unseen independent test across revisions. Future external validation is necessary.

**Interpretation:** A negative final R² means the selected estimator performs worse than the constant holdout mean on this period. The result is reported transparently rather than tuned against the same holdout. The historical notebook's numbers are not comparable because it used a different split and preprocessing method.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="usage"></a>

## How to Use

1. Read the single notebook top-to-bottom: daily EDA and models, followed by hourly patterns and independent hourly model evaluation.
2. Inspect the generated CSVs and `outputs/metrics.json` for auditable numerical results.
3. [Open the published interactive HTML report](https://eduardojr-pereira.github.io/data-science-portfolio/selected_projects/bike_sharing/reports/index.html) in your browser, or open `reports/index.html` locally. GitHub's source-file viewer does not render the report as a web application.
4. Review the limitations before citing metrics or describing the work in a résumé.

### Practical Conclusions

Demand rose strongly in 2012 (**64.4%** increase in mean daily rentals) and shows pronounced intraday variation. This supports **investigating** operating-hour coverage, supply distribution and segment-specific demand, but provides no direct measurement of station-level service quality.

The hourly Random Forest (Random forest) attained historical holdout R² **0.695**; the daily model attained **-0.257** and systematically underestimated late-2012 volume. These are not operational forecasts. Future work should prioritize independent data, feature availability at prediction time and prospective validation—not tuning to the same previously examined holdout.


<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="references"></a>

## References

| Resource | Link |
|---|---|
| Original dataset and attribution | [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) — Fanaee-T & Gama, DOI: 10.24432/C5W894 |
| Machine Learning | [Knowledge Base — Area 05](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/05_machine_learning) |
| Data Analysis & Visualization | [Knowledge Base — Area 02](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/02_data_analysis_visualization) |
| Data Preparation and Pipelines | [Technical Guide](https://github.com/eduardojr-pereira/data-science-knowledge-base/blob/main/05_machine_learning/reference_materials/04_preparacao_pipelines.pdf) |
| Validation and Optimization | [Technical Guide](https://github.com/eduardojr-pereira/data-science-knowledge-base/blob/main/05_machine_learning/reference_materials/11_validacao_otimizacao.pdf) |
| Linear Regression | [Technical Guide](https://github.com/eduardojr-pereira/data-science-knowledge-base/blob/main/05_machine_learning/reference_materials/12_regressao_linear.pdf) · [Cheat Sheet](https://github.com/eduardojr-pereira/data-science-knowledge-base/blob/main/05_machine_learning/cheat_sheets/cheat_sheet_regressao_linear.pdf) |
| Data leakage and pipelines | [scikit-learn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) |
| Time-aware cross-validation | [scikit-learn TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) |

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="license"></a>

## License

The **dataset** is attributed to Fanaee-T and Gama via UCI and is currently listed as **CC BY 4.0** ([license details](https://creativecommons.org/licenses/by/4.0/)). Retain the attribution and the source link when redistributing `day.csv`.

The separate `data-science-portfolio` repository does **not currently declare a repository-wide code/content license**. Do not assume the Knowledge Base's MIT or CC BY-NC licenses automatically apply. Source-code and documentation licensing is awaiting the owner's decision. Third-party logos, libraries and source data retain their respective rights.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="contact"></a>

## Contato

<div align="center">

<a href="https://eduardo-pereira.webflow.io/" title="Personal website — Eduardo Junior Pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="EP logo — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**

*Economics • Data Science • Python*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="Email" height="27"></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;
<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Vamos nos conectar no LinkedIn para trocar ideias e oportunidades.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Base de Conhecimento**](https://github.com/eduardojr-pereira/data-science-knowledge-base) &nbsp;•&nbsp; [**Site Pessoal**](https://eduardo-pereira.webflow.io/)

</div>

<p align="right"><a href="#readme-top">↑ VOLTAR AO TOPO</a></p>

---
