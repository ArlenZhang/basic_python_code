# ===========================字符串的格式化问题===============================

# 1.位置参数的替换
formatStr = "{0} 是我们的 {1}".format("Tom", "孩子")
print(formatStr)

# 2.按关键字参数替换（存在位置参数要放前面）
formatStr = "我们是{0}, {a} 是我们的 {b}".format("夫妻", a="Tom", b="孩子")
print(formatStr)

# 3.对{xxx}的转义输出
print("{{0}}")
formatStr = "{{0}} 是的 {a}".format("能替换？", a="00")
print(formatStr)

# 4.数据格式化输出
formatStr = "{0:.1f}{1}".format(22.3323, 'place2')  # 前面的是数据格式化，四舍五入
print(formatStr)

# 5.视频015字符串格式化中讲了对%的使用进行数据转义、替换、得到格式化串
"""
    %s    字符串 (采用str()的显示)
    %r    字符串 (采用repr()的显示)
    %c    单个字符
    %b    二进制整数
    %d    十进制整数
    %i    十进制整数
    %o    八进制整数
    %x    十六进制整数
    %e    指数 (基底写为e)
    %E    指数 (基底写为E)
    %f    浮点数
    %F    浮点数，与上相同
    %g    指数(e)或浮点数 (根据显示长度)
    %G    指数(E)或浮点数 (根据显示长度)
    %%    字符"%"
"""

# ============================序列的内置方法====================================

# 1.list：将可迭代的对象转换为列表
str1 = "I love China"
strList = list(str1)
print(strList)

tuple1 = (1, 2, 3, 4, 5)
tupleList = list(tuple1)
print(tupleList)

# 2.tuple：将可迭代对象转换成元组,用法同上

# 3.len：返回序列长度

# 4.max：返回序列中最大值,min同样，但是要保证序列类型的一致
print(max(tupleList))

# 5.sum：对可迭代的对象进行求和
print(sum(tupleList))

# 6.sorted：从小到大排序，或者加参数 reverse反转排序

# 7.reversed：返回反转的迭代器对象
print(list(reversed(tupleList)))

# 8.enumerate：枚举，为每个元素添加一个index构成n个元组的列表
print(list(enumerate(tupleList)))

# 9.zip：返回匹配列表，列表元素为二元元组
myIndex = [7, 8, 9]
print(list(zip(myIndex, tupleList)))
