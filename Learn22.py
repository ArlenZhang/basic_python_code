"""
    与定制容器有关的协议
    ->  定制不可变容器： 定义__len__() __getitem__()
    ->  定制可变容器： 还需要定义__setitem__()和__delitem__()

"""

# 自定义不可改变的列表，记录访问次数
class MyList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.countDict = {}.fromkeys(range(len(self.values)), 0)  # 学过

    def __len__(self):
        return len(self.values)

    def __getitem__(self, k):
        self.countDict[k] += 1
        return self.values[k]


list1 = MyList(1, 2, 3, 4, 5)
print(list1)
print(list1[2])
print(list1.countDict)

'''
    迭代器提供两个方法 iter()和 next()
    魔法方法：__iter__() 和 __next__()
'''
str1 = 'addiction'
ite = iter(str1)  # ite就是一个迭代器了
while True:
    try:
        print(next(ite), end='')
    except StopIteration:
        break


# 迭代器的魔法方法实现斐波那契数列
class Fibs:
    def __init__(self, stopPoint=10):
        self.a = 0
        self.b = 1
        self.stopPoint = stopPoint

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.stopPoint:
            raise StopIteration  # 停止迭代
        return self.a


f = Fibs(20)
for each in f:
    print(each, end=' ')
