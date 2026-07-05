#!/usr/bin/env python3
"""RUBRIC.md 채점용 표본 선정 (재현 가능): 카테고리당 중간 항목 1개."""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw=open(os.path.join(ROOT,"docs/js/gallery-data.js"),encoding="utf-8").read()
data=json.loads(raw[len("window.GALLERY_REFERENCES = "):].rstrip().rstrip(";"))
order=["웹툰","일러스트","게임","시네마틱","포스터","제품 · 브랜드","인물 사진","건물 사진","인포그래픽","UI·대시보드"]
by={}
for d in data: by.setdefault(d["category"],[]).append(d)
sample=[]
for c in order:
    items=by[c]; d=items[len(items)//2]
    sample.append({"id":d["id"],"category":c,"title":d["title"],
                   "image":d["image"].lstrip("./"),"metadata":d["metadata"],"prompt":d["prompt"]})
os.makedirs(os.path.join(ROOT,"experiments/_work"),exist_ok=True)
json.dump(sample,open(os.path.join(ROOT,"experiments/_work/sample.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("표본 10개 → experiments/_work/sample.json")
for s in sample: print(f'  {s["id"]:8} {s["category"]}')
