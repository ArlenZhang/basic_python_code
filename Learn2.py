# ========================elseif 在python中的书写格式
score = int(input('输入分数：'))
if score > 100:
    print('出错误！')
elif 100 >= score >= 80:
    print('合格！')
else:
    print('重修~')

# ========================三元操作符
tip = 'vip' if score > 90 else 'shit'
print(tip)

# ========================断言 assert,抛出异常
# assert 0 > 10

# ========================for循环
# 1.对字符串字符遍历
favor = 'fish'
for i in favor:
    print(i, end=' ')  # 按照行输出，默认换行输出
print('\n')

# 2.对列表遍历
animals = ['dog', 'cat', 'fish']
for animal in animals:
    print(len(animal))
# 3.优化，用enumerate方法遍历，既有数据遍历也有索引跟踪
for index, animal in enumerate(animals):
    print(animal, index, end=' ')
print("")
# 3.普通数组列表
for i in range(1, 10, 3):  # 按照步长构建列表，对range函数的灵活使用
    print(i)

# =============continue 和 break 与其他语言大同小异~

# ==========================列表存储结构掌握=====================================

mixList = [22, 'element', 2.1, [1, 2, 3]]

print(mixList)
print(' length：'+str(len(mixList)))

# ====列表中的列表中的数据访问方式
print('访问元素中的元素：' + str(mixList[3][0])+"\n")

# ====列表的操作
# 1.append追加
mixList.append('arlen')
print(mixList)
print(' length：'+str(len(mixList))+"\n")

# 2.extend 用列表+也行，但是最好统一书写用extend
mixList.extend(['gg', 'ww'])
print(mixList)
print(' length：'+str(len(mixList))+"\n")

# 3.insert，0是python的绝对开始
mixList.insert(0, '牡丹')
print(mixList)
print(' length：'+str(len(mixList))+"\n")

# 4.获取元素,和其它语言里面的数组一样的
print(mixList[0])

# 5.从列表删除的实现
mixList.remove('gg')
del mixList[0]  # 语句删除指定下表的元素
# del mixList清空列表
print(mixList)

# 6.pop方法，取出元素并且返回,默认从最后一个剔除,也可以加索引值获取剔除
print(mixList.pop())
print(mixList)

# 7.列表的批量获取
print(mixList[1:3])
print(mixList[:3])
print(mixList[3:])
copyList = mixList[:]  # 获取拷贝
newNameList = mixList  # 异名同根
newNameList[0] = 'replaced'
print(copyList)
print(mixList)

# 8.列表的比较，从左小右决定，递增列表比较有意义

# 9.列表翻倍用*和字符串翻倍类似

# 10.判断列表中是否存在元素很重要，in语句在很多序列中都适用
if 'replaced' in mixList:
    print('该元素在列表中出现')
else:
    print('不存在')

# 11.计算数元素存在个数
print(mixList.count('replaced'))

# 12.返回某个区域内某元素出现的首位，也可以不要区域
print(mixList.index('replaced', 0, len(mixList)))

# 13.列表反转
up = [1, 7, 3, 8]
down = up[:]
down.reverse()  # 注意没有返回值
print(down)

# 14.列表排序，默认归并排序
up.sort(reverse=True)
print(up)  # 默认不要参数则从小到大，否则从大到小

"""
列表推导式,轻量级循环，用其他的列表创建新列表的过程
"""
# 下面的构建方式适用于函数变量数量和类型未知的时候
myList = [x for x in mixList]
print('mylist', myList)

a = [i for i in range(100) if not(i % 2) and i % 3]
print(a)

# 当然也可以为轻量级循环增加变量和结果构建元组或者列表的列表
mixList = [(x, y) for x in range(3) for y in range(3)]
print(mixList)
