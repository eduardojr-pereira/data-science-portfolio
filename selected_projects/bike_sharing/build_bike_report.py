from __future__ import annotations

import argparse
import json
from html import escape
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from ep_brand import render_footer, logo_data_uri, render_references, render_outputs, render_project_links
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


BIKE_REPORT_TRANSLATIONS = '(function(){\n\'use strict\';\n  const bike = document.querySelector(\'.bike-local-nav\');\n  if (!bike) return;\n  const pt = {\n    \'Overview\':\'Visão geral\',\n    \'Business\':\'Negócio\',\n    \'Exploration\':\'Exploração\',\n    \'Hourly\':\'Padrões horários\',\n    \'Models\':\'Modelos\',\n    \'Conclusions\':\'Conclusões\',\n    \'Outputs\':\'Resultados\',\n    \'References\':\'Referências\',\n    \'Technical report · Regression analysis\':\'Relatório técnico · Análise de regressão\',\n    \'Bike Sharing Demand Analysis\':\'Análise da Demanda por Bicicletas Compartilhadas\',\n    \'Explore daily and hourly demand patterns from Washington, D.C. (2011–2012), compare regression models through chronological validation, and examine the limitations of retrospective demand estimation.\':\'Explore os padrões diários e horários da demanda em Washington, D.C. (2011–2012), compare modelos de regressão com validação cronológica e examine as limitações da estimativa retrospectiva da demanda.\',\n    \'Time-series CV\':\'Validação temporal\',\n    \'Dataset overview\':\'Visão geral dos dados\',\n    \'The UCI dataset contains daily and hourly bike rental totals and weather-related variables. These figures are historical observations, not forecasts.\':\'O conjunto de dados da UCI contém totais diários e horários de aluguéis de bicicletas e variáveis meteorológicas. Esses números representam observações históricas, não previsões.\',\n    \'Daily observations\':\'Observações diárias\',\n    \'Total rentals\':\'Total de aluguéis\',\n    \'Development days\':\'Dias de desenvolvimento\',\n    \'Holdout days\':\'Dias de teste cronológico\',\n    \'Total recorded rentals\':\'Total de aluguéis registrados\',\n    \'Business questions & operational insights\':\'Questões de negócio e insights operacionais\',\n    \'A historical system-level demand study: where might the operator investigate staffing, bicycle availability or rebalancing windows? These are planning hypotheses, not measured cost savings or station-level prescriptions.\':\'Um estudo histórico da demanda no sistema: em quais períodos o operador poderia investigar equipes, disponibilidade de bicicletas ou redistribuição? São hipóteses de planejamento, não economias comprovadas nem recomendações específicas por estação.\',\n    \'Most active clock hour\':\'Horário de maior movimento\',\n    \'Average\':\'Média de\',\n    \'461.5 rentals\':\'461,5 aluguéis\',\n    \'per recorded observation at this hour, over 2011–2012. Missing clock-hour records are not imputed as zero.\':\'por observação registrada nesse horário, em 2011–2012. Horários ausentes não foram imputados como zero.\',\n    \'Demand growth\':\'Crescimento da demanda\',\n    \'Change in mean daily rentals from 2011 to 2012. It does not establish the causes of growth or a future growth rate.\':\'Variação da média diária de aluguéis de 2011 para 2012. Isso não estabelece as causas do crescimento nem uma taxa futura.\',\n    \'Operational questions\':\'Questões operacionais\',\n    \'Compare registered and casual hourly patterns, workdays and non-workdays, and peak windows before planning inventory coverage. Station-level supply data are required to design actual rebalancing routes.\':\'Compare padrões horários de usuários registrados e ocasionais, dias úteis e não úteis e horários de pico antes de planejar a cobertura da frota. Dados de disponibilidade por estação são necessários para definir rotas de redistribuição.\',\n    \'Evidence, not a production forecast\':\'Evidências, não previsões em produção\',\n    \'Historical hourly holdout R²:\':\'R² do teste cronológico horário:\',\n    \'; daily holdout R²:\':\'; R² do teste cronológico diário:\',\n    \'. These models use observed contemporaneous weather; deployment requires available-at-prediction-time inputs and independent evaluation.\':\'. Esses modelos utilizam o clima observado no mesmo período; sua implantação exige variáveis disponíveis no momento da previsão e avaliação independente.\',\n    \'Exploratory analysis\':\'Análise exploratória\',\n    \'Hover to inspect values; use the modebar to zoom, pan or download chart images. In the first chart, switch rider groups and use the range slider to focus on a period.\':\'Passe o cursor para inspecionar valores; use a barra de ferramentas para ampliar, deslocar ou baixar imagens dos gráficos. No primeiro gráfico, alterne entre grupos de usuários e use o seletor de intervalo para focar um período.\',\n    \'Daily rental demand\':\'Demanda diária por aluguéis\',\n    \'Choose a rider segment or period; explore detailed values by hovering over the line.\':\'Escolha um segmento de usuários ou período; passe o cursor sobre a linha para explorar os valores.\',\n    \'Correlations are descriptive; `cnt` is the sum of casual and registered rentals, so its association with those components is structural.\':\'As correlações são descritivas; `cnt` é a soma dos aluguéis ocasionais e registrados, portanto a associação com esses componentes é estrutural.\',\n    \'Weather comparisons are observational. Group sizes differ, and no causal effect should be inferred from these summaries.\':\'As comparações meteorológicas são observacionais. Os grupos têm tamanhos diferentes, e não se deve inferir causalidade desses resumos.\',\n    \'Hourly patterns & validation\':\'Padrões horários e validação\',\n    \'The hourly UCI records cover the same 2011–2012 Capital Bikeshare rentals as the daily dataset, shown at a finer aggregation level. These are not additional rentals.\':\'Os registros horários da UCI abrangem os mesmos aluguéis do Capital Bikeshare de 2011–2012 presentes nos dados diários, em um nível mais detalhado. Não são aluguéis adicionais.\',\n    \'Recorded hourly observations\':\'Observações horárias registradas\',\n    \'Selected hourly candidate\':\'Modelo horário selecionado\',\n    \'Random forest\':\'Floresta aleatória\',\n    \'Hourly CV RMSE\':\'RMSE da validação horária\',\n    \'Hourly holdout R²\':\'R² do teste horário\',\n    \'Hourly chronological holdout\':\'Teste cronológico horário\',\n    \'76 days\':\'76 dias\',\n    \'Data completeness\':\'Completude dos dados\',\n    \'The source has\':\'A fonte possui\',\n    \'unrecorded clock hours across those days. The absent hours were not artificially imputed.\':\'horários sem registro nesses dias. As horas ausentes não foram imputadas artificialmente.\',\n    \'How to interpret:\':\'Como interpretar:\',\n    "Hourly and daily RMSE/MAE are measured in different units and should not be compared numerically. Both models are retrospective conditional estimates using observed weather at the target date/hour, not proven advance forecasts. The daily model\'s negative holdout R² is reported transparently. An earlier iteration already examined the holdout; this evaluation is not an untouched external benchmark.":\'O RMSE/MAE horário e diário é medido em unidades diferentes e não deve ser comparado numericamente. Ambos os modelos produzem estimativas condicionais retrospectivas usando o clima observado na data/hora de interesse, não previsões antecipadas comprovadas. O R² negativo do modelo diário no teste cronológico é apresentado de forma transparente. Uma versão anterior já examinou esse conjunto de teste; portanto, a avaliação não representa um teste externo ainda não explorado.\',\n    \'Operational questions: How do commute peaks differ from leisure use? Which hours would be important to examine for bicycle rebalancing and staffing? These associations are descriptive and do not prove that a specific intervention would increase demand.\':\'Questões operacionais: como os picos de deslocamento diferem do uso recreativo? Quais horários merecem investigação para redistribuição de bicicletas e dimensionamento de equipes? Essas associações são descritivas e não comprovam que uma intervenção específica aumentaria a demanda.\',\n    \'Daily model evaluation\':\'Avaliação do modelo diário\',\n    \'Candidate models are evaluated using expanding-window cross-validation on the development period. The final chronological holdout was examined in earlier pilot revisions, so it must not be presented as an untouched independent benchmark.\':\'Os modelos candidatos são avaliados por validação cruzada com janela de treinamento crescente no período de desenvolvimento. O conjunto final de teste cronológico já foi examinado em versões piloto anteriores e não pode ser apresentado como uma referência independente ainda não explorada.\',\n    \'Selected candidate\':\'Modelo selecionado\',\n    \'Polynomial ridge (degree 2)\':\'Ridge polinomial (grau 2)\',\n    \'Mean CV RMSE:\':\'RMSE médio da validação:\',\n    \'daily rentals\':\'aluguéis diários\',\n    \'Chronological holdout\':\'Teste cronológico\',\n    \'Importance comes from an illustrative Random Forest, not from the selected Polynomial Ridge model; impurity-based importances can be biased.\':\'A importância das variáveis vem de uma floresta aleatória ilustrativa, não do modelo Ridge polinomial selecionado; medidas baseadas na impureza podem apresentar vieses.\',\n    \'Key findings and limitations\':\'Principais resultados e limitações\',\n    \'Generalization warning:\':\'Alerta de generalização:\',\n    \'Negative R² indicates a poor fit relative to the holdout mean baseline. This is not evidence of deployment-ready prediction.\':\'Um R² negativo indica desempenho inferior à referência baseada na média do conjunto de teste. Isso não demonstra prontidão para previsões em produção.\',\n    \'Demand variation\':\'Variação da demanda\',\n    \'Rental counts vary across seasons, weather categories and rider groups. These are descriptive patterns, not causal explanations.\':\'A quantidade de aluguéis varia conforme as estações do ano, as condições meteorológicas e os grupos de usuários. São padrões descritivos, não explicações causais.\',\n    \'Interpretation of model performance\':\'Interpretação do desempenho dos modelos\',\n    \'Training-only cross-validation was used to select candidates. A difficult chronological holdout reveals limitations not evident from development-fold scores.\':\'A validação cruzada realizada apenas nos dados de treinamento foi utilizada para selecionar os candidatos. O teste cronológico mais difícil revela limitações que não aparecem nos resultados das partições de desenvolvimento.\',\n    \'Same-day weather\':\'Clima do mesmo dia\',\n    \'The models use observed same-day weather variables. This is\':\'Os modelos utilizam variáveis meteorológicas observadas no próprio dia. Trata-se de\',\n    \'retrospective conditional demand estimation\':\'estimativa retrospectiva condicional da demanda\',\n    \'and must not be described as a day-ahead forecast.\':\'e não deve ser descrita como previsão para o dia seguinte.\',\n    \'External validity\':\'Validade externa\',\n    \'These results cover a single city and 2011–2012. Prospective evaluation with a new period would be required before operational use.\':\'Esses resultados abrangem uma única cidade e os anos de 2011–2012. Uma avaliação prospectiva com novos dados seria necessária antes do uso operacional.\',\n    \'Validated outputs & additional figures\':\'Resultados validados e figuras adicionais\',\n    "The HTML is built from the notebook\'s exported metrics and tables. Use these source artifacts to inspect exact numbers. Additional PNG figures remain available without reproducing them in new storage formats.":\'O HTML é construído a partir de métricas e tabelas exportadas pelo notebook. Utilize esses arquivos para conferir os números exatos. As figuras PNG adicionais continuam disponíveis sem necessidade de reproduzi-las em outros formatos.\',\n    \'Daily metrics JSON\':\'Métricas diárias (JSON)\',\n    \'Hourly metrics JSON\':\'Métricas horárias (JSON)\',\n    \'Hourly model comparison CSV\':\'Comparação de modelos horários (CSV)\',\n    \'Hourly holdout predictions CSV\':\'Predições do teste horário (CSV)\',\n    \'Model comparison CSV\':\'Comparação de modelos (CSV)\',\n    \'Holdout predictions CSV\':\'Predições do teste (CSV)\',\n    \'Feature importance CSV\':\'Importância das variáveis (CSV)\',\n    \'Variable distributions\':\'Distribuições das variáveis\',\n    \'Tree excerpt\':\'Trecho de árvore\',\n    \'Notebook demand patterns\':\'Padrões de demanda do notebook\',\n    \'References and reproducibility\':\'Referências e reprodutibilidade\',\n    \'Original dataset:\':\'Conjunto de dados original:\',\n    \', Fanaee-T & Gama, DOI 10.24432/C5W894, distributed under CC BY 4.0 with attribution.\':\', Fanaee-T & Gama, DOI 10.24432/C5W894, distribuído sob CC BY 4.0, com atribuição.\',\n    \'Knowledge Base:\':\'Base de conhecimento:\',\n    \'Machine Learning\':\'Aprendizado de Máquina\',\n    \'and\':\'e\',\n    \'Data Analysis & Visualization\':\'Análise e Visualização de Dados\',\n    \'Implementation:\':\'Implementação:\',\n    \'execute\':\'execute\',\n    \'to regenerate data exports, then run\':\'para regenerar os dados exportados; depois execute\',\n    \'from the project directory to rebuild this HTML. The HTML requires no Python server and includes Plotly.js offline; GitHub Pages hosting is supported.\':\'na pasta do projeto para reconstruir este HTML. O HTML não requer servidor Python, inclui Plotly.js para uso offline e pode ser hospedado no GitHub Pages.\',\n    \'MAE\':\'MAE\',\n    \'rentals/hour · R²\':\'aluguéis/hora · R²\',\n  };\n  const rootNodes = [document.querySelector(\'.hero\'),document.querySelector(\'main\'),bike].filter(Boolean);\n  const originals = [];\n  const normalize = value => value.replace(/\\s+/g,\' \').trim();\n  for (const root of rootNodes) {\n    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);\n    while (walker.nextNode()) {\n      const node = walker.currentNode;\n      if (node.parentElement.closest(\'script,style,svg,.plotly-graph-div,.ep-references,.ep-outputs\')) continue;\n      const key = normalize(node.nodeValue);\n      if (Object.prototype.hasOwnProperty.call(pt,key)) originals.push({node,original:node.nodeValue,key});\n    }\n  }\n  function syncBike() {\n    const translated = document.documentElement.lang === \'pt-BR\';\n    for (const item of originals) {\n      if (!item.node.isConnected) continue;\n      if (!translated) { item.node.nodeValue = item.original; continue; }\n      const value = item.original;\n      const start = value.match(/^\\s*/)[0];\n      const end = value.match(/\\s*$/)[0];\n      item.node.nodeValue = start + pt[item.key] + end;\n    }\n  }\n  document.addEventListener(\'DOMContentLoaded\', syncBike);\n  document.addEventListener(\'ep:languagechange\', syncBike);\n})();\n'


