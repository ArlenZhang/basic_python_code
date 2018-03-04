"""
    异常的捕获和解决
    else语句

"""


def devision(num1, num2):
    try:
        result = num1 / num2
    except (ZeroDivisionError, TypeError) as reason:
        print('出错信息：' + str(reason))
    else:
        print('没问题，可以返回')
        return result
    finally:  # 必定执行的模块
        print('关闭资源呗')


result1 = devision(2, 0)
# 捕获之后能继续执行程序
result1 = devision('a', 2)
# 看看else是否执行
result1 = devision(6, 2)
print(result1)

# =========特殊的else,还能和循环语句、异常处理搭配
# ===test1
def judge_num(num):
    max_t = num // 2
    while max_t > 1:
        if num % max_t == 0:
            print('最大公约数：' + str(max_t))
            break
        max_t -= 1
    else:
        print('质数吧~大姐！')


# judgeNum(11)
judge_num(25)

# =========简洁的with语句的使用:没关闭的文件自动关闭
try:
    with open('none.txt', 'w') as f:  # with语句关注文件，不用则自动关闭
        print(f.readline())
except OSError as reason:
    print(str(reason))
