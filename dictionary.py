import string
punctuation=string.punctuation
chnpunctuation='，。、？！……：；“‘”’{}【】——（）'


def getdict():
	ver_file=open('./dict/latest.log','r')
	ver=ver_file.readline()
	ver.replace('\n','')

	dict_file=open('./dict/'+ver,'r')
	dict=[]
	while True:
		line=dict_file.readline()
		if (line==''): break
		dict.append(getline(line))

	return dict

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

def splitwords(text):
        text=text.replace('｜','|')
        if(text[0]!='|'):text='|'+text
        if(text[-1]!='|'):text=text+'|'
        text_list=list(text)

        char_list=[]
        for i in range(len(text_list)):
                char=text_list[i]
                if ((char in punctuation)and not(char=='|')):pass
                elif ((char=='\n')or(char==' ')or(char=='\t')):pass
                elif (char in chnpunctuation):pass
                else:char_list.append(char)
        print(char_list)
        text=''.join(char_list)
        print(text)
        print(type(text))
        #Remove punctuation
        word_list=text.split('|')
        word_num=len(word_list)-2
        
        word_list[0],word_list[-1]=None,None
        print(word_list)
        input()

text='''领。导。，？！人｜杭州｜峰会|的|
贵宾|的|到。来。|。新华社|记者|兰|红光|摄'''

splitwords(text)














