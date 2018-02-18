# usr/bin/env python
#-*- coding:utf-8 -*-
import gzip,json
def Extraction(country):
    for line in gzip.open('jawiki-country.json.gz','rt'):
        data_json = json.loads(line)
        if data_json['title'] == country:
            return data_json['text']
