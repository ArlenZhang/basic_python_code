# ===========================元组的掌握===================================

tuple_t = (2, 3, 1, 4, 5, 6)  # 可以访问不能修改
print(tuple_t[0])
print(tuple_t[1:])
# tuple[0]=11
print(type((1)))  # 当前属于整型-->元组的判定在于逗号
tuple2 = 2, 3, 6, 7
print(type(tuple2))  # 属于元组类型

# *和+在元组中同样是 重复&合并
result = 8 * (1,)
print(result)

# 元组不可以赋值和删除，但是可以新建
tuple3 = tuple_t[:2] + (100,) + tuple_t[2:]
print(tuple3)

# python zip 内置方法
listA = [1, 2, 3, 4]
listB = [4, 3, 2, 1]
result_tuple = zip(listA, listB)
listB, listA = zip(*result_tuple)  # 相当于解压缩，返回两个list
print(result_tuple)

# ========================字符串的内置方法（基本全是返回值方式）======================
str1 = "I love china"
str2 = "I LOVE YOU"
print(str1[3:] + "最后一个字母获取：" + str1[len(str1) - 1])  # 类数组喽
# 将字符串首字母大写
str1.capitalize()
# 所有字母小写
str2.casefold()
# 左右空格居中
str2.center(8)
print("str1: " + str1 + " str2: " + str2 + "\n")
# 计算字符出现次数，同列表--->字符串和列表很像
print(str1.count('lo', 0, len(str1)))
# endswith还有区域可选参数
print(str1.endswith('na'))

# find函数也包含范围参数（可选）
subIndex = str1.find('dd')
if subIndex != -1:
    print('包含子串,下标：' + str(subIndex))
else:
    print('不包含')

# 方法列举： index(sub,xx,xx) 不在则抛出异常
#           isalnum()至少有一个字符且所有字符是字母或者数字
#           isalpha()、isdecmial() 十进制数字、isdigit()数字、isnumeric()
#           lower()、upper()、islower()、isupper()、isspace()只包含空格
#           istitle()单纯首字母都是大写返回True
#           str.join(sub)将str插入到sub的每个字符之间
#           ljust()左对齐、rjust右对齐、lstrip()去左边所有空格、rstrip()、strip()
#           partition(sub)将串分割成三元组
#           rfind()右查找、rindex()右定位、

# 字符串分割-->元组
strTotal = '   I want you.   '
resultTuple = strTotal.partition('want')
print('分割得到的三元组：')
print(resultTuple)
print("===================================================")

# join方法拼接字符串
resultStr = '-'.join('you')
print(resultStr)
resultStr = '-'.join(['ss', 'dd', 'fff'])  # 必须是同类型
print(resultStr)

print("===================================================")

# 替换replace,返回结果串
resultStr = strTotal.replace('want', 'love', 1)  # count指定则替换不超过count次
print(resultStr + '\n')

# 切割返回列表
print(resultStr.split(' '))

# 按行切割
linesStr = "sss\n ddddd\nsssssss\n"
print(linesStr)
print(linesStr.splitlines())

# 去左右两边的空格
print(strTotal.strip())

# 大小写反转 swapcase
print(strTotal.swapcase())

# strl.translate(str.maketrans('old','new')) 按照映射表进行替换

strx1 = "I love you."
