<a id="readme-top"></a>

<div align="center">

[🇺🇸 English](./README.md) &nbsp;|&nbsp; [🇧🇷 Português](./README.pt-BR.md)

# Bike Sharing Demand Analysis

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge) ![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white&style=for-the-badge) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=for-the-badge)

*Daily rental analysis, leakage-aware regression benchmarks, and a standalone interactive report.*

</div>

---

## On This Page

<div align="center">

[Overview](#overview) • [Contents](#contents) • [Technologies](#technologies) • [Setup and Installation](#installation) • [Testing and Validation](#validation)  
[How to Use](#usage) • [References](#references) • [License](#license) • [Contact](#contact)

</div>

---

<a id="overview"></a>

## Overview

This academic regression exercise analyzes daily Capital Bikeshare rental counts for Washington, D.C., during **2011–2012**. It combines an extended exploratory study with chronological comparison of seven predefined baselines/regressors and a separate training-only tuning demonstration. It deliberately avoids random train/test splits and fits preprocessing inside training folds.

**Important scope:** Same-day observed weather is used as input. This experiment evaluates *conditional demand estimation*, **not** operational day-ahead forecasting. It does not demonstrate causal effects of temperature or weather.

**Portfolio status:** **Pilot under review — not approved for public release.** The revised notebook and generated report were executed successfully in a separate validation environment, and the user's earlier v1 pilot was executed locally without errors. Local execution of this expanded v2 remains pending. The source notebook was preserved in the historical archive.

**Key finding:** Polynomial ridge (degree 2) was selected by training-only time-series CV, but the final holdout yielded **R² = -0.257**, warning against promoting this model as a reliable forecast.

**Knowledge Base:** [Machine Learning](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/05_machine_learning) · [Data Analysis & Visualization](https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/02_data_analysis_visualization).

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="contents"></a>

## Contents

### Project Files

| Resource | Description |
|---|---|
| [Notebook](./bike_sharing_analysis.ipynb) | Fully documented, executed regression analysis |
| [Interactive HTML report](./reports/index.html) | Offline plots, verified metrics and explicit limitations |
| [Data source](./datasets/day.csv) | Unmodified UCI daily records (731 days) |
| [Environment](./requirements.txt) | Tested dependency ranges |
| [Report generator](./report_builder.py) | Rebuilds the HTML from validated data and model outputs |
| [Model comparison](./outputs/tables/model_comparison.csv) | Training-only cross-validation scores |
| [Holdout predictions](./outputs/tables/holdout_predictions.csv) | Final chronological test estimates |
| [Machine-readable metrics](./outputs/metrics.json) | Single source for report metrics |
| [Figures](./outputs/figures/) | Ten reproducible PNG charts |
| [Random forest importance](./outputs/tables/random_forest_feature_importance.csv) | Training-period feature importance (descriptive only) |

### Directory Structure

```text
bike_sharing/
├── README.md
├── README.pt-BR.md
├── requirements.txt
├── bike_sharing_analysis.ipynb
├── report_builder.py
├── datasets/
│   └── day.csv
├── outputs/
│   ├── metrics.json
│   ├── figures/
│   │   ├── correlation_matrix.png
│   │   ├── cross_validation_comparison.png
│   │   ├── demand_patterns.png
│   │   ├── distributions.png
│   │   ├── holdout_predictions.png
│   │   ├── random_forest_importances.png
│   │   ├── random_forest_tree_excerpt.png
│   │   ├── rentals_by_weather.png
│   │   ├── rider_type_mix.png
│   │   └── weekday_and_season.png
│   └── tables/
│       ├── model_comparison.csv
│       ├── holdout_predictions.csv
│       └── random_forest_feature_importance.csv
└── reports/
    └── index.html
```

The historical checkpoint, duplicate ZIP, and unused `hour.csv` are intentionally not copied. We include only data needed to reproduce the present analysis. The HTML contains the Plotly library offline; the linked EP logo still requires network access.

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
| Source data integrity | 731 daily records; 2011-01-01 to 2012-12-31; no missing values |
| Target consistency | `casual + registered = cnt` for all rows |
| Source dataset hash | SHA-256 `a6bcf826782d3c0fbfdcbeead17cd0884185a0dafe8ff10cd48a874ee7ba18be` |
| Train/test method | Chronological 584-day development / 147-day holdout |
| Model selection | `TimeSeriesSplit(n_splits=4)` on development data only |
| Preprocessing | `Pipeline` and fold-local `ColumnTransformer` |
| Best development CV | **Polynomial ridge (degree 2)**, mean RMSE **1,431.31** |
| Final holdout | RMSE **2,101.41**, MAE **1,968.90**, R² **-0.257** |
| Notebook execution | 43 cells completed without errors in the test environment |
| HTML report | Generated from the notebook outputs |
| Local Python 3.14 verification for expanded v2 | Pending (pilot v1 already executed locally) |

**Cross-version caution:** The same chronological holdout was inspected in the earlier v1 pilot. Thus, while this notebook keeps model selection inside development CV, this period is no longer an entirely unseen independent test across revisions. Future external validation is necessary.

**Interpretation:** A negative final R² means the selected estimator performs worse than the constant holdout mean on this period. The result is reported transparently rather than tuned against the same holdout. The historical notebook's numbers are not comparable because it used a different split and preprocessing method.

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

<a id="usage"></a>

## How to Use

1. Read the notebook top-to-bottom for data dictionary, data-quality checks, rider segmentation, calendar/weather analysis, correlations, regression comparison, tuning exercise, feature importance and final holdout.
2. Inspect the generated CSVs and `outputs/metrics.json` for auditable numerical results.
3. Open `reports/index.html` in a browser for the interactive, responsive executive view (GitHub's file viewer is not an HTML hosting service; publish through GitHub Pages only after approval).
4. Review the limitations before citing metrics or describing the work in a résumé.

### Practical Conclusions

Annual rental totals rose from 1,243,103 in 2011 to 2,049,576 in 2012. This is descriptive, not proof of a causal mechanism. The selected model failed to generalize well to the later 2012 holdout. The next scientific iteration should treat feature availability, data drift, and a new independent evaluation design as first-class concerns rather than optimizing against this test period.

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

## Contact

<div align="center">

<a href="https://eduardo-pereira.webflow.io/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="EP logo — Eduardo Junior Pereira" height="90"></a>

**Eduardo Junior Pereira**  
*Economics • Data Science • Python*

<a href="mailto:eduardojr.pereira@gmail.com"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/gmail_icon.svg" alt="Email" height="27"></a>&nbsp;&nbsp;<a href="https://www.linkedin.com/in/eduardo-jr-pereira/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/linkedin_icon.svg" alt="LinkedIn" height="27"></a>&nbsp;&nbsp;<a href="https://github.com/eduardojr-pereira"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/icons/github_icon.svg" alt="GitHub" height="27"></a>

[Let's connect on LinkedIn to exchange ideas and opportunities.](https://www.linkedin.com/in/eduardo-jr-pereira/)

[**Knowledge Base**](https://github.com/eduardojr-pereira/data-science-knowledge-base) &nbsp;•&nbsp; [**GitHub Portfolio**](https://github.com/eduardojr-pereira/data-science-portfolio) &nbsp;•&nbsp; [**Personal Website**](https://eduardo-pereira.webflow.io/)

</div>

<p align="right"><a href="#readme-top">↑ BACK TO TOP</a></p>

---

