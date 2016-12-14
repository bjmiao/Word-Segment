from ss import fmm
import dictionary
# -*- coding: utf-8 -*-

def use_fmm(s1,dic,url,index):    
    result_str=fmm.fmm(s1,dic)

    f=open('corpus/'+repr(index)+'-fmm.txt','w',encoding='UTF-8')
    f.write(url)
    f.write(result_str)

    f.close()

start=int(input("start:"))
stop=int(input("stop:"))
for i in range(start,stop+1):
    f=open('corpus/'+repr(i)+'.txt','r',encoding='UTF-8')
    url=f.readline()#Remove the URL in head
    s1=f.read()
    f.close()    
    dic,url_list=dictionary.getdict()

    use_fmm(s1,dic,url,i)
