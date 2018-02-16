# usr/bin/env python
#-*- coding:utf-8 -*-
# cut -f 1 hightemp.txt | sort | uniq -c | sort -r
col1 = [line.split('\t')[0] for line in open('hightemp.txt','r')]
dictionary={prefecture:col1.count(prefecture) for prefecture in col1}
sort=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)
for name,count in sort:
    print(count,name)
