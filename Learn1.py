import random

print('Hello World!')

# 类型转换之 int float str的使用
a = 5.99
b = int(a)
print(b)
c = str(5e10)
print(c)  # 5e+10
print(c + ' 字符串拼接\n')
print(str(128) + ' 这样拼接\n')  # 报错可能
print('这样也是6\n' * 4)
print(True + True)

# 运算，优先级啦
# ** , + - , * / // + - , < <= > >= == != , not and or 优先级最后一级也从高到底
print('除法5/3：' + str(5 / 3) + ' 除法5//3：' + str(5 // 3) + ' 余数5%3：' + str(5 % 3))
print(-3 ** 2)
print("True or False and not True: " + str(True or False and not True) + "\n")
# equals True or (False and (not True))

# 生成随机数
randomNum = random.randint(1, 10)
temp = int(input('猜一猜大小：'))
# 类型检测
if isinstance(temp, int):
    inputNum = int(temp)
else:
    inputNum = 0
while inputNum != randomNum:
    if inputNum > randomNum:
        print('猜大啦！')
    else:
        print('猜小啦！')
    temp = int(input('再猜一猜：'))
    # 类型检测
    if isinstance(temp, int):
        inputNum = int(temp)
    else:
        inputNum = 0
print('你竟然猜对了~')
