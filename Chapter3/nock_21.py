# 記事中でカテゴリ名を宣言している行を抽出せよ．

# usr/bin/env python
#-*- coding:utf-8 -*-

from extraction_country import Extraction
lines=Extraction("イギリス").split('\n')
# li=[line for line in lines if "Category" in line]
for line in lines:
    if "Category" in line:
        print(line)