BIKE_REFERENCES = {
    "data_source": {
        "name": "UCI Bike Sharing Dataset",
        "url": "https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset",
        "authors": "Fanaee-T & Gama",
        "doi": "10.24432/C5W894",
        "license": "CC BY 4.0",
        "note": {"en": "Distributed with attribution.", "pt-BR": "Distribuído com atribuição."},
    },
    "knowledge_base": [
        {"label": {"en": "Machine Learning", "pt-BR": "Aprendizado de Máquina"},
         "url": "https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/05_machine_learning"},
        {"label": {"en": "Data Analysis & Visualization", "pt-BR": "Análise e Visualização de Dados"},
         "url": "https://github.com/eduardojr-pereira/data-science-knowledge-base/tree/main/02_data_analysis_visualization"},
    ],
    "reproducibility": {
        "intro": {"en": "Review the project documentation for dependencies and data setup before executing the analysis.",
                  "pt-BR": "Consulte a documentação do projeto para configurar as dependências e os dados antes de executar a análise."},
        "steps": [
            {"label": {"en": "Clone the portfolio in your working directory.", "pt-BR": "Clone o portfólio no seu diretório de trabalho."},
             "command": "git clone https://github.com/eduardojr-pereira/data-science-portfolio.git"},
            {"label": {"en": "Clone EP Brand Assets alongside the portfolio, in the same parent directory.", "pt-BR": "Clone o EP Brand Assets ao lado do portfólio, no mesmo diretório pai."},
             "command": "git clone https://github.com/eduardojr-pereira/ep-brand-assets.git"},
            {"label": {"en": "Navigate to the Bike Sharing project.", "pt-BR": "Acesse o diretório do projeto Bike Sharing."},
             "command": "cd data-science-portfolio/selected_projects/bike_sharing"},
            {"label": {"en": "If you need to regenerate data exports, execute bike_sharing_analysis.ipynb using the configured Python environment.", "pt-BR": "Se precisar regenerar os dados exportados, execute bike_sharing_analysis.ipynb no ambiente Python configurado."}},
            {"label": {"en": "Build the HTML report from the existing validated exports.", "pt-BR": "Gere o relatório HTML a partir dos dados exportados e validados."},
             "command": "python build_bike_report.py"},
        ],
        "note": {"en": "Static HTML with offline Plotly.js. No Python server is required to view the generated report. GitHub Pages hosting is supported.",
                 "pt-BR": "HTML estático com Plotly.js offline. Não é necessário um servidor Python para visualizar o relatório gerado. Compatível com GitHub Pages."},
        "documentation": "https://github.com/eduardojr-pereira/data-science-portfolio/tree/main/selected_projects/bike_sharing",
    },
}


