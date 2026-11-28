"""Responsibility: Verify every prepared chart against the original Bike Sharing exports and canonical chart contract.
Boundaries: No source modification, training, page rendering or browser acceptance.
"""
import argparse
import json
import math
from pathlib import Path
import sys
import unittest

import numpy as np
import pandas as pd
import plotly.graph_objects as go


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--prepared', type=Path, required=True)
    parser.add_argument('--brand', type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.brand.resolve() / 'tools'))
    from plotly_presentation import chart_payload
    root, prepared = args.project, args.prepared
    specs = {p.stem: json.loads(p.read_text(encoding='utf-8')) for p in (prepared/'content/charts').glob('*.json')}
    messages = json.loads((prepared/'translations.json').read_text(encoding='utf-8'))
    d = pd.read_csv(root/'datasets/day.csv').sort_values('dteday')
    h = pd.read_csv(root/'datasets/hour.csv')
    p = pd.read_csv(root/'outputs/tables/holdout_predictions.csv').sort_values('date')
    hp = pd.read_csv(root/'outputs/hourly/tables/hourly_holdout_predictions.csv').sort_values(['date','hour'])
    m = pd.read_csv(root/'outputs/tables/model_comparison.csv').sort_values('cv_mean_rmse')
    hm = pd.read_csv(root/'outputs/hourly/tables/hourly_model_comparison.csv').sort_values('cv_mean_rmse')
    imp = pd.read_csv(root/'outputs/tables/random_forest_feature_importance.csv').sort_values('importance',ascending=False).head(12)
    dm=json.loads((root/'outputs/metrics.json').read_text())
    hrm=json.loads((root/'outputs/hourly/metrics.json').read_text())
    def close(a,b):
        np.testing.assert_allclose(a,b,rtol=1e-12,atol=1e-10)
    def data(ident): return specs['plot-'+ident]['figure']['data']
    class Checks(unittest.TestCase):
        def test_contract(self):
            self.assertEqual(len(specs),16)
            self.assertEqual(set(messages['en']),set(messages['pt-BR']))
            for ident,spec in specs.items():
                with self.subTest(chart=ident):
                    chart_payload(ident,local=messages,**spec)
                    go.Figure(spec['figure'])
        def test_demand(self):
            for t,col in zip(data('demand'),['cnt','registered','casual'],strict=True):
                self.assertEqual(t['x'],d.dteday.tolist());close(t['y'],d[col])
            layout=specs['plot-demand']['figure']['layout']
            self.assertEqual([t['visible'] for t in data('demand')],[True,False,False])
            self.assertEqual([b['args'][0]['visible'] for b in layout['updatemenus'][0]['buttons']],[[True,False,False],[False,True,False],[False,False,True]])
            self.assertTrue(layout['xaxis']['rangeslider']['visible'])
        def test_seasonality(self):
            for year,t in zip([2011,2012],data('seasonality'),strict=True):
                rows=d[d.dteday.str.startswith(str(year))]
                close(t['y'],[rows[rows.mnth==month].cnt.mean() for month in range(1,13)])
        def test_composition(self):
            for col,t in zip(['registered','casual'],data('composition'),strict=True):
                close(t['y'],[d[d.dteday.str.startswith(str(y))][col].sum() for y in [2011,2012]])
        def test_weather(self):
            t=data('weather')[0]
            for i,code in enumerate(t['x']):
                rows=d[d.weathersit==code];close(t['y'][i],rows.cnt.mean());self.assertEqual(t['customdata'][i][0],len(rows))
        def test_weekday(self):
            t=data('weekday')[0]
            for i,code in enumerate(t['x']):
                rows=d[d.weekday==code];close(t['y'][i],rows.cnt.mean());self.assertEqual(t['customdata'][i][0],len(rows))
        def test_correlation(self):
            t=data('corr')[0];close(t['z'],np.corrcoef(d[t['x']].to_numpy().T));self.assertEqual(t['x'],t['y'])
        def check_cv(self,ident,frame):
            t=data(ident)[0];self.assertEqual(t['y'],frame.model.tolist());close(t['x'],frame.cv_mean_rmse);close(t['error_x']['array'],frame.cv_std_rmse)
        def test_daily_cv(self): self.check_cv('cv',m)
        def test_hourly_cv(self): self.check_cv('hourly-cv',hm)
        def check_holdout(self,ident,frame,timestamps):
            for col,t in zip(['observed_rentals','estimated_rentals'],data(ident),strict=True):
                close(t['y'],frame[col]);self.assertEqual(t['x'],timestamps)
        def test_holdout(self): self.check_holdout('holdout',p,p.date.tolist())
        def test_residuals(self): close(data('residuals')[0]['y'],p.observed_rentals-p.estimated_rentals)
        def test_importance(self):
            t=data('importance')[0];self.assertEqual(t['y'],imp.feature.tolist());close(t['x'],imp.importance)
        def test_hourly_profile(self):
            for t,col in zip(data('hourly-profile'),['cnt','registered','casual'],strict=True):close(t['y'],[h[h.hr==n][col].mean() for n in range(24)])
        def test_heatmap(self): close(data('hourly-heatmap')[0]['z'],[[h[(h.weekday==day)&(h.hr==hour)].cnt.mean() for hour in range(24)] for day in range(7)])
        def test_workday(self):
            for t,flag in zip(data('hourly-workday'),[1,0],strict=True):close(t['y'],[h[(h.workingday==flag)&(h.hr==hour)].cnt.mean() for hour in range(24)])
        def test_hourly_holdout(self): self.check_holdout('hourly-holdout',hp,[f'{date}T{hour:02d}:00:00' for date,hour in zip(hp.date,hp.hour,strict=True)])
        def test_hourly_errors(self):
            expected=[]
            for hour in range(24):
                rows=hp[hp.hour==hour];expected.append((rows.observed_rentals-rows.estimated_rentals).abs().mean())
            close(data('hourly-errors')[0]['y'],expected)
        def test_metrics(self):
            for frame,expected in [(p,dm['validation']['holdout']),(hp,{'rmse':hrm['holdout_rmse'],'mae':hrm['holdout_mae'],'r2':hrm['holdout_r2']})]:
                y=frame.observed_rentals.to_numpy();err=y-frame.estimated_rentals.to_numpy()
                actual={'rmse':math.sqrt(np.mean(err**2)),'mae':np.mean(abs(err)),'r2':1-np.sum(err**2)/np.sum((y-y.mean())**2)}
                for key,value in actual.items():self.assertAlmostEqual(value,expected[key],delta=0.001)
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    if not result.wasSuccessful(): raise SystemExit(1)

if __name__=='__main__': main()
