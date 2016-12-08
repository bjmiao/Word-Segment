from ss import fmm
import dictionary
# -*- coding: utf-8 -*-

start=int(input("start:"))
stop=int(input("stop:"))
for i in range(start,stop+1):
    f=open('corpus/'+repr(i)+'.txt','r',encoding='UTF-8')
    url=f.readline()#Remove the URL in head
    s1=f.read()
    print(s1)
    dic=dictionary.getdict()
    
    result_str=fmm.fmm(s1,dic)