BIKE_OUTPUTS = {'items': [{'name': {'en': 'Daily metrics', 'pt-BR': 'Métricas diárias'},
            'origin': {'en': 'Daily analysis', 'pt-BR': 'Análise diária'},
            'description': {'en': 'Model performance and validation metrics.',
                            'pt-BR': 'Métricas de desempenho e validação dos modelos.'},
            'path': '../outputs/metrics.json',
            'format': 'JSON'},
           {'name': {'en': 'Hourly metrics', 'pt-BR': 'Métricas horárias'},
            'origin': {'en': 'Hourly analysis', 'pt-BR': 'Análise horária'},
            'description': {'en': 'Hourly model performance and data completeness.',
                            'pt-BR': 'Desempenho do modelo horário e completude dos dados.'},
            'path': '../outputs/hourly/metrics.json',
            'format': 'JSON'},
           {'name': {'en': 'Model comparison', 'pt-BR': 'Comparação de modelos'},
            'origin': {'en': 'Daily analysis', 'pt-BR': 'Análise diária'},
            'description': {'en': 'Cross-validation results for candidate models.',
                            'pt-BR': 'Resultados da validação cruzada dos modelos candidatos.'},
            'path': '../outputs/tables/model_comparison.csv',
            'format': 'CSV'},
           {'name': {'en': 'Hourly model comparison', 'pt-BR': 'Comparação de modelos horários'},
            'origin': {'en': 'Hourly analysis', 'pt-BR': 'Análise horária'},
            'description': {'en': 'Cross-validation results for hourly regression models.',
                            'pt-BR': 'Resultados da validação cruzada dos modelos de regressão '
                                     'horária.'},
            'path': '../outputs/hourly/tables/hourly_model_comparison.csv',
            'format': 'CSV'},
           {'name': {'en': 'Holdout predictions', 'pt-BR': 'Predições do teste'},
            'origin': {'en': 'Daily analysis', 'pt-BR': 'Análise diária'},
            'description': {'en': 'Observed and estimated daily rentals in the chronological holdout.',
                            'pt-BR': 'Aluguéis diários observados e estimados no teste cronológico.'},
            'path': '../outputs/tables/holdout_predictions.csv',
            'format': 'CSV'},
           {'name': {'en': 'Hourly holdout predictions', 'pt-BR': 'Predições do teste horário'},
            'origin': {'en': 'Hourly analysis', 'pt-BR': 'Análise horária'},
            'description': {'en': 'Observed and estimated hourly rentals in the chronological holdout.',
                            'pt-BR': 'Aluguéis horários observados e estimados no teste cronológico.'},
            'path': '../outputs/hourly/tables/hourly_holdout_predictions.csv',
            'format': 'CSV'},
           {'name': {'en': 'Feature importance', 'pt-BR': 'Importância das variáveis'},
            'origin': {'en': 'Random Forest', 'pt-BR': 'Floresta aleatória'},
            'description': {'en': 'Illustrative impurity-based feature importance.',
                            'pt-BR': 'Importância ilustrativa das variáveis baseada na impureza.'},
            'path': '../outputs/tables/random_forest_feature_importance.csv',
            'format': 'CSV'}],
 'figures': [{'name': {'en': 'Variable distributions', 'pt-BR': 'Distribuições das variáveis'},
              'description': {'en': 'Exploratory distributions and relationships between variables.',
                              'pt-BR': 'Distribuições e relações exploratórias entre variáveis.'},
              'path': '../outputs/figures/distributions.png'},
             {'name': {'en': 'Tree excerpt', 'pt-BR': 'Trecho de árvore'},
              'description': {'en': 'Structure of an illustrative Random Forest decision tree.',
                              'pt-BR': 'Estrutura de uma árvore de decisão ilustrativa da floresta '
                                       'aleatória.'},
              'path': '../outputs/figures/random_forest_tree_excerpt.png'},
             {'name': {'en': 'Demand patterns', 'pt-BR': 'Padrões de demanda'},
              'description': {'en': 'Historical rental trends and seasonality from the notebook.',
                              'pt-BR': 'Tendências históricas de aluguéis e sazonalidade do notebook.'},
              'path': '../outputs/figures/demand_patterns.png'}]}


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



