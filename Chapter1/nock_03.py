# -*- coding: utf-8 -*-
sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
sentence_change = (sentence.replace(',',' ')).replace('.',' ')
array = []
x = sentence_change.split(' ')
for i in range(len(x)):
    if(x[i] == ''):
        continue
    else:
        array.append(len(x[i]))
print(array)
