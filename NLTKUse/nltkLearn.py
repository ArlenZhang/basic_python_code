'''
    NLTK涉及的内容比较重要
    some simple things you can do with NLTK
'''
#tokenize and tag some text:
import nltk
stry="The oil industry's middling profits could persist through the rest of the year. "
tokens=nltk.word_tokenize(stry)
print(tokens)#将符号和单词和非单词部分分割成list存储

#词性标注,按照pennTreebank 词法标注
tagedToekns=nltk.pos_tag(tokens)
print(tagedToekns)

#实体识别
entities=nltk.chunk.ne_chunk(tagedToekns)
print(entities)
from nltk.corpus import treebank
t=treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()

#词性标注是否关系到句子？还是单独的词性？
s="She always troubles mother which makes many troubles."
tokens=nltk.word_tokenize(s)
tagedToekns=nltk.pos_tag(tokens)
print(tagedToekns) #结果表明有关系的