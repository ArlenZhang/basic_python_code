# ===========================闭包编程范式======================
def func_outer(x):
    def func_inner(y):
        return x * y

    return func_inner


# ===调用===
rep = func_outer(2)
print(type(rep))
result = rep(4)
print(result)
result = func_outer(5)(6)
print(result)


def func_outer2():
    x = 5

    def func_inner():
        nonlocal x  # 试图修改外部‘全局变量’x,这时候需要设置为非局部变量才能实现
        x = 10
        return x

    return func_inner


# =====================lambda表达式运用于定义数学中的函数公式========================
# ===demo1
g = lambda x: x * x + 2 * x + 1
print(g(6))
# ===demo2
average = lambda x, y: (int(x) + int(y)) / 2
print(average(input(), input()))

# =========================filter内置函数，过滤==============================
# 1.None情况下默认过滤掉false值
print(list(filter(None, [1, 3, True, 0, False])))


# 2.自定义过滤函数-->留下偶数
def even(num):
    return True if num % 2 == 0 else False


print(list(filter(even, [1, 2, 3, 4, 5, 6])))

# ============================filter结合lambda=================================
print(list(filter(lambda x: 1 - x % 2, [1, 2, 3, 4, 5, 6])))

# ============map实现结合lambda对一组数据针对lambda映射得到一组新的结果========
print(list(map(lambda x: x + 1, [1, 2, 3, 4, 5])))
