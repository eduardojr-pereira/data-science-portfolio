# Bike Sharing chart preparation

**Responsibility:** Document the project-owned preparation of chart specifications and locale dictionaries.

**Boundaries:** No shared UI, page generation, notebook execution, model training or publication. The canonical EP report contract owns chart presentation and composition.

`prepare_charts.py` reads the existing daily/hourly datasets, exported predictions, metrics and model tables. It emits 16 build-only JSON specifications under `content/charts/` and chart-only locale dictionaries (`translations.json`). The latter is the initial project dictionary; subsequent report copy belongs in the same file, not a second runtime dictionary. Regeneration writes to a new external directory and does not replace existing copy. Compare and reconcile chart keys before importing an intentional regeneration. The specifications contain the necessary trace values; no raw dataset or notebook is copied for publication. The specifications are inputs, not standalone HTML pages. `project.json` stays v1 during this preparation step; the actual v2 report will declare the charts and its authorized outputs in the next integration.

The historical chart IDs and analytical definitions are preserved: daily rider selector and date range controls, monthly/yearly daily means, annual rider totals, weather/weekday means and sample counts, Pearson correlations, CV means and standard deviations, chronological holdouts, observed-minus-estimated residuals, top 12 illustrative RF impurity importances, hourly profiles, weekday/hour means, working-day profiles and hourly MAE. Missing clock hours are not imputed. Exported predictions are not recomputed. The selected daily model is polynomial Ridge, not the illustrative RF; results are retrospective conditional estimates, not production forecasts. Chart categories retain stable data identifiers and localized display labels. The hourly heatmap uses a localized numerical weekday-code hover (0=Sunday), because the canonical contract does not translate two-dimensional per-cell text. Correlation and importance feature IDs are source identifiers, not translated data. Categorical colors use the EP canonical palette; continuous palettes are `vik` and `nuuk`. These presentation bindings require visual acceptance during the real report integration.

From the project directory in the existing Python environment, use a new directory under Downloads (do not overwrite the existing candidate):

```bash
python -B prepare_charts.py --output "$HOME/Downloads/bike-charts-candidate"
python -B tests/test_chart_specs.py --project . \
  --prepared "$HOME/Downloads/bike-charts-candidate" \
  --brand /path/to/ep-brand-assets
```

The test suite compares all 16 figures with the existing CSVs, verifies holdout metrics within 0.001 (rounding of exported predictions), and validates every spec through the canonical adapter and Plotly Python schema. The full browser and visual validation, actual report metadata, authorized files, and user-facing composition remain separate.
