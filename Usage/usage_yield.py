# usr/bin/env python
#-*- coding:utf-8 -*-
import time
def yield_func():
    a=1
    b=2
    c=a+b
    yield c
    yield 10*c
    yield 100*c

start = time.time()
for func in yield_func():
    print(func)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
# print("------Not use [for loop]------")
start = time.time()
gen = yield_func()
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
