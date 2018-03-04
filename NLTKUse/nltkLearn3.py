'''
对 nltk中BllipParser的分析，这个树很重要，没有这个我的工作没法继续

'''

from nltk.parse.bllip import BllipParser
from nltk import ParentedTree
from nltk.tokenize.stanford import StanfordTokenizer
from nltk import Tree

s="The bank also says it will use its network to channel investments."
tokenizer=StanfordTokenizer()
tokens=tokenizer.tokenize(s)
from nltk.data import find
model_dir = find('models/bllip_wsj_no_aux').path
# the easiest way to get started is to use a unified model
bllip = BllipParser.from_unified_model_dir(model_dir)
bllip_tree = bllip.parse(tokens)

#怎么才能将bllip_tree的节点数据转变成字符串输出？
ptree=bllip.get_parented_tree(bllip_tree)

bllip_tree = bllip.parse(tokens)
print("========================================================")
tempTree=list(bllip_tree)[0]
leaf_values = tempTree.leaves()
print(leaf_values)

if 'bank' in leaf_values:
    leaf_index = leaf_values.index('it')
    print("叶子节点的数组下标定位：",leaf_index)
    tree_location = ptree.leaf_treeposition(leaf_index)
    print('Tree中节点的坐标定位：',tree_location)
    print('直接根据定位输出结果：',ptree[tree_location])
    print('该节点的父节点坐标定位：',tree_location[:-1])
    print('输出父节点到达叶子的值：',ptree[tree_location[:-1]])
    print('祖父节点坐标定位：',tree_location[:-2])
    print('输出祖父到叶子节点的值：',ptree[tree_location[:-2]])
    print('输出祖父节点值：',ptree[tree_location[:-2]].label())


    '''
    下面的问题是，怎么查看一个节点是否存在兄弟节点，因为检测到一个节点的中心词成立之后就要查看兄弟，不存在则
    回到孩子节点，测试it的NP节点的兄弟节点
    '''
    print(ptree[tree_location[:-2]].label())#输出it后退两部的NP节点的节点值为NP
    temp_p_tree = ptree[tree_location[:-2]]
    print('当前NP树：',temp_p_tree)
    if temp_p_tree.left_sibling() is None :
        print('我没有左兄弟节点')
    else:
        print(temp_p_tree.left_sibling().label())
    if temp_p_tree.right_sibling() is None :
        print('我没有右兄弟节点')
    else:
        print(temp_p_tree.right_sibling().label())
    '''
        查找一个子树父母树 和 root树，查看root的孩子节点
    '''
    parent_p_tree = temp_p_tree.parent()
    print('父节点树', parent_p_tree)

    root_tree = temp_p_tree.root()
    print('根节点树',root_tree)
    #因为这不是二叉树，所以不能用left_child这样的句子
    print("输出当前树的所有直接孩子")
    for i,child_tree in enumerate(root_tree):
        if isinstance(child_tree,Tree):
            print(child_tree.label())