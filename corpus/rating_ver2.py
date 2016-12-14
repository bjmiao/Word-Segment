#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-
# Name:        模块2
# Purpose:
#
# Author:      li
#
# Created:     12/12/2016
# Copyright:   (c) li 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def rating(raw_infilename,std_infilename):
    import re
    raw_infile=open(raw_infilename,'r',encoding='UTF-8')
    std_infile=open(std_infilename,'r',encoding='UTF-8')
    (fa,fb)=('','')
    for line in raw_infile:
        fa+=''.join(re.split(r'[\s\n]*',line))
    for line in std_infile:
        fb+=''.join(re.split(r'[\s\n]*',line))

    def line_rate(fa,fb):
        grade=100
        for i in range(0,len(fa)-1):
            (str1,str2)=(fa[i],fb[i])
            if str1!=str2:
                grade=grade-1
                if str1=='｜'and str2!='｜':
                    fb=fb[:i]+'｜'+fb[i:]
                elif str1!="｜"and str2=='｜':
                    fb=fb[:i]+fb[i+1:]
                else:
                    pass
                    #print(str1,str2)
        return grade

    grade=line_rate(fa,fb)
    print('grade:',grade)
    return grade

rating('1-fmm.txt','1-std.txt')

