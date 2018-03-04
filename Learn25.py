'''
	python开发思考：最好用一种方法解决同一个问题-->标准模块使用
	同时，https://pypi,python.org/pypi汇集了全球python爱好者提供的若干开源模块可供
使用。
	思考这个timeit里面的语句能不能换成测量函数运行时间？
'''
#怎么使用，举例计时器应用，计时器不要手写，用模块 timeit
from timeit import *
import timeit

print(timeit.__doc__)
print(dir(timeit))
print(timeit.__all__)#用得到的东西，from timeit import*导入时只导入这些
print(Timer)
#==查找模块源代码
print(timeit.__file__)
#help(timeit)

'''
	timeit模块详解：该模块定义了三个函数timeit()、repeat()、default_timer()和公共类
Timer。

timeit函数：timeit(stmt='pass',setup='pass',timer=<default timer>,number=1000000)
	stmt：需要测量的语句或函数
	setup：初始化代码
	timer：默认机时器
	number：语句执行次数
	根据这几个默认参数，我们要计算一个语句执行number次的运行时间就相当方便
'''

#10阶乘函数执行100次
def func():
	for i in range(1,11):
		i*=i

print(timeit.timeit("func()", setup="from __main__ import func"),'==================================')


timeLast=timeit.timeit('"arlen".join(["Father","Mother"])',number=10000)
print(timeLast)


'''
repeat函数：repeat(stmt='pass',setup='pass',timer=<default timer>,repeat=3,number=1000000)
	repeat：重复测量的次数
'''
timeLast=timeit.repeat('"arlen".join(["Father","Mother"])',repeat=4,number=10000)
print(timeLast)

'''
default_timer函数：default_timer()
	默认计时器,记录自然时间，疑问到底返回了什么时间？
'''
print('=============')
print(timeit.default_timer())
'''
Timer类：Timer(stmt='pass',setup='pass',timer=<timer function>)
	计算小段代码执行速度的类，timer（计时函数）
	用的时候用Timer构建对象传入语句、初始化，在执行timeit测时间即可
	timeit() and repeat()其中repeat就是重复n次执行timeit方法
	
	print_exc()输出计时代码的回溯，常用如下
'''
mytt=timeit.Timer('for i in range(10):oct(i)','gc.enable()')
try:
	print(mytt.timeit())
	print(mytt.repeat(3))
except Exception:
    mytt.print_exc()




