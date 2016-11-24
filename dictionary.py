import string
punctuation=string.punctuation
chnpunctuation='，。、？！……：；“‘”’{}【】《》——（）'


def getdict():
        def getline(line):
                w={}
                #{'Word': ,'Num': ,'Pre':[dict] , 'Suf':[dict] }

                def list_word(line):
                        fix={}
                        list=line.split(',')
                        for ele in list:
                                pair=ele.split(':')
                                fix[pair[0]]=int(pair[1])
                        return fix

                index=line.find('|Word|')
                w['Word']=line[:index]
                line=line[index+len('|Word|'): ]

                index=line.find('|Num|')
                w['Num']=int(line[:index])
                line=line[index+len('|Num|'): ]

                index=line.find('|Pre|')
                w['Pre']=list_word(line[:index])
                line=line[index+len('|Pre|'): ]

                index=line.find('|Suf|')
                w['Suf']=list_word(line[:index])
                line=line[index+len('|Suf|'): ]

                return w
        
        ver_file=open('./dict/latest.log','r')
        ver=ver_file.readline()
        ver=ver.replace('\n','')

        dic_file=open('./dict/'+ver,'r')
        dic=[]
        while True:
                line=dic_file.readline()
                if (line==''): break
                dic.append(getline(line))

        return dic



def splitwords(text):
        text=text.replace('｜','|')
        if(text[0]!='|'):text='|'+text
        if(text[-1]!='|'):text=text+'|'
        text_list=list(text)

        char_list=[]
        for i in range(len(text_list)):
                char=text_list[i]
                if ((char in punctuation)and not(char=='|')):char_list.append('|')
                elif ((char=='\n')or(char==' ')or(char=='\t')):pass
                elif (char in chnpunctuation):char_list.append('|')
                else:char_list.append(char)

        text=''.join(char_list)
        while ('||' in text):text=text.replace('||','|')

        #Remove punctuation
        word_seq=text.split('|')
        word_num=len(word_seq)-2
        
        word_seq[0],word_seq[-1]=None,None

        #word_seq is the sequence of textwords
        return(word_seq)

def add_to_dict(dic,word_seq):
        def search(word,dic):
                for i in range(len(dic)):
                        if (dic[i]['Word']==word):return i

                return -1

        def insert(fix,word):
                #dic is {'的': 1},{'是':1}
                fix[word]=fix.get(word,0)+1
                return fix

        #{'Word': ,'Num': ,'Pre':[dict] , 'Suf':[dict] }
        
        for i in range(len(word_seq)):
                if (word_seq[i]==None) : continue
                index=search(word_seq[i],dic)
                if (index>=0):
                        temp=dic[index]
                        temp['Num']+=1
                        temp['Pre']=insert(temp['Pre'],word_seq[i-1])
                        temp['Suf']=insert(temp['Suf'],word_seq[i+1])
                        dic[index]=temp
                else:
                        d={}
                        d['Word']=word_seq[i]
                        d['Num']=1
                        d['Pre']={word_seq[i-1]:1}
                        d['Suf']={word_seq[i+1]:1}
                        dic.append(d)
   ##     dic.sort()

        for entry in dic:
                print(entry)

        

text='''早上|好！上|个|月，二十|国|集团|领导人|第|十一|次|峰会|在|杭州|
圆满|落幕|。在|世界|经济|增长|和|二十|国|集团|转型|的|关键|节点，杭州|
峰会|承载|了|各方|高度|期待|。各|成员国|、嘉宾|国|领导人|和|国际|组织|负
责人|围绕|构建|创新|、活力|、联动|、包容|的|世界|经济|的|峰会|主题|，就
|加强|政策|协调|、创新|增长|方式|，更|高效|的|全球|经济|金融|治理，|强
劲|的|国际|贸易|和|投资|，包容|和|联动|式|发展|等|议题|深入|交换|意见|，共
同|探讨|影响|世界|经济|的|其他|重大|全球|性|挑战|，达成|了|广泛|共识|。
《二十|国|集团|领导人|杭州|峰会|公报》集中|体现|了|着眼|长远|、综合|施|
策|、开放|创新|、包容|发展|的|杭州|共识|，进一步|明确|了|二十|国|集团|
合作|的|发展|方向|、目标|和|举措|。杭州|峰会|以|历史|的|担当|、
战略|的|眼光|，开启|了|世界|经济|增长|和|二十|国|集团|合作|的|新|进程|。'''
dic=getdict()
word_seq=splitwords(text)
add_to_dict(dic,word_seq)













