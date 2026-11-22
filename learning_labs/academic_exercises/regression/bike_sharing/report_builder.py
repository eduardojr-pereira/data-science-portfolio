from __future__ import annotations

import argparse
import json
from html import escape
from pathlib import Path
from string import Template

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.io import to_html
from plotly.offline import get_plotlyjs


COLORS = {
    "background": "#0c1525",
    "card": "#14243a",
    "aqua": "#67d8e9",
    "blue": "#7f98ff",
    "orange": "#ffc07a",
    "green": "#87dbc0",
    "red": "#ff9898",
    "muted": "#a7bfd3",
}


def _safe_float(value):
    return f"{float(value):,.2f}"


def _layout(fig, title, y_title=None, height=370, legend_orientation="h"):
    fig.update_layout(
        title=dict(text=title, font=dict(size=17)),
        template="plotly_dark",
        paper_bgcolor=COLORS["card"],
        plot_bgcolor=COLORS["card"],
        font=dict(family="Inter, system-ui, sans-serif", color="#e7eef9", size=12),
        legend=dict(orientation=legend_orientation, y=1.12, x=0),
        margin=dict(l=50, r=20, t=76, b=50),
        height=height,
        hoverlabel=dict(bgcolor="#253852", font_size=12),
        yaxis=dict(title=y_title, gridcolor="#31435a", zerolinecolor="#31435a"),
        xaxis=dict(gridcolor="#31435a"),
    )
    return fig


def _figure_html(fig, plot_id):
    return to_html(
        fig,
        full_html=False,
        include_plotlyjs=False,
        div_id=plot_id,
        config={"responsive": True, "displaylogo": False,
                "modeBarButtonsToRemove": ["lasso2d", "select2d"]},
    )