PLOTLY_TRANSLATIONS = {
    # Chart titles
    "Average daily rentals by month and year":
        "Média diária de aluguéis por mês e ano",
    "Annual rentals by rider type":
        "Aluguéis anuais por tipo de usuário",
    "Mean rentals by recorded weather conditions":
        "Média de aluguéis por condição meteorológica",
    "Daily rentals by day of the week":
        "Aluguéis diários por dia da semana",
    "Pairwise Pearson correlations":
        "Correlações de Pearson entre variáveis",
    "Expanding-window cross-validation · lower RMSE is better":
        "Validação cruzada com janela crescente · menor RMSE é melhor",
    "Chronological holdout · observed vs estimated":
        "Teste cronológico · observado versus estimado",
    "Holdout residuals · observed − estimated":
        "Resíduos do teste · observado − estimado",
    "Random forest feature importance · illustrative model":
        "Importância das variáveis · floresta aleatória ilustrativa",
    "Mean recorded rentals by hour and rider type":
        "Média de aluguéis por hora e tipo de usuário",
    "Hour × weekday: mean recorded demand":
        "Hora × dia da semana: demanda média registrada",
    "Working vs non-working day hourly patterns":
        "Padrões horários em dias úteis e não úteis",
    "Hourly models: expanding-window CV RMSE":
        "Modelos horários: RMSE da validação com janela crescente",
    "Hourly chronological holdout: observed vs estimated":
        "Teste cronológico horário: observado versus estimado",
    "Hourly holdout: mean absolute error by hour":
        "Teste horário: erro absoluto médio por hora",

    # Axes and units
    "Rentals per day": "Aluguéis por dia",
    "Mean daily rentals": "Média diária de aluguéis",
    "Recorded rentals": "Aluguéis registrados",
    "Daily rentals": "Aluguéis diários",
    "RMSE (rentals / day)": "RMSE (aluguéis/dia)",
    "Impurity-based importance": "Importância baseada na impureza",
    "Mean rentals per recorded hour":
        "Média de aluguéis por hora registrada",
    "Hour of day": "Hora do dia",
    "Day of week": "Dia da semana",
    "Mean rentals": "Média de aluguéis",
    "Mean recorded rentals": "Média de aluguéis registrados",
    "RMSE · rentals per recorded hour":
        "RMSE · aluguéis por hora registrada",
    "Rentals per hour": "Aluguéis por hora",
    "MAE · rentals/hour": "MAE · aluguéis/hora",

    # Legends and controls
    "All rentals": "Todos os aluguéis",
    "All riders": "Todos os usuários",
    "Registered": "Registrados",
    "Casual": "Ocasionais",
    "Observed": "Observado",
    "Estimated": "Estimado",
    "Working day": "Dia útil",
    "Non-working day": "Dia não útil",
    "All": "Tudo",
    "3m": "3m",
    "6m": "6m",

    # Weather categories
    "Clear / partly cloudy": "Claro / parcialmente nublado",
    "Mist / cloudy": "Neblina / nublado",
    "Light rain / snow": "Chuva leve / neve",
    "Severe weather": "Condições severas",

    # Months
    "Jan": "Jan", "Feb": "Fev", "Mar": "Mar",
    "Apr": "Abr", "May": "Mai", "Jun": "Jun",
    "Jul": "Jul", "Aug": "Ago", "Sep": "Set",
    "Oct": "Out", "Nov": "Nov", "Dec": "Dez",

    # Weekdays
    "Sun": "Dom", "Mon": "Seg", "Tue": "Ter",
    "Wed": "Qua", "Thu": "Qui", "Fri": "Sex",
    "Sat": "Sáb",
    "Sunday": "Domingo",
    "Monday": "Segunda-feira",
    "Tuesday": "Terça-feira",
    "Wednesday": "Quarta-feira",
    "Thursday": "Quinta-feira",
    "Friday": "Sexta-feira",
    "Saturday": "Sábado",

    # Model labels
    "Random forest": "Floresta aleatória",
    "Random Forest": "Floresta aleatória",
    "Linear regression": "Regressão linear",
    "Linear Regression": "Regressão linear",
    "Polynomial ridge (degree 2)": "Ridge polinomial (grau 2)",
    "Decision tree": "Árvore de decisão",
    "Decision Tree": "Árvore de decisão",
    "Gradient boosting": "Gradient boosting",

    # Hover templates
    "Mean rentals:": "Média de aluguéis:",
    "Mean:": "Média:",
    "Days:": "Dias:",
    "Mean CV RMSE:": "RMSE médio da validação:",
    "Residual:": "Resíduo:",
    "Importance:": "Importância:",
    "mean rentals": "aluguéis em média",
    "mean CV RMSE": "RMSE médio da validação",
    "rentals/hour": "aluguéis/hora",
}


