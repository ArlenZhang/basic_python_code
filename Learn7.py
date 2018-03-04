# =================================递归阶乘===============================
def jie_c(num):
    if num == 1:
        return 1
    else:
        return num * jie_c(num - 1)


print(jie_c(5))


# ============斐波那契数列：工程数学中递归当误差小于一定数值则判断理想====
def feibo(num1, num2):
    print(num1 / num2)
    new_num1 = num2
    new_num2 = num1 + num2
    if abs(new_num1 / new_num2 - num1 / num2) < 0.0001:
        return num1, num2
    else:
        return feibo(new_num1, new_num2)


print(feibo(1, 1))

# =========================Python中汉诺塔问题解决==========================
"""
算法描述：
    用3个列表作为三座塔，从后向前取数据代表塔从上到下。每次每个列表中数据必须是倒序，
尝试将a列表中的三个数据移动到列表c中去。

pop 和 append方法实现移动，递归结束标志，当数目为1直接移动并返回上一层~

"""


# 参数说明：当前要移动的个数，从哪里移动到哪里
def hanoid(num, x, y, z):
    if num == 1:
        z.append(x.pop())
    else:
        hanoid(num - 1, x, z, y)  # 现将底层以上移动到另外一层
        z.append(x.pop())
        hanoid(num - 1, y, x, z)


# 全局变量
a = [3, 2, 1]
b = []
c = []
hanoid(len(a), a, b, c)
print('c', c)
