"""Responsibility: Prepare the Bike Sharing report's 16 declarative Plotly specifications and chart translations from audited exports.
Boundaries: No model fitting, notebook execution, HTML rendering, shared UI, publication or writes to source datasets/outputs.
"""
import argparse
import json
import re
from pathlib import Path

import pandas as pd

PALETTE = 'ep-muted-pastel'


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + '\n', encoding='utf-8')


def prepare(root):
    """Return chart specs and locale dictionaries; preserve source identifiers and numerical values."""
    def csv(path, **kwargs):
        return pd.read_csv(root / path, **kwargs)
    def read(path):
        return json.loads((root / path).read_text(encoding='utf-8'))
    d = csv('datasets/day.csv', parse_dates=['dteday']).sort_values('dteday')
    h = csv('datasets/hour.csv', parse_dates=['dteday'])
    p = csv('outputs/tables/holdout_predictions.csv', parse_dates=['date']).sort_values('date')
    hp = csv('outputs/hourly/tables/hourly_holdout_predictions.csv', parse_dates=['date']).sort_values(['date','hour'])
    m = csv('outputs/tables/model_comparison.csv').sort_values('cv_mean_rmse')
    hm = csv('outputs/hourly/tables/hourly_model_comparison.csv').sort_values('cv_mean_rmse')
    imp = csv('outputs/tables/random_forest_feature_importance.csv').sort_values('importance', ascending=False).head(12)
    dm, hrm = read('outputs/metrics.json'), read('outputs/hourly/metrics.json')
    def require(condition, message):
        if not condition:
            raise ValueError(message)
    require(len(d)==dm['data']['records'] and len(h)==hrm['hourly_rows'], 'Source row count mismatch')
    require(not d.dteday.duplicated().any() and not h.duplicated(['dteday','hr']).any(), 'Duplicate observations')
    for frame in (d,h):
        require((frame.casual+frame.registered).eq(frame.cnt).all(), 'Rider counts do not reconcile')
    require(d.set_index('dteday')[['cnt','casual','registered']].equals(h.groupby('dteday')[['cnt','casual','registered']].sum()), 'Daily/hourly mismatch')
    require(int(d.cnt.sum())==dm['data']['total_rentals'], 'Rental total mismatch')
    require(len(p)==dm['methodology']['holdout_size'] and len(hp)==hrm['holdout_rows'], 'Holdout count mismatch')
    require(not p.date.duplicated().any() and not hp.duplicated(['date','hour']).any(), 'Duplicate predictions')
    require(p.set_index('date').observed_rentals.eq(d.set_index('dteday').cnt.reindex(p.date)).all(), 'Daily observed predictions mismatch')
    require(hp.set_index(['date','hour']).observed_rentals.eq(h.set_index(['dteday','hr']).cnt.reindex(hp.set_index(['date','hour']).index)).all(), 'Hourly observed predictions mismatch')
    selected=dm['validation']['selected_model']
    require(m.iloc[0].model==selected and hm.iloc[0].model==hrm['model'], 'Selected model differs from CV minimum')
    translations={'en':{}, 'pt-BR':{}}
    specs={}
    def msg(key, en, pt):
        key='content.bike.chart.'+key
        for locale,value in [('en',en),('pt-BR',pt)]:
            if key in translations[locale] and translations[locale][key]!=value:
                raise ValueError('Conflicting message: '+key)
            translations[locale][key]=value
        return key
    def val(key): return translations['en'][key]
    def dates(series, hourly=False): return series.dt.strftime('%Y-%m-%dT%H:%M:%S' if hourly else '%Y-%m-%d').tolist()
    def chart(ident, title, axis=None, *, height=370, xaxis=None):
        key=msg(ident+'.title',*title)
        layout={'height':height,'autosize':True,'title':{'text':val(key)},'margin':{'l':65,'r':24,'t':75,'b':65}}
        spec={'figure':{'data':[],'layout':layout},'translations':{'layout':{'title.text':key},'traces':[]},'colors':[],'palette':PALETTE,'config':{'responsive':True,'displaylogo':False}}
        specs['plot-'+ident]=spec
        if axis: axis_title(spec,'yaxis',axis)
        if xaxis: axis_title(spec,'xaxis',xaxis)
        return spec
    def axis_title(s, axis, pair):
        key=msg('axis.'+re.sub(r'[^a-z0-9]+', '_', pair[0].lower()).strip('_'),*pair)
        s['figure']['layout'].setdefault(axis,{})['title']={'text':val(key)}
        s['translations']['layout'][axis+'.title.text']=key
    def ticks(s,axis,values,keys):
        s['figure']['layout'].setdefault(axis,{}).update(tickmode='array',tickvals=list(values),ticktext=[val(k) for k in keys])
        s['translations']['layout'][axis+'.ticktext']=keys
    def trace(s,data,*,name=None,hover=None,text=None,color=None,path='marker.color'):
        i=len(s['figure']['data']); fields={}
        if name: data['name']=val(name);fields['name']=name
        if hover: data['hovertemplate']=val(hover);fields['hovertemplate']=hover
        if text: data['text']=[val(k) for k in text];fields['text']=text
        s['figure']['data'].append(data)
        if fields: s['translations']['traces'].append({'index':i,'fields':fields})
        if color is not None: s['colors'].append({'trace':i,'path':path,'palette':PALETTE,'index':color})
    def continuous(s,palette): s['colors'].append({'trace':0,'path':'colorscale','palette':palette})
    daily=('Rentals per day','Aluguéis por dia'); mean_daily=('Mean daily rentals','Média diária de aluguéis'); hourly=('Rentals per hour','Aluguéis por hora'); hour_axis=('Hour of day','Hora do dia'); mean_hour=('Mean rentals per recorded hour','Média de aluguéis por hora registrada')
    all_r=msg('series.all','All rentals','Todos os aluguéis'); reg=msg('series.registered','Registered','Cadastrados'); casual=msg('series.casual','Casual','Casuais'); observed=msg('series.observed','Observed','Observado'); estimated=msg('series.estimated','Estimated','Estimado')
    day_names=[('Sun','Dom'),('Mon','Seg'),('Tue','Ter'),('Wed','Qua'),('Thu','Qui'),('Fri','Sex'),('Sat','Sáb')]
    full_days=[('Sunday','Domingo'),('Monday','Segunda-feira'),('Tuesday','Terça-feira'),('Wednesday','Quarta-feira'),('Thursday','Quinta-feira'),('Friday','Sexta-feira'),('Saturday','Sábado')]
    day_keys=[msg('weekday.'+str(i),*pair) for i,pair in enumerate(day_names)]
    full_keys=[msg('weekday.full.'+str(i),*pair) for i,pair in enumerate(full_days)]
    month_names=[('Jan','Jan'),('Feb','Fev'),('Mar','Mar'),('Apr','Abr'),('May','Mai'),('Jun','Jun'),('Jul','Jul'),('Aug','Ago'),('Sep','Set'),('Oct','Out'),('Nov','Nov'),('Dec','Dez')]
    month_keys=[msg('month.'+str(i),*pair) for i,pair in enumerate(month_names,1)]
    rental_hover=msg('hover.rentals','%{x}<br>Rentals: %{y:,.0f}<extra></extra>','%{x}<br>Aluguéis: %{y:,.0f}<extra></extra>')
    category_hover=msg('hover.category','%{text}<br>Mean rentals: %{y:,.1f}<extra></extra>','%{text}<br>Média de aluguéis: %{y:,.1f}<extra></extra>')
    count_hover=msg('hover.count','%{text}<br>Mean rentals: %{y:,.1f}<br>Days: %{customdata[0]:.0f}<extra></extra>','%{text}<br>Média de aluguéis: %{y:,.1f}<br>Dias: %{customdata[0]:.0f}<extra></extra>')
    s=chart('demand',('Daily rental demand','Demanda diária de aluguéis'),daily,height=420)
    for i,(col,key) in enumerate([('cnt',all_r),('registered',reg),('casual',casual)]):
        trace(s,{'type':'scatter','x':dates(d.dteday),'y':d[col].tolist(),'mode':'lines','visible':i==0,'line':{'width':1.65}},name=key,color=i,path='line.color')
    l=s['figure']['layout']; l.pop('title'); s['translations']['layout'].pop('title.text');l['margin']['t']=95
    keys=[all_r,reg,casual];l['updatemenus']=[{'buttons':[{'label':val(k),'method':'update','args':[{'visible':[j==i for j in range(3)]}]} for i,k in enumerate(keys)],'direction':'down','x':.99,'xanchor':'right','y':1.15,'yanchor':'top','showactive':True}]
    for i,k in enumerate(keys):s['translations']['layout'][f'updatemenus[0].buttons[{i}].label']=k
    ranges=[msg('range.3m','3m','3m'),msg('range.6m','6m','6m'),msg('range.all','All','Tudo')]
    l['xaxis']={'type':'date','rangeslider':{'visible':True},'rangeselector':{'x':0,'y':1.15,'buttons':[{'count':3,'label':val(ranges[0]),'step':'month','stepmode':'backward'},{'count':6,'label':val(ranges[1]),'step':'month','stepmode':'backward'},{'step':'all','label':val(ranges[2])}]}}
    for i,k in enumerate(ranges):s['translations']['layout'][f'xaxis.rangeselector.buttons[{i}].label']=k
    d=d.assign(year=d.dteday.dt.year,month=d.dteday.dt.month)
    monthly=d.groupby(['year','month']).cnt.mean()
    s=chart('seasonality',('Average daily rentals by month and year','Média diária de aluguéis por mês e ano'),mean_daily)
    for i,year in enumerate((2011,2012)):
        a=monthly.loc[year];trace(s,{'type':'scatter','x':a.index.tolist(),'y':a.tolist(),'mode':'lines+markers','name':str(year),'line':{'width':3,'dash':['solid','dash'][i]}},text=[month_keys[n-1] for n in a.index],hover=category_hover,color=[1,0][i],path='line.color')
    ticks(s,'xaxis',range(1,13),month_keys)
    s=chart('composition',('Annual rentals by rider type','Aluguéis anuais por tipo de usuário'),('Recorded rentals','Aluguéis registrados'))
    for col,key,i in [('registered',reg,1),('casual',casual,2)]:
        a=d.groupby('year')[col].sum();trace(s,{'type':'bar','x':a.index.astype(str).tolist(),'y':a.tolist()},name=key,color=i)
    s['figure']['layout']['barmode']='stack'
    s=chart('weather',('Mean rentals by recorded weather conditions','Média de aluguéis por condição meteorológica registrada'),daily)
    weather=d.groupby('weathersit').cnt.agg(['mean','count']);weather_names={1:('Clear / partly cloudy','Céu limpo / parcialmente nublado'),2:('Mist / cloudy','Neblina / nublado'),3:('Light rain / snow','Chuva leve / neve'),4:('Severe weather','Tempo severo')};keys=[msg('weather.'+str(i),*weather_names[i]) for i in weather.index]
    trace(s,{'type':'bar','x':weather.index.tolist(),'y':weather['mean'].tolist(),'customdata':weather[['count']].values.tolist()},text=keys,hover=count_hover,color=0);ticks(s,'xaxis',weather.index,keys)
    s=chart('weekday',('Daily rentals by day of the week','Aluguéis diários por dia da semana'),mean_daily)
    a=d.groupby('weekday').cnt.agg(['mean','count']).reindex(range(7));trace(s,{'type':'bar','x':list(range(7)),'y':a['mean'].tolist(),'customdata':a[['count']].values.tolist()},text=day_keys,hover=count_hover,color=2);ticks(s,'xaxis',range(7),day_keys)
    s=chart('corr',('Pairwise Pearson correlations','Correlações de Pearson entre pares'),height=440)
    c=d[['cnt','temp','atemp','hum','windspeed','casual','registered']].corr();trace(s,{'type':'heatmap','x':c.columns.tolist(),'y':c.columns.tolist(),'z':c.values.tolist(),'zmin':-1,'zmax':1,'text':c.round(2).values.tolist(),'texttemplate':'%{text}','hovertemplate':'%{x} / %{y}: %{z:.2f}<extra></extra>'});continuous(s,'vik')
    model_names={'Polynomial ridge (degree 2)':'Ridge polinomial (grau 2)','Ridge regression':'Regressão Ridge','Decision tree':'Árvore de decisão','Random forest':'Floresta aleatória','SVR':'SVR','Linear regression':'Regressão linear','Median baseline':'Baseline da mediana','Histogram gradient boosting':'Gradient boosting por histogramas','Ridge':'Ridge'}
    def model_chart(ident,frame,title,axis,height,highlight=None):
        s=chart(ident,title,height=height,xaxis=axis);keys=[msg('model.'+str(list(model_names).index(n)),n,model_names[n]) for n in frame.model]
        hover=msg(ident+'.hover','%{text}<br>Mean CV RMSE: %{x:,.1f}<extra></extra>','%{text}<br>RMSE médio na CV: %{x:,.1f}<extra></extra>')
        trace(s,{'type':'bar','y':frame.model.tolist(),'x':frame.cv_mean_rmse.tolist(),'orientation':'h','error_x':{'type':'data','array':frame.cv_std_rmse.tolist(),'visible':True}},text=keys,hover=hover,color=[0 if n==highlight else 1 for n in frame.model] if highlight else 0)
        ticks(s,'yaxis',frame.model,keys);s['figure']['layout']['yaxis']['autorange']='reversed';s['figure']['layout']['margin']['l']=205
    model_chart('cv',m,('Expanding-window cross-validation · lower RMSE is better','Validação cruzada com janela expansiva · menor RMSE é melhor'),('RMSE (rentals / day)','RMSE (aluguéis / dia)'),460,selected)
    def holdout(ident,frame,x,axis,title,height):
        s=chart(ident,title,axis,height=height)
        for key,col,i in [(observed,'observed_rentals',0),(estimated,'estimated_rentals',2)]:
            trace(s,{'type':'scatter','x':x,'y':frame[col].tolist(),'mode':'lines','line':{'width':2 if ident=='holdout' else 1.3,'dash':'solid' if i==0 else 'dash'}},name=key,color=i,path='line.color')
        s['figure']['layout']['xaxis']={'type':'date','rangeslider':{'visible':True}}
    holdout('holdout',p,dates(p.date),daily,('Chronological holdout · observed vs estimated','Holdout cronológico · observado versus estimado'),370)
    s=chart('residuals',('Holdout residuals · observed − estimated','Resíduos no holdout · observado − estimado'),daily)
    a=p.observed_rentals-p.estimated_rentals;hover=msg('residuals.hover','%{x|%Y-%m-%d}<br>Residual: %{y:,.1f}<extra></extra>','%{x|%Y-%m-%d}<br>Resíduo: %{y:,.1f}<extra></extra>');trace(s,{'type':'bar','x':dates(p.date),'y':a.tolist()},hover=hover,color=[4 if n>0 else 3 for n in a]);s['figure']['layout']['shapes']=[{'type':'line','xref':'paper','x0':0,'x1':1,'y0':0,'y1':0,'line':{'dash':'dash'}}]
    s=chart('importance',('Random forest feature importance · illustrative model','Importância das variáveis na floresta aleatória · modelo ilustrativo'),height=430,xaxis=('Impurity-based importance','Importância por impureza'));hover=msg('importance.hover','%{y}<br>Importance: %{x:.3f}<extra></extra>','%{y}<br>Importância: %{x:.3f}<extra></extra>');trace(s,{'type':'bar','y':imp.feature.tolist(),'x':imp.importance.tolist(),'orientation':'h'},hover=hover,color=1);s['figure']['layout']['yaxis']={'autorange':'reversed'};s['figure']['layout']['margin']['l']=205
    s=chart('hourly-profile',('Mean recorded rentals by hour and rider type','Média de aluguéis registrados por hora e tipo de usuário'),mean_hour,height=400,xaxis=hour_axis)
    a=h.groupby('hr')[['cnt','registered','casual']].mean().reindex(range(24))
    for i,(col,key) in enumerate([('cnt',all_r),('registered',reg),('casual',casual)]):trace(s,{'type':'scatter','x':list(range(24)),'y':a[col].tolist(),'mode':'lines+markers','line':{'width':2.6,'dash':['solid','dash','dot'][i]}},name=key,color=i,path='line.color')
    s['figure']['layout']['xaxis'].update(dtick=2,range=[0,23])
    s=chart('hourly-heatmap',('Hour × weekday: mean recorded demand','Hora × dia da semana: demanda média registrada'),height=450,xaxis=hour_axis,axis=('Day of week','Dia da semana'))
    a=h.groupby(['weekday','hr']).cnt.mean().unstack('hr').reindex(index=range(7),columns=range(24));hover=msg('heatmap.hover','Day code (0=Sun): %{y}<br>%{x}:00 — %{z:.1f} mean rentals<extra></extra>','Código do dia (0=dom): %{y}<br>%{x}:00 — %{z:.1f} aluguéis em média<extra></extra>');bar=msg('heatmap.colorbar','Mean rentals','Média de aluguéis');trace(s,{'type':'heatmap','x':list(range(24)),'y':list(range(7)),'z':a.values.tolist(),'colorbar':{'title':{'text':val(bar)}}},hover=hover);s['translations']['traces'][0]['fields']['colorbar.title.text']=bar;continuous(s,'nuuk');ticks(s,'yaxis',range(7),full_keys);s['figure']['layout']['yaxis']['autorange']='reversed';s['figure']['layout']['xaxis']['dtick']=2
    s=chart('hourly-workday',('Working vs non-working day hourly patterns','Padrões horários em dias úteis e não úteis'),('Mean recorded rentals','Média de aluguéis registrados'),height=400,xaxis=hour_axis);a=h.groupby(['workingday','hr']).cnt.mean().unstack(0).reindex(range(24))
    for flag,pair,i in [(1,('Working day','Dia útil'),0),(0,('Non-working day','Dia não útil'),2)]:trace(s,{'type':'scatter','x':list(range(24)),'y':a[flag].tolist(),'mode':'lines+markers','line':{'width':2.5,'dash':'solid' if flag else 'dash'}},name=msg('workday.'+str(flag),*pair),color=i,path='line.color')
    s['figure']['layout']['xaxis']['dtick']=2
    model_chart('hourly-cv',hm,('Hourly models: expanding-window CV RMSE','Modelos horários: RMSE na CV com janela expansiva'),('RMSE · rentals per recorded hour','RMSE · aluguéis por hora registrada'),350)
    holdout('hourly-holdout',hp,dates(hp.date+pd.to_timedelta(hp.hour,unit='h'),True),hourly,('Hourly chronological holdout: observed vs estimated','Holdout cronológico horário: observado versus estimado'),440)
    s=chart('hourly-errors',('Hourly holdout: mean absolute error by hour','Holdout horário: erro absoluto médio por hora'),('MAE · rentals/hour','MAE · aluguéis/hora'),height=350,xaxis=hour_axis);a=hp.assign(abs_error=(hp.observed_rentals-hp.estimated_rentals).abs()).groupby('hour').abs_error.mean();hover=msg('hourly-errors.hover','%{x}:00 — MAE %{y:.1f}<extra></extra>','%{x}:00 — MAE %{y:.1f}<extra></extra>');trace(s,{'type':'bar','x':a.index.tolist(),'y':a.tolist()},hover=hover,color=2);s['figure']['layout']['xaxis']['dtick']=2
    require(len(specs)==16,'Unexpected chart count')
    for ident in specs:
        title_key='content.bike.chart.'+ident.removeprefix('plot-')+'.title'
        require(title_key in translations['en'],'Missing chart title')
    return specs,translations


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--output', type=Path,required=True,help='New external candidate directory; never the source project')
    args=parser.parse_args();root=args.project.resolve(strict=True);out=args.output.resolve()
    if out.exists() or root==out or root in out.parents:
        raise SystemExit('Output must be a new directory outside the source project')
    specs,messages=prepare(root)
    (out/'content/charts').mkdir(parents=True)
    for ident,spec in specs.items():write_json(out/'content/charts'/f'{ident}.json',spec)
    write_json(out/'translations.json',messages)
    print(f'Prepared {len(specs)} specifications and {len(messages["en"])} bilingual message keys; source files unchanged')

if __name__=='__main__':
    main()
