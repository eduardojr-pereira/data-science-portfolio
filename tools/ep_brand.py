"""EP web component renderer, synchronized from sibling ep-brand-assets snapshot."""
from pathlib import Path
import base64
import datetime
import json
import mimetypes
import os
import re

ROOT = Path(os.environ.get('EP_BRAND_ASSETS_ROOT', Path(__file__).resolve().parents[1] / 'vendor/ep-brand-assets'))

def _values():
    brand=json.loads((ROOT/'config/brand.json').read_text(encoding='utf-8'))
    values=dict(brand)
    for key, rel in {'logo_src':'logos/logo_initials.png', 'gmail_src':'icons/gmail_icon.svg', 'linkedin_src':'icons/linkedin_icon.svg'}.items():
        payload=(ROOT/'assets'/rel).read_bytes()
        mime=mimetypes.guess_type(rel)[0] or 'application/octet-stream'
        values[key]=f'data:{mime};base64,'+base64.b64encode(payload).decode('ascii')
    values['year']=str(datetime.date.today().year)
    return values

def _sub(template, values):
    def replace(m):
        k=m.group(1)
        if k not in values:raise ValueError('Unknown EP placeholder: '+k)
        return str(values[k])
    result=re.sub(r'\{\{([a-z_]+)\}\}',replace,template)
    if '{{' in result or '}}' in result:raise ValueError('Unresolved EP placeholders')
    return result

def logo_data_uri():
    return _values()['logo_src']

def render_footer():
    values=_values()
    html=_sub((ROOT/'components/web/footer.html').read_text(encoding='utf-8'),values)
    css_paths = [
        ROOT / 'styles' / 'colors.css',
        ROOT / 'styles' / 'typography.css',
        ROOT / 'styles' / 'layout.css',
        ROOT / 'components/web/footer.css',
    ]
    css = '\n'.join(
        path.read_text(encoding='utf-8').rstrip()
        for path in css_paths
    ) + '\n'
    return html,css