def build_html_report(project_root: Path | None = None, *, metrics_path: Path | None = None,
                      daily_data_path: Path | None = None,
                      predictions_path: Path | None = None,
                      output_path: Path | None = None) -> Path:
    """Render a self-contained interactive report without retraining models.

    Backwards-compatible with the existing notebook call using metrics_path,
    daily_data_path, predictions_path and output_path keyword arguments.
    """
    if project_root is None:
        project_root = Path(output_path).parent.parent if output_path else Path(__file__).parent
    project_root = Path(project_root).resolve()
    dataset_path = Path(daily_data_path) if daily_data_path else project_root / "datasets" / "day.csv"
    metrics_path = Path(metrics_path) if metrics_path else project_root / "outputs" / "metrics.json"
    models_path = project_root / "outputs" / "tables" / "model_comparison.csv"
    predictions_path = Path(predictions_path) if predictions_path else project_root / "outputs" / "tables" / "holdout_predictions.csv"
    importances_path = project_root / "outputs" / "tables" / "random_forest_feature_importance.csv"
    for p in (dataset_path, metrics_path, models_path, predictions_path, importances_path):
        if not p.is_file():
            raise FileNotFoundError(f"Missing validated source artifact: {p}")

    daily = pd.read_csv(dataset_path, parse_dates=["dteday"]).sort_values("dteday")
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    models = pd.read_csv(models_path).sort_values("cv_mean_rmse")
    preds = pd.read_csv(predictions_path, parse_dates=["date"]).sort_values("date")
    imp = pd.read_csv(importances_path).sort_values("importance", ascending=False).head(12)

    if daily.empty or preds.empty or models.empty or imp.empty:
        raise ValueError("An input data export is empty")
    if not (daily["casual"] + daily["registered"] == daily["cnt"]).all():
        raise ValueError("Rider totals in daily source are inconsistent")
    if int(metrics["data"]["records"]) != len(daily):
        raise ValueError("Notebook metadata does not match source dataset")
    if int(metrics["methodology"]["holdout_size"]) != len(preds):
        raise ValueError("Holdout export does not match metadata")

    model_name = metrics["validation"]["selected_model"]
    test = metrics["validation"]["holdout"]
    report_path = Path(output_path) if output_path else project_root / "reports" / "index.html"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    # 1. Time series — Plotly controls switch among rider segments.
    demand = go.Figure()
    series = [("All rentals", "cnt", COLORS["aqua"]),
              ("Registered", "registered", COLORS["blue"]),
              ("Casual", "casual", COLORS["orange"])]
    for i, (label, column, color) in enumerate(series):
        demand.add_trace(go.Scatter(x=daily["dteday"], y=daily[column], name=label,
                                    mode="lines", visible=(i == 0),
                                    line=dict(color=color, width=1.65)))
    demand.update_layout(
        updatemenus=[dict(buttons=[dict(label=label, method="update",
                                       args=[{"visible": [j == i for j in range(len(series))]}])
                                  for i, (label, _, _) in enumerate(series)],
                         direction="down", x=0.99, xanchor="right", y=1.15, yanchor="top",
                         showactive=True, bgcolor="#243753", bordercolor="#34536a")]
    )
    _layout(demand, "", "Rentals per day", height=420)
    # Reserve a dedicated, title-free control band within the Plotly figure.
    demand.update_layout(title=None, margin=dict(l=60, r=24, t=95, b=68))
    demand.update_xaxes(rangeslider_visible=True, rangeselector=dict(
        buttons=[dict(count=3, label="3m", step="month", stepmode="backward"),
                 dict(count=6, label="6m", step="month", stepmode="backward"),
                 dict(step="all", label="All")],
        bgcolor="#243753", activecolor="#345b73", x=0.0, y=1.15))

    # 2. Seasonality by month/year.
    daily["year"] = daily["dteday"].dt.year
    daily["month"] = daily["dteday"].dt.month
    monthly = daily.groupby(["year", "month"], as_index=False)["cnt"].mean()
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    seasonality = go.Figure()
    for year, color in ((2011, COLORS["blue"]), (2012, COLORS["aqua"])):
        df = monthly[monthly["year"] == year]
        seasonality.add_trace(go.Scatter(x=[month_names[m - 1] for m in df["month"]],
                                        y=df["cnt"], mode="lines+markers", name=str(year),
                                        line=dict(color=color, width=3)))
    _layout(seasonality, "Average daily rentals by month and year", "Mean daily rentals")

    # 3. Rider-type composition.
    composition = go.Figure()
    for column, label, color in (("registered", "Registered", COLORS["blue"]),
                                 ("casual", "Casual", COLORS["orange"])):
        values = daily.groupby("year")[column].sum()
        composition.add_bar(x=values.index.astype(str), y=values.values, name=label,
                            marker_color=color, hovertemplate="%{x}: %{y:,.0f}<extra>" + label + "</extra>")
    _layout(composition, "Annual rentals by rider type", "Recorded rentals")
    composition.update_layout(barmode="stack")

    # 4. Weather — descriptive comparison, no causal claims.
    labels = {1: "Clear / partly cloudy", 2: "Mist / cloudy", 3: "Light rain / snow", 4: "Severe weather"}
    weather = daily.groupby("weathersit")["cnt"].agg(["mean", "count"]).reset_index()
    weather_chart = go.Figure(go.Bar(
        x=[labels.get(int(code), f"Code {code}") for code in weather["weathersit"]],
        y=weather["mean"], marker_color=COLORS["aqua"],
        customdata=weather[["count"]].to_numpy(),
        hovertemplate="Mean rentals: %{y:,.0f}<br>Days: %{customdata[0]:,.0f}<extra></extra>"))
    _layout(weather_chart, "Mean rentals by recorded weather conditions", "Daily rentals")

    # 5. Weekday with proper original dataset coding.
    weekdays = daily.groupby("weekday")["cnt"].agg(["mean", "count"]).reindex(range(7))
    weekday_chart = go.Figure(go.Bar(x=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
                                    y=weekdays["mean"], marker_color=COLORS["orange"],
                                    customdata=weekdays[["count"]].to_numpy(),
                                    hovertemplate="Mean: %{y:,.0f}<br>Days: %{customdata[0]:.0f}<extra></extra>"))
    _layout(weekday_chart, "Daily rentals by day of the week", "Mean daily rentals")

    # 6. Correlation (only descriptive; not a basis for causal interpretation).
    correlations = daily[["cnt", "temp", "atemp", "hum", "windspeed", "casual", "registered"]].corr()
    corr = go.Figure(go.Heatmap(z=correlations.to_numpy(), x=correlations.columns,
                                y=correlations.columns, zmin=-1, zmax=1,
                                colorscale="RdBu", reversescale=True,
                                text=correlations.round(2).to_numpy(), texttemplate="%{text}",
                                hovertemplate="%{x} / %{y}: %{z:.2f}<extra></extra>"))
    _layout(corr, "Pairwise Pearson correlations", height=440)
    corr.update_layout(margin=dict(l=70, r=15, t=75, b=60))

    # 7. Model comparison — notebook CSV is the source of truth.
    cv = go.Figure(go.Bar(y=models["model"], x=models["cv_mean_rmse"], orientation="h",
                              error_x=dict(type="data", array=models["cv_std_rmse"], color=COLORS["muted"]),
                              marker_color=[COLORS["aqua"] if name == model_name else COLORS["blue"]
                                            for name in models["model"]],
                              hovertemplate="%{y}<br>Mean CV RMSE: %{x:,.1f}<extra></extra>"))
    _layout(cv, "Expanding-window cross-validation · lower RMSE is better", "", height=460)
    cv.update_yaxes(autorange="reversed")
    cv.update_xaxes(title="RMSE (rentals / day)")
    cv.update_layout(margin=dict(l=170, r=25, t=75, b=50))

    # 8. Holdout predictions and residuals.
    holdout = go.Figure()
    holdout.add_trace(go.Scatter(x=preds["date"], y=preds["observed_rentals"],
                                 name="Observed", line=dict(color=COLORS["aqua"], width=2)))
    holdout.add_trace(go.Scatter(x=preds["date"], y=preds["estimated_rentals"],
                                 name="Estimated", line=dict(color=COLORS["orange"], width=2)))
    _layout(holdout, "Chronological holdout · observed vs estimated", "Rentals per day")
    holdout.update_xaxes(rangeslider_visible=True)
    residual = preds["observed_rentals"] - preds["estimated_rentals"]
    residuals = go.Figure(go.Bar(x=preds["date"], y=residual,
                                 marker_color=[COLORS["red"] if v > 0 else COLORS["green"] for v in residual],
                                 hovertemplate="%{x|%Y-%m-%d}<br>Residual: %{y:,.1f}<extra></extra>"))
    residuals.add_hline(y=0, line_dash="dash", line_color=COLORS["muted"])
    _layout(residuals, "Holdout residuals · observed − estimated", "Rentals per day")

    # 9. Distinct illustrative RF importance: not the selected Polynomial ridge model.
    rf = go.Figure(go.Bar(y=imp["feature"], x=imp["importance"], orientation="h",
                          marker_color=COLORS["blue"],
                          hovertemplate="%{y}<br>Importance: %{x:.3f}<extra></extra>"))
    _layout(rf, "Random forest feature importance · illustrative model", "", height=430)
    rf.update_yaxes(autorange="reversed")
    rf.update_xaxes(title="Impurity-based importance")
    rf.update_layout(margin=dict(l=170, r=20, t=75, b=50))

    plots = {
        "plot-demand": demand,
        "plot-seasonality": seasonality,
        "plot-composition": composition,
        "plot-weather": weather_chart,
        "plot-weekday": weekday_chart,
        "plot-corr": corr,
        "plot-cv": cv,
        "plot-holdout": holdout,
        "plot-residuals": residuals,
        "plot-importance": rf,
    }
    chart_divs = {key: _figure_html(figure, key) for key, figure in plots.items()}
    if not any(row["model"] == model_name for row in models.to_dict("records")):
        raise ValueError("Selected model name absent from model_comparison.csv")
    sel_cv = float(models.loc[models["model"] == model_name, "cv_mean_rmse"].iloc[0])
    r2_value = float(test["r2"])
    r2_note = (
        "Negative R² indicates a poor fit relative to the holdout mean baseline. "
        "This is not evidence of deployment-ready prediction."
        if r2_value < 0 else
        "A nonnegative holdout R² does not establish out-of-time generalization in new conditions."
    )
    # Report embeds Plotly.js only once and references existing static notebook outputs.
    plotly_js = get_plotlyjs()
    data = {
        "project_title": "Bike Sharing Demand Analysis",
        "year1": f"{int(metrics['data']['annual_totals']['2011']):,}",
        "year2": f"{int(metrics['data']['annual_totals']['2012']):,}",
        "rows": f"{len(daily):,}",
        "rentals": f"{int(daily['cnt'].sum()):,}",
        "development": f"{int(metrics['methodology']['train_size']):,}",
        "holdout_days": f"{len(preds):,}",
        "selected_model": escape(model_name),
        "cv_rmse": _safe_float(sel_cv),
        "test_rmse": _safe_float(test["rmse"]),
        "test_mae": _safe_float(test["mae"]),
        "test_r2": f"{r2_value:.3f}",
        "r2_note": escape(r2_note),
        "holdout_start": preds["date"].iloc[0].strftime("%Y-%m-%d"),
        "holdout_end": preds["date"].iloc[-1].strftime("%Y-%m-%d"),
        "plotly_js": plotly_js,
        **{key.replace("-", "_"): val for key, val in chart_divs.items()},
    }

    template = Template(r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Interactive reproducible analysis of bike sharing demand, descriptive trends and time-series model validation.">
  <title>Bike Sharing Demand Analysis · EP Data Science</title>
  <style>
  :root{--bg:#0c1525;--card:#14243a;--border:#28445e;--text:#e7eef9;--muted:#a7bfd3;--aqua:#67d8e9;--orange:#ffc07a;--nav-orange:#ff9f43;--warn:#ffd19b}
  *{box-sizing:border-box} html{scroll-behavior:smooth;scroll-padding-top:88px}
  body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.55}
  a{color:var(--aqua);text-underline-offset:3px}a:hover{color:#e9ffff}
  .container{width:min(1180px,calc(100% - 36px));margin:auto}
  .nav{position:sticky;top:0;z-index:3;background:#0d1a2cef;border-bottom:1px solid var(--border);backdrop-filter:blur(12px)}
  .nav-inner{min-height:64px;display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;padding:12px 0}
  .brand{font-size:.9rem;font-weight:800;letter-spacing:.05em;color:white;text-decoration:none}
  .nav-links{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
  .nav-links a{position:relative;display:inline-flex;align-items:center;text-decoration:none;color:#cad8e8;font-size:.84rem;font-weight:600;padding:8px 9px;border-radius:8px;transition:color .25s ease}
  .nav-links a::after{content:"";position:absolute;left:9px;right:9px;bottom:3px;height:3px;background:var(--nav-orange);transform:scaleX(0);transform-origin:left;transition:transform .25s ease;border-radius:999px}
  .nav-links a:hover,.nav-links a:focus-visible,.nav-links a.is-active{color:#ffffff}
  .nav-links a:hover::after,.nav-links a:focus-visible::after,.nav-links a.is-active::after{transform:scaleX(1)}
  .nav-links a.is-active::after{background:var(--orange)}
  .nav-links a:focus-visible{outline:2px solid var(--nav-orange);outline-offset:3px}
  a:focus-visible{outline:2px solid var(--aqua);outline-offset:3px}
  @media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.nav-links a,.nav-links a::after{transition:none}}
  .hero{background:linear-gradient(125deg,#14375a 5%,#112642 50%,#102135);border-bottom:1px solid var(--border);padding:64px 0 52px}
  .eyebrow{font-size:.76rem;letter-spacing:.17em;text-transform:uppercase;font-weight:700;color:#8cdaec}
  h1{font-size:clamp(2.1rem,5vw,3.7rem);line-height:1.14;letter-spacing:-.035em;margin:12px 0}
  .lead{color:#c7d7e7;max-width:820px;font-size:1.09rem}.tags{display:flex;gap:8px;flex-wrap:wrap;margin-top:22px}
  .tag{font-size:.78rem;border:1px solid #527b94;background:#1a3a52;padding:6px 12px;border-radius:999px}
  main{padding:25px 0 80px}section{margin:36px 0 56px}.section-heading{margin:0 0 8px;font-size:1.55rem;letter-spacing:-.02em}
  .hint{color:var(--muted);font-size:.9rem;margin:0 0 19px;max-width:950px}.cards{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
  .stat,.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:18px;min-width:0}
  .stat small{color:var(--muted);display:block;font-size:.8rem}.stat strong{font-size:1.7rem;letter-spacing:-.03em;display:block;margin-top:4px}
  .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:15px}.chart{background:var(--card);border:1px solid var(--border);border-radius:15px;padding:10px;min-width:0;overflow:hidden}
  .chart.full{grid-column:1/-1}.chart > .plotly-graph-div{width:100%!important}
  .chart-heading{font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;font-size:1.07rem;font-weight:700;letter-spacing:-.015em;line-height:1.35;color:var(--text);margin:10px 12px 3px}
  .chart-subheading{font-size:.83rem;color:var(--muted);margin:0 12px 4px}
  .chart--demand .plotly-graph-div{margin-top:2px}
  .callout{border-left:4px solid #e7a958;background:#2e2a30;padding:16px 19px;border-radius:0 10px 10px 0;color:#f4e1ca}
  .callout strong{color:#ffd8a6}p{margin-top:8px}.card h3{margin:0 0 9px;font-size:1.1rem}.card p{color:#c7d7e7}.metric{font-size:1.35rem;font-weight:800;color:white}
  .caption{font-size:.82rem;color:var(--muted);padding:6px 4px 0}.downloads{display:flex;gap:10px;flex-wrap:wrap}
  .download{display:inline-flex;align-items:center;border:1px solid #547d94;text-decoration:none;padding:9px 14px;border-radius:9px;background:#1a3348;font-weight:650;font-size:.86rem}
  .gallery{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.gallery a{text-decoration:none;border:1px solid var(--border);border-radius:10px;overflow:hidden;background:var(--card)}
  .gallery img{width:100%;height:170px;object-fit:cover;background:white;display:block}.gallery span{display:block;padding:9px 12px;font-size:.85rem;color:#dfedf9}
  footer{border-top:1px solid var(--border);text-align:center;padding:34px 16px 48px;color:var(--muted);font-size:.85rem}footer img{width:72px;height:auto}
  .sr-only{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  @media(max-width:850px){.cards{grid-template-columns:repeat(2,minmax(0,1fr))}.gallery{grid-template-columns:repeat(2,minmax(0,1fr))}}
  @media(max-width:670px){.grid{grid-template-columns:1fr}.chart.full{grid-column:auto}.nav-links{gap:5px}.nav-links a{font-size:.78rem;padding:7px 8px}.gallery{grid-template-columns:1fr}.hero{padding:35px 0}.stat strong{font-size:1.4rem}}
  </style>
  <script>$plotly_js</script>
</head>
<body>
  <nav class="nav" aria-label="Main navigation"><div class="container nav-inner"><a class="brand" href="#top">EP / DATA SCIENCE</a>
    <div class="nav-links"><a href="#overview">Overview</a><a href="#exploration">Exploration</a><a href="#models">Models</a><a href="#findings">Conclusions</a><a href="#outputs">Outputs</a></div>
  </div></nav>
  <div id="top" class="hero"><div class="container">
    <div class="eyebrow">Interactive technical report · Academic regression exercise</div>
    <h1>Bike Sharing Demand Analysis</h1>
    <p class="lead">Explore demand patterns from Washington, D.C. (2011–2012), compare regression models through chronological validation, and examine the limitations of retrospective demand estimation.</p>
    <div class="tags"><span class="tag">Python</span><span class="tag">Pandas</span><span class="tag">scikit-learn</span><span class="tag">Plotly</span><span class="tag">Time-series CV</span></div>
  </div></div>
  <main class="container">
    <section id="overview"><h2 class="section-heading">Dataset overview</h2>
      <p class="hint">The UCI dataset contains daily bike rental totals and weather-related variables. These figures are historical observations, not forecasts.</p>
      <div class="cards"><div class="stat"><small>Daily observations</small><strong>$rows</strong></div><div class="stat"><small>Total rentals</small><strong>$rentals</strong></div><div class="stat"><small>Development days</small><strong>$development</strong></div><div class="stat"><small>Holdout days</small><strong>$holdout_days</strong></div></div>
      <div class="grid" style="margin-top:15px"><div class="card"><h3>2011</h3><span class="metric">$year1</span><p>Total recorded rentals</p></div>
      <div class="card"><h3>2012</h3><span class="metric">$year2</span><p>Total recorded rentals</p></div></div>
    </section>
    <section id="exploration"><h2 class="section-heading">Exploratory analysis</h2>
      <p class="hint">Hover to inspect values; use the modebar to zoom, pan or download chart images. In the first chart, switch rider groups and use the range slider to focus on a period.</p>
      <div class="grid">
        <div class="chart full chart--demand"><h3 class="chart-heading">Daily rental demand</h3>
          <p class="chart-subheading">Choose a rider segment or period; explore detailed values by hovering over the line.</p>
          $plot_demand</div>
        <div class="chart">$plot_seasonality</div><div class="chart">$plot_composition</div>
        <div class="chart">$plot_weather</div><div class="chart">$plot_weekday</div>
        <div class="chart full">$plot_corr<div class="caption">Correlations are descriptive; `cnt` is the sum of casual and registered rentals, so its association with those components is structural.</div></div>
      </div>
      <p class="hint" style="margin-top:16px">Weather comparisons are observational. Group sizes differ, and no causal effect should be inferred from these summaries.</p>
    </section>
    <section id="models"><h2 class="section-heading">Model evaluation</h2>
      <p class="hint">Candidate models are evaluated using expanding-window cross-validation on the development period. The final chronological holdout was examined in earlier pilot revisions, so it must not be presented as an untouched independent benchmark.</p>
      <div class="grid">
        <div class="chart full">$plot_cv</div>
        <div class="card"><h3>Selected candidate</h3><div class="metric">$selected_model</div><p>Mean CV RMSE: <strong>$cv_rmse</strong> daily rentals</p></div>
        <div class="card"><h3>Chronological holdout</h3><div class="metric">RMSE $test_rmse</div><p>MAE <strong>$test_mae</strong> · R² <strong>$test_r2</strong></p><p>$holdout_start to $holdout_end</p></div>
        <div class="chart full">$plot_holdout</div>
        <div class="chart full">$plot_residuals</div>
        <div class="chart full">$plot_importance<div class="caption">Importance comes from an illustrative Random Forest, not from the selected Polynomial Ridge model; impurity-based importances can be biased.</div></div>
      </div>
    </section>
    <section id="findings"><h2 class="section-heading">Key findings and limitations</h2>
      <div class="callout"><strong>Generalization warning:</strong> $r2_note</div>
      <div class="grid" style="margin-top:14px">
        <div class="card"><h3>Demand variation</h3><p>Rental counts vary across seasons, weather categories and rider groups. These are descriptive patterns, not causal explanations.</p></div>
        <div class="card"><h3>Interpretation of model performance</h3><p>Training-only cross-validation was used to select candidates. A difficult chronological holdout reveals limitations not evident from development-fold scores.</p></div>
        <div class="card"><h3>Same-day weather</h3><p>The models use observed same-day weather variables. This is <strong>retrospective conditional demand estimation</strong> and must not be described as a day-ahead forecast.</p></div>
        <div class="card"><h3>External validity</h3><p>These results cover a single city and 2011–2012. Prospective evaluation with a new period would be required before operational use.</p></div>
      </div>
    </section>
    <section id="outputs"><h2 class="section-heading">Validated outputs & additional figures</h2>
      <p class="hint">The HTML is built from the notebook's exported metrics and tables. Use these source artifacts to inspect exact numbers. Additional PNG figures remain available without reproducing them in new storage formats.</p>
      <div class="downloads">
        <a class="download" href="../outputs/metrics.json">Metrics JSON</a>
        <a class="download" href="../outputs/tables/model_comparison.csv">Model comparison CSV</a>
        <a class="download" href="../outputs/tables/holdout_predictions.csv">Holdout predictions CSV</a>
        <a class="download" href="../outputs/tables/random_forest_feature_importance.csv">Feature importance CSV</a>
      </div>
      <div class="gallery" style="margin-top:20px">
        <a href="../outputs/figures/distributions.png"><img loading="lazy" src="../outputs/figures/distributions.png" alt="Exploratory variable distributions"><span>Variable distributions</span></a>
        <a href="../outputs/figures/random_forest_tree_excerpt.png"><img loading="lazy" src="../outputs/figures/random_forest_tree_excerpt.png" alt="Illustrative Random Forest decision tree excerpt"><span>Tree excerpt</span></a>
        <a href="../outputs/figures/demand_patterns.png"><img loading="lazy" src="../outputs/figures/demand_patterns.png" alt="Notebook demand analysis"><span>Notebook demand patterns</span></a>
      </div>
    </section>
    <section id="references"><h2 class="section-heading">References and reproducibility</h2>
      <div class="card"><p><strong>Original dataset:</strong> <a href="https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset">UCI Bike Sharing Dataset</a>, Fanaee-T & Gama, DOI 10.24432/C5W894, distributed under CC BY 4.0 with attribution.</p>
      <p><strong>Knowledge Base:</strong> <a href="https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/05_machine_learning">Machine Learning</a> and <a href="https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/02_data_analysis_visualization">Data Analysis & Visualization</a>.</p>
      <p><strong>Implementation:</strong> execute <code>bike_sharing_analysis.ipynb</code> to regenerate data exports, then run <code>python report_builder.py</code> from the project directory to rebuild this HTML. The HTML requires no Python server and includes Plotly.js offline; GitHub Pages hosting is supported.</p></div>
    </section>
  </main>
  <footer><a href="https://eduardo-pereira.webflow.io/"><img src="https://raw.githubusercontent.com/eduardojr-pereira/ep-brand-assets/main/assets/logos/logo_initials.png" alt="EP logo"></a>
    <p><strong>Eduardo Junior Pereira</strong><br>Economics · Data Science · Python</p>
    <p><a href="mailto:eduardojr.pereira@gmail.com">Email</a> · <a href="https://www.linkedin.com/in/eduardo-jr-pereira/">LinkedIn</a> · <a href="https://github.com/eduardojr-pereira">GitHub</a> · <a href="https://eduardo-pereira.webflow.io/">Personal Website</a></p>
  </footer>
  <script>
  (() => {
    const links = [...document.querySelectorAll('.nav-links a[href^="#"]')];
    const sections = links.map(link => document.getElementById(link.hash.slice(1)));
    function updateActiveSection() {
      const threshold = 125;
      let current = null;
      sections.forEach(section => {
        if (section && section.getBoundingClientRect().top <= threshold) current = section.id;
      });
      links.forEach(link => {
        const active = Boolean(current && link.hash === '#' + current);
        link.classList.toggle('is-active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }
    window.addEventListener('scroll', updateActiveSection, {passive: true});
    window.addEventListener('resize', updateActiveSection);
    window.addEventListener('hashchange', updateActiveSection);
    updateActiveSection();
  })();
  </script>
</body></html>''')
    html = template.safe_substitute(data)
    report_path.write_text(html, encoding="utf-8")
    print(f"HTML report updated: {report_path}")
    print(f"Figures: {len(plots)} interactive Plotly charts; notebook and outputs unchanged")
    return report_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Regenerate the Bike Sharing Plotly HTML report from existing notebook outputs")
    parser.add_argument("--project-root", default=Path(__file__).resolve().parent, type=Path,
                        help="Bike sharing project directory; defaults to script location")
    args = parser.parse_args()
    build_html_report(args.project_root)
