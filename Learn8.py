# ===============================python中的字典构建==================================

# =========python中的字典构建============
# 1.传统构建方案如下：效率低
alpha = ['aIndex', 'bIndex', 'cIndex', 'dIndex']
dictionary = [['apple', 'append', 'abandon'], ['boy', 'blue'], ['cat'], ['door', 'dig', 'drag', 'drive']]
# 查找a打头的单词
print(dictionary[alpha.index('aIndex')])

# 2.字典构建和索引,属于映射类型
iDic = {'aIndex': ['apple', 'append', 'abandon'], 'bIndex': ['boy', 'blue'], 'cIndex': ['cat'],
        'dIndex': ['door', 'dig', 'drag', 'drive']}
numDic = {1: 'ff'}
print(iDic['aIndex'])
print(numDic[1])

# 3.也可以用工厂方式创建字典
dicByFc = dict((('a', 'alpha'), ('b', 110), (3, ['2', '3'])))
print(dicByFc)

# 4.工厂创建的时候用关键词创建，注意格式
dicByFc = dict(b='binana', a='apple', d='dog', c='cat')
print(dicByFc)

# 5.直接修改也能简便添加
dicByFc['arlen'] = ' cool '
print(dicByFc)

# =========python中的字典数据访问============
# 1.遍历 dict的四个属性 keys、values、items
zanDic = {}
zanDic = zanDic.fromkeys(range(4), '赞')  # 很重要的生成方式
for key in zanDic.keys():
    print(zanDic[key])
for val in zanDic.values():
    print(val)
for item in zanDic.items():
    print(item)  # item是元组

# 2.访问具体
print(zanDic[3])
# print(zanDic[4]) 越界报错
print(zanDic.get(3, "找不到"))
print(zanDic.get(4, "找不到"))

# 3.键是否存在
print(4 in zanDic)
print(len(zanDic))  # 直接输出字典条目数量

# 4.清空字典
zanDic.clear()
print(zanDic)

'''
 5. 字典赋值是引用传递，拷贝是数据备份
    clear清楚数据本身，nam={}只是换了指向
'''
copyDic = zanDic.copy()
newName = zanDic
# ===输出各自指向的地址
print(id(zanDic))
print(id(copyDic))
print(id(newName))

# 6.pop 和 popitem方法，pop和列表用法一致，popitem不仅删除最后元素而且返回值

# 7.更新字典
oldDic = {"a": "apple", "b": "blue"}
print(oldDic)
newDic = {"a": "avoid", "d": "dog"}
oldDic.update(newDic)
print(oldDic)

# ==================================字典推导式===================================
# 0-9的偶数平方展示
b = {i: (i * i) for i in range(10) if not (i % 2)}
print(b)

# =================================集合相关知识==================================
'''
    字典里面用的花括号这里也是，只是这里花括号直接放数据
'''
numSet = {1, 2, 3, 4, 3, 3, 4, 5}
print(numSet)
# 1.使用set工厂,以列表数据初始化得到集合
set1 = set({1, 4, 3, 2, 5, 6, 7, 4, 3, 2, 1})
print(list(set1))  # set是无序的，用list转变set的过程中会正序排序

print(1 in set1)  # 序列都可以这么用判断是否存在

# 2.增删数据
set1.add(10)
set1.remove(1)  # 删除的是数据而不是对应下标里面的数据
print(set1)

# 3.定义不可变集合
set2 = frozenset([1, 2, 6, 5, 4, 8, 7, 5])

# ==================================集合推导式===================================
li = [2, 3, 5, 6, 4, 5, 2, 1, 9, 13, 14, 16, 15]
c = {i for i in li if i % 2 == 0}
# 将列表中偶数提取出来并且不重复展示,依旧是集合展示列表数据会排序，集合没顺序

print(li.pop())
