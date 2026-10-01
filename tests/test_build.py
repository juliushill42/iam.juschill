#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'dist'; req=['index.html','identity.json','identity.jsonld','timeline.json','evidence.json','domains.json','llms.txt','llms-full.txt','robots.txt','sitemap.xml','.well-known/julius-cameron-hill.json']
missing=[x for x in req if not (D/x).exists()]; assert not missing, missing
identity=json.loads((D/'identity.json').read_text()); timeline=json.loads((D/'timeline.json').read_text()); domains=json.loads((D/'domains.json').read_text())
assert identity['name']=='Julius Cameron Hill'; assert identity['canonical_url']=='https://iam.movingwithclarity.com'; assert len(timeline)>=6; assert len(domains)>=20
body=(D/'index.html').read_text()
for n in ['Julius Cameron Hill',"A man can't rewrite history",'The IAM Mesh','Machine endpoints']: assert n in body,n
print(f'PASS: {len(req)} endpoints, {len(domains)} domains, {len(timeline)} timeline entries')