def _plotly_translation_spec(fig, plot_id):
    """Generate presentation-only bilingual updates."""

    def translate(value):
        return PLOTLY_TRANSLATIONS.get(value, value)

    def translate_hover(value):
        if not isinstance(value, str):
            return value
        import re
        keys = sorted(PLOTLY_TRANSLATIONS, key=len, reverse=True)
        # Preserve Plotly placeholders and HTML tags.
        parts = re.split(r"(%\{[^}]+\}|<[^>]+>)", value)
        for i in range(0, len(parts), 2):
            part = parts[i]
            pattern = "|".join(
                re.escape(key) for key in keys
            )
            parts[i] = re.sub(
                pattern,
                lambda m: PLOTLY_TRANSLATIONS[m.group(0)],
                part
            )
        return "".join(parts)

    layout_en = {"separators": ".,"}
    layout_pt = {"separators": ",."}

    def add_layout(key, value):
        if isinstance(value, str) and value:
            translated = translate(value)
            if translated != value:
                layout_en[key] = value
                layout_pt[key] = translated

    layout = fig.layout.to_plotly_json()

    add_layout(
        "title.text",
        layout.get("title", {}).get("text")
    )

    for axis_name, axis in layout.items():
        if not axis_name.startswith(("xaxis", "yaxis")):
            continue
        if not isinstance(axis, dict):
            continue

        add_layout(
            axis_name + ".title.text",
            axis.get("title", {}).get("text")
        )

        for i, button in enumerate(
            axis.get("rangeselector", {}).get("buttons", [])
        ):
            add_layout(
                f"{axis_name}.rangeselector.buttons[{i}].label",
                button.get("label")
            )

    for i, menu in enumerate(layout.get("updatemenus", [])):
        for j, button in enumerate(menu.get("buttons", [])):
            add_layout(
                f"updatemenus[{i}].buttons[{j}].label",
                button.get("label")
            )

    traces_en = []
    traces_pt = []

    for i, trace in enumerate(fig.data):
        item = trace.to_plotly_json()

        update_en = {}
        update_pt = {}

        name = item.get("name")

        if isinstance(name, str) and translate(name) != name:
            update_en["name"] = name
            update_pt["name"] = translate(name)

        hover = item.get("hovertemplate")

        if isinstance(hover, str):
            translated = translate_hover(hover)

            if translated != hover:
                update_en["hovertemplate"] = hover
                update_pt["hovertemplate"] = translated

        colorbar = item.get("colorbar", {})
        title = colorbar.get("title", {}).get("text")

        if isinstance(title, str) and translate(title) != title:
            update_en["colorbar.title.text"] = title
            update_pt["colorbar.title.text"] = translate(title)

        if update_en:
            traces_en.append({"index": i, "update": update_en})
            traces_pt.append({"index": i, "update": update_pt})

    # Translate categorical tick labels without modifying category data.
    for dimension in ("x", "y"):
        categories = []

        for trace in fig.data:
            values = getattr(trace, dimension, None)

            if values is None:
                continue

            for value in values:
                if isinstance(value, str) and value not in categories:
                    categories.append(value)

        if categories and any(
            translate(value) != value for value in categories
        ):
            axis = dimension + "axis"

            for destination, localized in (
                (layout_en, categories),
                (layout_pt, [translate(v) for v in categories])
            ):
                destination[axis + ".tickmode"] = "array"
                destination[axis + ".tickvals"] = categories
                destination[axis + ".ticktext"] = localized

    heading = layout.get("title", {}).get("text") or ""

    # Titles are presented outside the Plotly canvas.
    layout_en.pop("title.text", None)
    layout_pt.pop("title.text", None)

    return {
        "id": plot_id,
        "locales": {
            "en": {
                "heading": heading,
                "layout": layout_en,
                "traces": traces_en
            },
            "pt-BR": {
                "heading": translate(heading),
                "layout": layout_pt,
                "traces": traces_pt
            }
        }
    }


