cols=['a','b','c']
res_cols=[1,2,3,4,5,6,7]
li=[]
mapping = {'surface': cols[0],'base': res_cols[6],'pos': res_cols[0],'pos1': res_cols[1]}
li.append(mapping)
mapping = {'surface': cols[1],'base': res_cols[5],'pos': res_cols[1],'pos1': res_cols[2]}
li.append(mapping)
print(li)
