'''
解决完基本问题，下面就是关于词性的向上探索过程，当前词性的上层节点中心词（针对短语）的判断，最上层由中心词的节点是否存在
右兄弟节点，存在则给出当前词性组，否则下降，直到词性层面。
'''
from nltk.tokenize.stanford import StanfordTokenizer
from nltk import Tree
from nltk.parse.bllip import BllipParser
from nltk.data import find

s = "The bank also says it will use its network to channel investments."
tokenizer = StanfordTokenizer()
tokens = tokenizer.tokenize(s)
bllip_parser = BllipParser.from_unified_model_dir(find("models/bllip_wsj_no_aux").path)
bllip_tree = bllip_parser.parse(tokens)
parented_tree=bllip_parser.get_parented_tree(bllip_tree)

bllip_tree = bllip_parser.parse(tokens)
bllip_tree_list=list(bllip_tree)[0]

leaves = bllip_tree_list.leaves()
length = len(leaves)
#定义词性组数组
syntasic_arr=[1 for i in range(length)]

#定义动词集合和名词词性集合
none_set={"NN","NNS","NNP",'PRP','PRP$'} #代名词和所有格代名词
verb_set={"VBD","VBZ","VBP","VBN","VBG"}

def judgeType(label):
    print(none_set)

#其余的词性的单词都不可能是中心词，理解对么？
for leaf_index in range(length):
    tree_location = parented_tree.leaf_treeposition(leaf_index)
    temp_p_tree=parented_tree[tree_location[:-1]]#得到当前叶子节点的坐标
    #下面根据当前节点向上查找,我们对名词词性和动词词性的标签分组，对其他类型只关心词性，否则向上寻找句法结构
    resultType=judgeType(temp_p_tree.label())
    if resultType == "none" :
        flag=True #不停的向上遍历





