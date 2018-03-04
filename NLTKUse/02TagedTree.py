'''
对生文本的词性标注和树形结构输出，用stanford coreNLP
对RST训练库中数据
'''
from nltk.tokenize import StanfordTokenizer
from nltk import Tree

# fileObj=open("/home/arlenzhang/Desktop/语料/rst_discourse_treebank/data/RSTtrees-WSJ-main-1.0/TRAINING/wsj_2325.out","r")
# rawText=fileObj.read()
rawText="the quick brown fox jumps over the lazy dog"
#对英文进行分词
tokenizer=StanfordTokenizer()
tokens=tokenizer.tokenize(rawText)
print(tokens)
#对分词进行词性标注和句法结构构建
from nltk.parse.stanford import StanfordParser
eng_parser=StanfordParser("edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
treeList=eng_parser.parse(tokens)

#调用nltk的Tree对tree list 转换成树对象
from nltk import Tree
tree=treeList[0]#树元素即为所求
tree.draw()
