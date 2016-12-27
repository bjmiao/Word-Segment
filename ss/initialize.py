import re

def token_sentence(text):
    '''return a list, each element is a sentence'''
    text=re.sub(r'([，。？！：；])',r'|\1|',text)
    text=re.sub(r'[　 \t\n]+','|',text)
    if '||' in text: text=text.replace('||','|')
    sentence_list=text.split('|')
    
    if ('\n' in sentence_list):sentence_list.remove('\n')
    if ('' in sentence_list):sentence_list.remove('')
    return sentence_list

def remove_num_and_punc(sentence):
    word_str=re.sub(r'([0-9a-zA-Z]+|[“‘”’{}、【】《》——（）])',r'|\1|',sentence)
    word_list=word_str.split('|')
    while ('' in word_list): word_list.remove('')
    return(word_list)
            
def init(text):
    '''return a list, each element is a list of words(with tokened num and punc)'''
    sentence_list=token_sentence(text)
    for i in range(len(sentence_list)):
        sentence_list[i]=remove_num_and_punc(sentence_list[i])
    return sentence_list
    
