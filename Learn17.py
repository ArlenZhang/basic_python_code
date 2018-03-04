'''
	要求定义个水池类，包含鱼儿和乌龟，这时候很多类不存在继承关系而是共同组合成水池，
所以组合由此派上用场。
'''
class Turtle:
	def __init__(self,x):
		self.num=x
		
class Fish:
	def __init__(self,x):
		self.num=x

#说白了就是类的数据变量为特殊类的类型
class Pool:
	def __init__(self,x,y):
		self.turtle=Turtle(x)
		self.fish=Fish(y)
	def getNum(self):
		print(self.turtle.num)
		print(self.fish.num)

pool=Pool(2,3)
pool.getNum()
print('========================================')
'''
	对象实例和类实例的属性值之间的关系
'''
class CS:
	count=0
	def printCount(self):
		print(self.count)

#count属于类实例的数据
print(CS.count)

#定义两个对象实例
a=CS()
b=CS()

print(a.count)#实例对象有了类的数据，也就是能访问到的count是类实例的数据
a.count=100   #重新赋值不会改变类实例的数据，而是对象实例新建的属性信息
print(a.count)
print(CS.count)
print(b.count)

#同样新建的变量能覆盖函数
a.printCount()#能调用
a.printCount=0#新建变量同名
#a.printCount()#报错
print('===========================================')
'''
	类中定义的属性和方法都是静态的，所以类实例删除之后属性和方法还在内存，之前的对象实例仍
然可以调用
'''
del CS
b.printCount()