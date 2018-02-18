# 記事中でカテゴリ名を宣言している行を抽出せよ．

# usr/bin/env python
#-*- coding:utf-8 -*-

from extraction_country import Extraction
lines=Extraction("イギリス").split('\n')
print(lines)
