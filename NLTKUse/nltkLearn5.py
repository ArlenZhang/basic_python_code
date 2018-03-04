'''
    学习class StanfordNeuralDependencyParser(GenericStanfordParser)类的使用，找寻句子词语之间的依赖关系，找到名词短语 动词短语中的中心词
There, judges who saw few such cases and had no experience in the field grappled with some of the most technical and complex disputes imaginable.
'''
s="There, judges who saw few such cases and had no experience in the field grappled with some of the most technical and complex disputes imaginable."
from nltk.parse.stanford import StanfordDependencyParser
parser=StanfordDependencyParser(path_to_models_jar="/home/arlenzhang/stanford/parser/stanford-parser-3.6.0-models.jar")
from nltk.tokenize.stanford import StanfordTokenizer
tokenizer=StanfordTokenizer()
from nltk.parse.stanford import StanfordParser
ps=StanfordParser(path_to_models_jar="/home/arlenzhang/stanford/parser/stanford-parser-3.6.0-models.jar")
s="to channel investments."
list(ps.parse(tokenizer.tokenize(s)))[0].draw()
parse_result=parser.parse(tokenizer.tokenize(s))
print("================parse_result==================")
print(parse_result)
print("================parse_result[0]==================")
list_result=list(parser.parse(tokenizer.tokenize(s)))
print(list_result)
print("================result==================")
result=list_result[0]
print(result)
#s='There, judges who saw few such cases and had no experience in the field grappled with some of the most technical and complex disputes imaginable.'
'''
    上面的数据是一个字典，包含所有的单词和关系。
'''
print("=================actual===================")
length = 3
for i in range(1,4):
    print(result.get_by_address(i)["rel"])