def _plotly_translation_html(fig, plot_id):
    specification = _plotly_translation_spec(fig, plot_id)
    payload = json.dumps(
        specification, ensure_ascii=False
    ).replace("<", "\\u003c")

    return (
        '<script type="application/json" data-ep-plotly-i18n>'
        + payload
        + '</script>'
    )


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

    # EP_HOURLY_REPORT_EXTENSION_V1: validated hourly artifacts from the same notebook.
    hour_path = project_root / "datasets" / "hour.csv"
    hour_metrics_path = project_root / "outputs" / "hourly" / "metrics.json"
    hour_models_path = project_root / "outputs" / "hourly" / "tables" / "hourly_model_comparison.csv"
    hour_preds_path = project_root / "outputs" / "hourly" / "tables" / "hourly_holdout_predictions.csv"
    for artifact in (hour_path, hour_metrics_path, hour_models_path, hour_preds_path):
        if not artifact.is_file():
            raise FileNotFoundError(f"Missing hourly notebook export: {artifact}")

    hours = pd.read_csv(hour_path, parse_dates=["dteday"])
    hour_metrics = json.loads(hour_metrics_path.read_text(encoding="utf-8"))
    hour_models = pd.read_csv(hour_models_path).sort_values("cv_mean_rmse")
    hour_preds = pd.read_csv(hour_preds_path, parse_dates=["date"])
    needed = {"dteday", "hr", "weekday", "workingday", "cnt", "casual", "registered"}
    if not needed.issubset(hours.columns):
        raise ValueError("Hourly dataset schema mismatch")
    if len(hours) != int(hour_metrics["hourly_rows"]):
        raise ValueError("Hourly metrics record count does not match hour.csv")
    if len(hour_preds) != int(hour_metrics["holdout_rows"]):
        raise ValueError("Hourly predictions record count mismatch")
    if not (hours["casual"] + hours["registered"]).eq(hours["cnt"]).all():
        raise ValueError("Hourly rental component totals do not add up")
    if int(hours["cnt"].sum()) != int(daily["cnt"].sum()):
        raise ValueError("Daily and hourly rental totals do not match")
    if hours.duplicated(subset=["dteday", "hr"]).any():
        raise ValueError("Duplicate date-hour rows")
    if hour_models.empty or hour_preds.empty:
        raise ValueError("Hourly model results are empty")
    if not {"date", "hour", "observed_rentals", "estimated_rentals"}.issubset(hour_preds.columns):
        raise ValueError("Unexpected hourly prediction columns")
    if hour_metrics["model"] not in set(hour_models["model"]):
        raise ValueError("Selected hourly model is absent from CV comparison")


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

    # EP_HOURLY_REPORT_CHARTS: six interactive views, populated from notebook outputs.
    hourly_segments = hours.groupby("hr")[["cnt", "registered", "casual"]].mean().reindex(range(24))
    hourly_profile = go.Figure()
    for label, field, color in (("All riders", "cnt", COLORS["aqua"]),
                                ("Registered", "registered", COLORS["blue"]),
                                ("Casual", "casual", COLORS["orange"])):
        hourly_profile.add_trace(go.Scatter(
            x=list(range(24)), y=hourly_segments[field], mode="lines+markers",
            name=label, line=dict(color=color, width=2.6)))
    _layout(hourly_profile, "Mean recorded rentals by hour and rider type", "Mean rentals per recorded hour", height=400)
    hourly_profile.update_xaxes(title="Hour of day", dtick=2, range=[0, 23])

    hour_weekdays = hours.groupby(["weekday", "hr"])["cnt"].mean().unstack("hr")
    hour_weekdays = hour_weekdays.reindex(index=range(7), columns=range(24))
    weekday_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    hourly_heatmap = go.Figure(go.Heatmap(
        x=list(range(24)), y=weekday_names, z=hour_weekdays.to_numpy(),
        colorscale="YlOrBr", colorbar=dict(title="Mean rentals"),
        hovertemplate="%{y}, %{x}:00 — %{z:.1f} mean rentals<extra></extra>"))
    _layout(hourly_heatmap, "Hour × weekday: mean recorded demand", height=450)
    hourly_heatmap.update_xaxes(title="Hour of day", dtick=2)
    hourly_heatmap.update_yaxes(autorange="reversed", title="Day of week")

    workday_hours = hours.groupby(["workingday", "hr"])["cnt"].mean().unstack(0).reindex(range(24))
    hourly_workday = go.Figure()
    for flag, label, color in ((1, "Working day", COLORS["aqua"]),
                                (0, "Non-working day", COLORS["orange"])):
        hourly_workday.add_trace(go.Scatter(
            x=list(range(24)), y=workday_hours[flag], name=label,
            mode="lines+markers", line=dict(color=color, width=2.5)))
    _layout(hourly_workday, "Working vs non-working day hourly patterns", "Mean recorded rentals", height=400)
    hourly_workday.update_xaxes(title="Hour of day", dtick=2)

    hour_cv_chart = go.Figure(go.Bar(
        x=hour_models["cv_mean_rmse"], y=hour_models["model"], orientation="h",
        marker_color=COLORS["aqua"],
        error_x=dict(type="data", array=hour_models["cv_std_rmse"], visible=True),
        hovertemplate="%{y}: mean CV RMSE %{x:.1f} rentals/hour<extra></extra>"))
    _layout(hour_cv_chart, "Hourly models: expanding-window CV RMSE", "", height=350)
    hour_cv_chart.update_xaxes(title="RMSE · rentals per recorded hour")
    hour_cv_chart.update_yaxes(autorange="reversed")
    hour_cv_chart.update_layout(margin=dict(l=205, r=30, t=80, b=62))

    hour_preds = hour_preds.sort_values(["date", "hour"]).copy()
    hour_preds["timestamp"] = hour_preds["date"] + pd.to_timedelta(hour_preds["hour"], unit="h")
    hour_holdout_chart = go.Figure()
    for label, field, color in (("Observed", "observed_rentals", COLORS["aqua"]),
                                ("Estimated", "estimated_rentals", COLORS["orange"])):
        hour_holdout_chart.add_trace(go.Scatter(
            x=hour_preds["timestamp"], y=hour_preds[field], name=label,
            mode="lines", line=dict(color=color, width=1.3)))
    _layout(hour_holdout_chart, "Hourly chronological holdout: observed vs estimated", "Rentals per hour", height=440)
    hour_holdout_chart.update_layout(
        margin=dict(l=65, r=25, t=125, b=85),
        title=dict(
            x=0.02,
            xanchor="left",
            y=0.98,
            yanchor="top"
        ),
        legend=dict(
            orientation="h",
            x=0,
            y=1.04,
            yanchor="bottom",
            xanchor="left"
        )
    )
    hour_holdout_chart.update_xaxes(rangeslider_visible=True)

    hour_errors = hour_preds.assign(abs_error=(hour_preds["observed_rentals"] - hour_preds["estimated_rentals"]).abs())
    hour_errors = hour_errors.groupby("hour", as_index=False)["abs_error"].mean()
    hour_error_chart = go.Figure(go.Bar(
        x=hour_errors["hour"], y=hour_errors["abs_error"], marker_color=COLORS["orange"],
        hovertemplate="%{x}:00 — MAE %{y:.1f}<extra></extra>"))
    _layout(hour_error_chart, "Hourly holdout: mean absolute error by hour", "MAE · rentals/hour", height=350)
    hour_error_chart.update_xaxes(title="Hour of day", dtick=2)

    plots = {
        "plot-hourly-profile": hourly_profile,
        "plot-hourly-heatmap": hourly_heatmap,
        "plot-hourly-workday": hourly_workday,
        "plot-hourly-cv": hour_cv_chart,
        "plot-hourly-holdout": hour_holdout_chart,
        "plot-hourly-errors": hour_error_chart,
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
    chart_divs = {}

    for key, figure in plots.items():
        heading = figure.layout.title.text or ""
        translation = _plotly_translation_html(figure, key)

        if heading:
            heading_html = (
                f'<h3 class="ep-chart-heading" id="{key}-heading">'
                f'{escape(heading)}</h3>'
            )
        else:
            heading_html = ""

        # The demand chart already has its external title.
        figure.update_layout(title=None)

        if key != "plot-demand":
            has_legend = (
                len(figure.data) > 1
                and figure.layout.showlegend is not False
            )

            if has_legend:
                figure.update_layout(
                    margin=dict(t=65),
                    legend=dict(
                        orientation="h",
                        x=0,
                        xanchor="left",
                        y=1.04,
                        yanchor="bottom"
                    )
                )
            else:
                figure.update_layout(margin=dict(t=28))

        chart_divs[key] = (
            heading_html
            + _figure_html(figure, key)
            + translation
        )
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
    # Business notes are calculated from validated raw hourly records, never hard-coded.
    business_hour_path = project_root / "datasets" / "hour.csv"
    business_hourly_metrics_path = project_root / "outputs" / "hourly" / "metrics.json"
    if not business_hour_path.is_file() or not business_hourly_metrics_path.is_file():
        raise FileNotFoundError("Both hourly raw data and validated metrics are required")
    business_hourly_data = pd.read_csv(business_hour_path)
    business_hourly_metrics = json.loads(business_hourly_metrics_path.read_text(encoding="utf-8"))
    business_hourly_avg = business_hourly_data.groupby("hr")["cnt"].mean()
    business_peak_hour = int(business_hourly_avg.idxmax())
    business_year1 = int(metrics["data"]["annual_totals"]["2011"])
    business_year2 = int(metrics["data"]["annual_totals"]["2012"])
    # Use annual per-day averages (365 days in 2011, 366 days in 2012).
    business_growth = 100 * ((business_year2 / 366) / (business_year1 / 365) - 1)
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
        "business_peak": f"{business_peak_hour:02d}:00–{(business_peak_hour+1) % 24:02d}:00",
        "business_peak_mean": f"{float(business_hourly_avg.loc[business_peak_hour]):,.1f}",
        "business_growth": f"{business_growth:.1f}",
        "business_hour_r2": f"{float(business_hourly_metrics['holdout_r2']):.3f}",
        "business_daily_r2": f"{float(test['r2']):.3f}",
        "hourly_rows": f"{len(hours):,}",
        "hourly_model": escape(str(hour_metrics["model"])),
        "hourly_cv_rmse": _safe_float(hour_metrics["cv_mean_rmse"]),
        "hourly_rmse": _safe_float(hour_metrics["holdout_rmse"]),
        "hourly_mae": _safe_float(hour_metrics["holdout_mae"]),
        "hourly_r2": f"{float(hour_metrics['holdout_r2']):.3f}",
        "hourly_incomplete_days": str(int(hour_metrics["incomplete_days"])),
        "hourly_missing_hours": str(int(hour_metrics["missing_recorded_clock_hours"])),
        "hourly_holdout_start": hour_preds["date"].min().strftime("%Y-%m-%d"),
        "hourly_holdout_end": hour_preds["date"].max().strftime("%Y-%m-%d"),
        **{key.replace("-", "_"): val for key, val in chart_divs.items()},
    }

    ep_footer_html, _ = render_footer()
    ep_logo_src = logo_data_uri()
    data.update(ep_footer_html=ep_footer_html, ep_logo_src=ep_logo_src, ep_references_html=render_references(BIKE_REFERENCES), ep_outputs_html=render_outputs(BIKE_OUTPUTS))
    data["ep_project_links_html"] = render_project_links('https://github.com/eduardojr-pereira/data-science-portfolio/tree/main/selected_projects/bike_sharing')
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
  a{color:var(--aqua);text-underline-offset:3px}a:hover{color:var(--ep-color-link-hover)}
  .container{width:min(1180px,calc(100% - 36px));margin:auto}
  /* Bike Sharing controls layout only; EP Brand controls link styling. */
  .bike-local-nav{position:sticky;top:0;z-index:20;background:var(--ep-color-bg);border-bottom:1px solid var(--ep-color-border)}
  .bike-local-nav__inner{min-height:64px;display:flex;align-items:center;padding:12px 0}
  .bike-local-nav__links{display:flex;align-items:center;flex-wrap:wrap;gap:10px;width:100%}
  .bike-local-nav__back{margin-left:auto}
  @media(max-width:670px){.bike-local-nav__links{gap:6px}}
  @media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
  main{padding:25px 0 80px}main section{margin:36px 0 56px}.section-heading{margin:0 0 8px;font-size:1.55rem;letter-spacing:-.02em}
  .hint{color:var(--muted);font-size:.9rem;margin:0 0 19px;max-width:950px}.cards{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
  .stat,.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:18px;min-width:0}
  .stat small{color:var(--muted);display:block;font-size:.8rem}.stat strong{font-size:1.7rem;letter-spacing:-.03em;display:block;margin-top:4px}
  .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:15px}.chart{background:var(--card);border:1px solid var(--border);border-radius:15px;padding:10px;min-width:0;overflow:hidden}
  .chart.full{grid-column:1/-1}.chart > .plotly-graph-div{width:100%!important}
  .chart-heading{font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;font-size:1.07rem;font-weight:700;letter-spacing:-.015em;line-height:1.35;color:var(--text);margin:10px 12px 3px}
  .chart-subheading{font-size:.83rem;color:var(--muted);margin:0 12px 4px}
  .chart--demand .plotly-graph-div{margin-top:2px}
  .callout{border-left:4px solid var(--ep-color-accent);background:var(--ep-color-surface);padding:16px 19px;border-radius:0 10px 10px 0;color:var(--ep-color-text)}
  .callout strong{color:var(--ep-color-accent)}p{margin-top:8px}.card h3{margin:0 0 9px;font-size:1.1rem}.card p{color:var(--ep-color-muted)}.metric{font-size:1.35rem;font-weight:800;color:var(--ep-color-text)}
  .caption{font-size:.82rem;color:var(--muted);padding:6px 4px 0}



  footer:not(.ep-footer){border-top:1px solid var(--border);text-align:center;padding:34px 16px 48px;color:var(--muted);font-size:.85rem}footer:not(.ep-footer) img{width:72px;height:auto}
  .sr-only{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
  @media(max-width:850px){.cards{grid-template-columns:repeat(2,minmax(0,1fr))}}
  @media(max-width:670px){.grid{grid-template-columns:1fr}.chart.full{grid-column:auto}.stat strong{font-size:1.4rem}}

  </style>
  <script>$plotly_js</script>
</head>
<body>
  <nav class="bike-local-nav ep-report-nav" aria-label="Report sections">
    <div class="container bike-local-nav__inner">
      <div class="bike-local-nav__links">
        <a class="ep-report-nav__link" href="#overview" data-i18n-en="Overview" data-i18n-pt="Visão geral">Overview</a>
        <a class="ep-report-nav__link" href="#business" data-i18n-en="Business" data-i18n-pt="Negócios">Business</a>
        <a class="ep-report-nav__link" href="#exploration" data-i18n-en="Exploration" data-i18n-pt="Exploração">Exploration</a>
        <a class="ep-report-nav__link" href="#hourly" data-i18n-en="Hourly" data-i18n-pt="Análise horária">Hourly</a>
        <a class="ep-report-nav__link" href="#models" data-i18n-en="Models" data-i18n-pt="Modelos">Models</a>
        <a class="ep-report-nav__link" href="#findings" data-i18n-en="Conclusions" data-i18n-pt="Conclusões">Conclusions</a>
        <a class="ep-report-nav__link" href="#outputs" data-i18n-en="Outputs" data-i18n-pt="Resultados">Outputs</a>
        <a class="ep-report-nav__link" href="#references" data-i18n-en="References" data-i18n-pt="Referências">References</a>
        <a class="ep-report-nav__back bike-local-nav__back" href="../../../index.html" aria-label="Back to Portfolio" data-replace="Back to Portfolio"><span>Back to Portfolio</span></a>
      </div>
    </div>
  </nav>
  <div id="top" class="hero ep-project-intro"><div class="ep-project-intro__inner">
    <div class="eyebrow">Technical report · Regression analysis</div>
    <h1>Bike Sharing Demand Analysis</h1>
    <p class="lead">Explore daily and hourly demand patterns from Washington, D.C. (2011–2012), compare regression models through chronological validation, and examine the limitations of retrospective demand estimation.</p>
    <div class="tags"><span class="tag">Python</span><span class="tag">Pandas</span><span class="tag">scikit-learn</span><span class="tag">Plotly</span><span class="tag">Time-series CV</span></div>
    $ep_project_links_html
  </div></div>
  <main class="container">
    <section id="overview"><h2 class="section-heading">Dataset overview</h2>
      <p class="hint">The UCI dataset contains daily and hourly bike rental totals and weather-related variables. These figures are historical observations, not forecasts.</p>
      <div class="cards"><div class="stat"><small>Daily observations</small><strong>$rows</strong></div><div class="stat"><small>Total rentals</small><strong>$rentals</strong></div><div class="stat"><small>Development days</small><strong>$development</strong></div><div class="stat"><small>Holdout days</small><strong>$holdout_days</strong></div></div>
      <div class="grid" style="margin-top:15px"><div class="card"><h3>2011</h3><span class="metric">$year1</span><p>Total recorded rentals</p></div>
      <div class="card"><h3>2012</h3><span class="metric">$year2</span><p>Total recorded rentals</p></div></div>
    </section>
    <section id="business"><h2 class="section-heading">Business questions & operational insights</h2>
      <p class="hint">A historical system-level demand study: where might the operator investigate staffing, bicycle availability or rebalancing windows? These are planning hypotheses, not measured cost savings or station-level prescriptions.</p>
      <div class="grid">
        <div class="card"><h3>Most active clock hour</h3><div class="metric">$business_peak</div><p>Average <strong>$business_peak_mean rentals</strong> per recorded observation at this hour, over 2011–2012. Missing clock-hour records are not imputed as zero.</p></div>
        <div class="card"><h3>Demand growth</h3><div class="metric">+$business_growth%</div><p>Change in mean daily rentals from 2011 to 2012. It does not establish the causes of growth or a future growth rate.</p></div>
        <div class="card"><h3>Operational questions</h3><p>Compare registered and casual hourly patterns, workdays and non-workdays, and peak windows before planning inventory coverage. Station-level supply data are required to design actual rebalancing routes.</p></div>
        <div class="card"><h3>Evidence, not a production forecast</h3><p>Historical hourly holdout R²: <strong>$business_hour_r2</strong>; daily holdout R²: <strong>$business_daily_r2</strong>. These models use observed contemporaneous weather; deployment requires available-at-prediction-time inputs and independent evaluation.</p></div>
      </div>
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
    <!-- EP_HOURLY_SECTION_START -->
    <section id="hourly"><h2 class="section-heading">Hourly patterns &amp; validation</h2>
      <p class="hint">The hourly UCI records cover the same 2011–2012 Capital Bikeshare rentals as the daily dataset, shown at a finer aggregation level. These are not additional rentals.</p>
      <div class="cards">
        <div class="stat"><small>Recorded hourly observations</small><strong>$hourly_rows</strong></div>
        <div class="stat"><small>Selected hourly candidate</small><strong style="font-size:1.2rem">$hourly_model</strong></div>
        <div class="stat"><small>Hourly CV RMSE</small><strong>$hourly_cv_rmse</strong></div>
        <div class="stat"><small>Hourly holdout R²</small><strong>$hourly_r2</strong></div>
      </div>
      <div class="grid" style="margin-top:18px">
        <div class="chart full">$plot_hourly_profile</div>
        <div class="chart full">$plot_hourly_heatmap</div>
        <div class="chart full">$plot_hourly_workday</div>
        <div class="chart full">$plot_hourly_cv</div>
        <div class="card"><h3>Hourly chronological holdout</h3><div class="metric">RMSE $hourly_rmse</div>
          <p>MAE <strong>$hourly_mae</strong> rentals/hour · R² <strong>$hourly_r2</strong></p>
          <p>$hourly_holdout_start to $hourly_holdout_end</p></div>
        <div class="card"><h3>Data completeness</h3><div class="metric">$hourly_incomplete_days days</div>
          <p>The source has <strong>$hourly_missing_hours</strong> unrecorded clock hours across those days. The absent hours were not artificially imputed.</p></div>
        <div class="chart full">$plot_hourly_holdout</div>
        <div class="chart full">$plot_hourly_errors</div>
      </div>
      <div class="callout" style="margin-top:16px"><strong>How to interpret:</strong>
        Hourly and daily RMSE/MAE are measured in different units and should not be compared numerically.
        Both models are retrospective conditional estimates using observed weather at the target date/hour,
        not proven advance forecasts. The daily model's negative holdout R² is reported transparently.
        An earlier iteration already examined the holdout; this evaluation is not an untouched external benchmark.</div>
      <p class="hint" style="margin-top:14px">Operational questions: How do commute peaks differ from leisure use? Which hours would be important to examine for bicycle rebalancing and staffing? These associations are descriptive and do not prove that a specific intervention would increase demand.</p>
    </section>
    <!-- EP_HOURLY_SECTION_END -->
    <section id="models"><h2 class="section-heading">Daily model evaluation</h2>
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
    $ep_outputs_html
    $ep_references_html
  </main>
  $ep_footer_html
  <script>
  (() => {
    // EP-NAV-CLICK-LOCK-V1: one active section during smooth scrolling.
    const links = [...document.querySelectorAll('.bike-local-nav__links a[href^="#"]')];
    const sections = links.map(link => document.getElementById(link.hash.slice(1)));
    let lockedTarget = null;
    let unlockTimer = null;

    function markActive(id) {
      links.forEach(link => {
        const active = Boolean(id && link.hash === '#' + id);
        link.classList.toggle('is-active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }

    function updateActiveSection() {
      if (lockedTarget) return;
      const threshold = 125;
      let current = null;
      sections.forEach(section => {
        if (section && section.getBoundingClientRect().top <= threshold) current = section.id;
      });
      // At document top, prefer the first section rather than leaving no selection.
      if (!current && sections[0]) current = sections[0].id;
      markActive(current);
    }

    function releaseNavigationLock() {
      if (!lockedTarget) return;
      lockedTarget = null;
      if (unlockTimer !== null) window.clearTimeout(unlockTimer);
      unlockTimer = null;
      updateActiveSection();
    }

    links.forEach(link => link.addEventListener('click', () => {
      // Keep native anchor navigation and smooth scrolling intact.
      const target = link.hash.slice(1);
      if (!document.getElementById(target)) return;
      lockedTarget = target;
      markActive(target);
      if (unlockTimer !== null) window.clearTimeout(unlockTimer);
      // Fallback for browsers without scrollend; no persistent stale selection.
      unlockTimer = window.setTimeout(releaseNavigationLock, 1800);
    }));

    window.addEventListener('scroll', updateActiveSection, {passive: true});
    window.addEventListener('resize', updateActiveSection);
    window.addEventListener('hashchange', updateActiveSection);
    // Supported in current Chrome; ends the click lock when the scroll finishes.
    window.addEventListener('scrollend', releaseNavigationLock, {passive: true});
    // A new manual scroll interrupts programmatic navigation.
    window.addEventListener('wheel', releaseNavigationLock, {passive: true});
    window.addEventListener('touchstart', releaseNavigationLock, {passive: true});
    updateActiveSection();
  })();
  </script>
</body></html>''')
    html = template.safe_substitute(data)
    html = html.replace(
        "</body>",
        "<script>\n" + BIKE_REPORT_TRANSLATIONS
        + "\n</script>\n</body>",
        1
    )
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
