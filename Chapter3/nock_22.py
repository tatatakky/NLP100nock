# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
# usr/bin/env python
#-*- coding:utf-8 -*-
from extraction_country import Extraction
import re
lines=Extraction("イギリス").split('\n')
for line in lines:
    match = re.search("^\[\[Category:(.*?)(|\|.*)\]\]",line)
    if match is not None:
        print(match.group(1))
