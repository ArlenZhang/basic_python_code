'''
	生成器：迭代器的一种实现，使得python更加简洁，用法在普通函数里面加上一个yield，这样
python就能模仿实现协同程序（函数可以暂停挂起和继续）。
'''
def myGen():
	print('生成器被执行')
	yield 1
	yield 2 #出现表名当前函数是生成器，相当于return，返回参数之后回来还在这里

gen=myGen()#返回值是生成器暂停点
print(gen)

getAtt=next(gen)
print(getAtt)

getAtt=next(gen)
print(getAtt)
#不知道还有多少步，所以要异常检测
try:
	getAtt=next(gen)
	print(getAtt)
except StopIteration:
	print('生成器运行结束')

'''
	既然能用next并且是一种迭代器，那么就能遍历，每次遍历的结果就是yield的返回值，
重新构建斐波那契数列将很简单
'''
def fibo():
	a=0
	b=1
	while True :
		a,b=b,a+b
		yield a #这个数值每次都会暂停并返回

for getAtt in fibo():
	if getAtt > 30 :
		break
	print(getAtt,end=" , ")

'''
	特殊：没有元组推导式，元组中的推导形成的是生成器推导式
'''
d=(i for i in range(4))
print(next(d))

'''
	其他推导式，很多内置函数中直接运用推导式能简洁化编程
'''
#求和函数推导式
sumD=sum(i for i in range(10) if not(i%2))
print(sumD)
