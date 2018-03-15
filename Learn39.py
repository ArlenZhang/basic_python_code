# Arlen
# 对 tensorflow 里面的一些数据变换使用， numpy继续学习
import numpy as np
# 创建numpy数组
print("-----------创建数组------------")
arr_o = [[1, 2, 3], [4, 5, 6]]
print(arr_o[0][1])
arr_a = np.array(arr_o)
print(arr_a[0][1])

print("-----------数组初始化------------")
# 根据指定数据初始化
seven_arr = np.full((3, 3), 7)
print("指定数字：", seven_arr)

# asarray将列表、元组等转变成numpy的数组
one_list = (1, 2, 3)
arr = np.asarray(one_list)
print("asarray: ", arr)

# fromiter 从任何可迭代数据构建数组
buffer = 'Iamdsdsfsf'
arr = np.fromiter(buffer, dtype='S1', count=-1)  # count代表读取到位置
print(arr)

# empty 创建位置上数据为空的数组
a = np.empty((2, 3), dtype=int)
print("empty数组: ", a)

# 随机初始化
random_arr = np.random.random((3, 3))
print("random arr：", random_arr)
# 随机新方法
random_choice = np.random.choice(100, 10)
print("random_c: ", random_choice)

print("-----------自定义数据类型------------")
# dtype 自定义数据类型
'''
    numpy里面的数据类型：
                    'b'：布尔值
                    'i'：符号整数
                    'u'：无符号整数
                    'f'：浮点
                    'c'：复数浮点
                    'm'：时间间隔
                    'M'：日期时间
                    'O'：Python 对象
                    'S', 'a'：字节串
                    'U'：Unicode
                    'V'：原始数据（void）
'''
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
students = np.array([('abc',  21,  50), ('xyz',  18,  75)], dtype=student)
print("students: ", students)

# dtype多样化使用
data = np.dtype([('attr1', 'i4'), ('sttr2', 'i4')])
a = np.zeros((2, 2), dtype=data)
print("指定类型数组作为item: ", a)

print("-----------矩阵变形------------")
# list不具备shape size这样的方法
print("shape: ", arr_a.shape)
print("size: ", arr_a.size)

# 用reshape调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print("原数组shape: ", a.shape, "reshape(3, 2)结果：")
print(b)

# 平铺矩阵
arr_a = np.array([[1, 2, 3], [4, 5, 6]])
arr_b = arr_a.flatten()
print("平铺结果: ", arr_b)

# 行、列合并
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
arr_c = np.vstack((arr_a, arr_b))  # vertical
arr_d = np.hstack((arr_a, arr_b))
print("垂直合并结果: ", "\r\n", arr_c)
print("水平合并结果: ", "\r\n", arr_d)

# 追加数据
arr_e = np.row_stack((arr_a, arr_b))
print("按行追加结果：", "\r\n", arr_e)
arr_f = np.column_stack((arr_e, np.array([1, 2])))
print("按列追加结果：", "\r\n", arr_f)

# 行、列分割机器学习常用
arr_a = np.array([[1, 2, 3], [3, 2, 1], [3, 1, 2]])
arr_b = np.vsplit(arr_a, 3)
arr_c = np.hsplit(arr_a, 3)
print("垂直分割结果: ", arr_b)
print("水平分割结果: ", arr_c)

# 转置
arr_a = np.array([[1, 2, 3], [4, 5, 6]])
arr_b = arr_a.T
print("转置结果: ", "\r\n", arr_b)
arr_a = np.array([1, 2, 3])
arr_b = arr_a.T
arr_c = np.dot(arr_a, arr_b)
arr_d = np.dot(arr_a, arr_a)
print("转置再矩阵乘法: ", arr_c)
print("直接对一维矩阵乘法: ", arr_d)  # 总结来看，一维情况可行可列，不用转置

# 列转置的最终实现
arr_a = np.array([1, 2, 3])
arr_b = arr_a[:, np.newaxis]
print("输出一维转置的结果: ", "\r\n", arr_b)

print("-----------维度、itemsize------------")
# 对dim参数的理解
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("a、b的维度分别为：", a.ndim, '  ', b.ndim)

# arange dim方法使用
a = np.arange(1, 25, 1)  # 步长为1
b = a.reshape(2, 4, 3)   # 转成2个4行3列的3维空间数据
print("a: ", a)
print("b: ", b)
print("b.ndim: ", b.ndim)

