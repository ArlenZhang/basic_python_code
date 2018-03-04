'''
测试stanford coreNLP使用
nltk stanford tagger
'''
#1. tokenizer
s='Three seats currently are vacant and three others are likely to be filled within a few years, so patent lawyers and research-based industries are making a new push for specialists to be added to the court.'
from nltk.tokenize.stanford import StanfordTokenizer
eng_tokenizer=StanfordTokenizer()
tokens=eng_tokenizer.tokenize(s)
print(tokens)
#2. tagger
from nltk.tag.stanford import StanfordPOSTagger
    #下面没有修改源代码，因为StanforgTagger下面的由两个子类，jar包检索在父类
eng_tagger=StanfordPOSTagger(model_filename='english-bidirectional-distsim.tagger',path_to_jar="/home/arlenzhang/stanford/postagger/stanford-postagger.jar")
taggedList=eng_tagger.tag(tokens)
print(taggedList)

import nltk
taggedList=nltk.pos_tag(s.split())
print(taggedList)
#发现用nltk词性标注存在一些缺点，比如brown stanford标注的更靠谱,所以在做词性标注的时候采用斯坦福的

#3. parser
from nltk.parse.stanford import StanfordParser
eng_parser = StanfordParser(path_to_models_jar="/home/arlenzhang/stanford/parser/stanford-parser-3.6.0-models.jar")
tree = eng_parser.parse(s.split())
treeList=list(tree)[0]
# print(treeList)
treeList[0].draw()

#对stanford_parser结果单独理解