# ==================================函数的操作掌握===================================

# 1.带参数和返回值的函数定义规范
def get_muti(num):
    muti = 1
    while num > 0:
        muti *= num
        num -= 1
    return muti, num  # 返回元组


# ===调用===
print("乘得的结果是：" + str(get_muti(4)))


# 2.当参数数量很多的时候关键字参数尤为重要
def hello_world(sb, sth="Nothing"):
    print(sb + " said " + sth)


# ===调用===
hello_world(sth="Hello World!", sb="arlen")
hello_world("arlen")  # 有默认参数的情况


# 3.在参数前加*形成可变参数
def myth_func(*params, name):
    print(params)  # 查看实际情况
    print(name + "先生找第一个参数信息是：" + str(params[0]))


# ===调用===
myth_func(1, 2, 3, 4, 5, name="arlen")


# 4.全局变量
def change_val():
    # print("打印全局变量：",allV)
    # allV=77 #注意点：在函数中使用全局变量时python新建局部变量copy全局变量的值，只能查看
    global allV  # 这样执行才能修改
    allV = 333


# 定义全局变量
allV = 100
change_val()
print("再次打印全局变量：", allV)

# python支持函数嵌套，函数内部定义函数（注意只有外部函数内部能调用它）
