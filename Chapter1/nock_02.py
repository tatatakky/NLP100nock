# -*- coding: utf-8 -*-
pat = 'パトカー'
taxi = 'タクシー'
c = []
for i in range(4):
    if(i%2==0):
        c.append(pat[i])
        c.append(taxi[i])
    else:
        c.append(pat[i])
        c.append(taxi[i])
print(''.join(c))
