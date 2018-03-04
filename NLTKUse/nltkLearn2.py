from nltk import Tree
tree=Tree('ROOT', [Tree('NP', [Tree('NP', [Tree('DT', ['the']), Tree('JJ', ['quick']), Tree('JJ', ['brown']), Tree('NN', ['fox'])]), Tree('NP', [Tree('NP', [Tree('NNS', ['jumps'])]), Tree('PP', [Tree('IN', ['over']), Tree('NP', [Tree('DT', ['the']), Tree('JJ', ['lazy']), Tree('NN', ['dog'])])])])])])
tree.draw()
#我们能根据这个list画出
print(tree[0])
#输出节点存储的数据,用label得到标签
print(tree[0].label())
#树列的输出，输出叶子节点
print(tree[0,0,0,0]) #输出值的时候直接输出即可

#得到所有的叶子节点
leaves=tree.leaves()
print(leaves)
'''
怎么访问叶子节点的父节点，因为需要找到词性
'''

#查看这个tree是由哪些grammer产生的,对节点的前序遍历
print(tree.productions())

#对不符合和取范式的语法结构转变成和取范式
tree2= Tree('S', [ Tree('NP', ['Gary']),Tree('VT', ['play']),Tree('NP', ['baeball'])])
print(tree2)
tree2.chomsky_normal_form()
print(tree2)

#fromstring 和 parse
tree3=Tree.fromstring("""
(S (NP Gary) (VP (VT plays) (NP baseball)))
""")
tree3.draw()



