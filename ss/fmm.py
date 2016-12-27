#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      li
#
# Created:     24/11/2016
# Copyright:   (c) li 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-*-coding:GBK-*-GBK


#dic=[{'Word':'早上'},{'Word':'杭州','Num':5,'Pre':{'领导人':1,'在':1,'节点':1,'的':1,'举措':1},'Suf':{'峰会':3,'圆满':1,'共识':1}},{'Word':'领导人'},{'Word':'圆满'}]
#{'Word': ,'Num': ,'Pre':[dict] , 'Suf':[dict] }

s1='早上好！上个月，二十国集团领导人第十一次峰会在杭州圆满落幕。'

def match_sep(s1,dic):
    def wordList(dic):
        wordList=[]
        for element in dic:
            wordList.append(element['Word'])
        return wordList


    def find_maxlen(dic):
        maxLen=0
        for element in dic:
            if maxLen<len(element['Word']):
                maxLen=len(element['Word'])
        return maxLen
    wordList=wordList(dic)
    maxLen=find_maxlen(dic)

    s2=''
    w=s1[:maxLen]
    while s1!='':
        if w in wordList or len(w)==1:
            s2+=w+'|'
            s1=s1[len(w):]
            w=s1[:maxLen]
        else:
            w=w[:-1]
    return s2

def fmm(s1,dic):
    return match_sep(s1,dic)