# itemsize 这一数组属性返回数组中每个元素的字节单位长度
a = np.array([1, 2, 3, 4], dtype='i4')
print("每个元素长度: ", a.itemsize)

print("-----------遍历方案------------")
# slice技术
a = np.arange(1, 20, 1)
s = slice(2, 10, 2)  # 作为索引
print("根据slice索引输出: ", a[s])

# 简写遍历
a = np.arange(1, 20, 1)
print("简写遍历1: ", a[2:7:3])  # 第三个参数是步长
print("简写遍历2: ", a[2:])

# 高级索引
a = np.array([[1, 2], [3, 4], [5, 6]])
b = a[[0, 1, 1], [1, 1, 0]]
print("高级索引结果: ", b)  # 获取交叉坐标点的数据

# 布尔索引
a = np.array([1, 2, 3, 4, 5])
bool_r = a > 2
print("布尔索引结果: ", bool_r)
count = np.count_nonzero(bool_r)
print("Number of True: ", count)

print("-----------numpy矩阵运算------------")
arr_a = np.array([1, 2, 3, 4])
arr_b = arr_a
print("arr_a: ", arr_a)
print("arr_b: ", arr_b)
# 直接相乘和np的multiply都是对应位乘
print(arr_a*arr_b)
print(np.multiply(arr_a, arr_b))

# np矩阵的平方即对应位平方
print("矩阵平方结果: ", "\r\n", arr_a**2)

# dot参数为1维时对应两个一维矩阵的对应位乘积之和
print("一维参数输出: ", np.dot(arr_a, arr_b))

# dot参数为2维时对应矩阵乘法
arr_a = np.array([1, 1])
arr_b = np.array([[1, 2, 3], [1, 1, 1]])
print("二维参数输出: ", np.dot(arr_a, arr_b))

# matmul or @  is preferred 建议使用这样的符号进行矩阵乘法
arr_c = arr_a @ arr_b
print("@运算结果: ", "\r\n", arr_c)
arr_c = np.matmul(arr_a, arr_b)
print("matmul运算结果: ", "\r\n", arr_c)

# 矩阵的加减法
arr_a = np.array([1, 2, 3])
arr_b = np.array([1, 1, 1])
arr_c = arr_a + arr_b
print("矩阵加法结果: ", "\r\n", arr_c)

print("-----------numpy三角函数运算------------")
arr_a = np.array([1, 2, 3])
tanh_r = np.tanh(arr_a)
print("三角函数结果: ", "\r\n", tanh_r)

print("-----------取最大最小值下标、求和、中位数------------")
arr_a = np.array([1, 2, 3])
min_r = np.argmin(arr_a)
max_r = np.argmax(arr_a)
sum_r = np.sum(arr_a)
accumulate_sum_r = np.cumsum(arr_a)
mean_r = np.mean(arr_a)
mid_r = np.median(arr_a)
print("argmax: ", max_r)
print("argmin: ", min_r)
print("sum_r: ", sum_r)
print("accumulate_sum_r: ", accumulate_sum_r)
print("mean_r: ", mean_r)
print("mid_r: ", mid_r)

print("-----------排序------------")
arr_a = np.array([3, 2, 1])
arr_b = np.sort(arr_a)
arr_a = np.array([[9, 5, 3], [3, 2, 1]])
arr_c = np.sort(arr_a)
print("排序结果1: ", arr_b)
print("排序结果2: ", "\r\n", arr_c)
# 很多类似运算默认进行行运算，通过参数axis可以进行调整
arr_d = np.sort(arr_a, axis=0)
print("列排序结果: ", "\r\n", arr_d)

print("-----------clip对数据中部分数据规范化防止梯度爆炸------------")
arr_a = np.array([1, 1, 100, -100])
arr_b = np.clip(arr_a, 0, 10)
print("clip结果: ", arr_b)

print("-----------地址传递与值传递------------")
arr_a = np.array([1, 2, 3])
arr_b = np.copy(arr_a)
arr_a[0] = 22
print(arr_a)
print(arr_b)

print("------------行数列数---------------")
arr_a = np.array([[1, 2, 3], [4, 5, 6]])
print("列数: ", arr_a.shape[-1])
print("行数: ", arr_a.shape[-2])
