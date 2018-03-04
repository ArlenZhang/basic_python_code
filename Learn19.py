'''
	构造函数和析构函数，定义对象的时候最先调用的是__new__方法然后才是init方法，多与参数
悉数传给init方法，考虑对象定义是赋值操作，__new__存在返回值，就是当前类直接继承的基类。
__del__是析构方法，垃圾回收机制销毁调用析构方法，当对象指向的实例不再使用的时候调用
'''
class A(str):
	def __new__(cls,string):
		string=string.upper()
		return str.__new__(cls,string)
	def __del__(self):
		print('调用析构函数')
a=A("I am old enough.")
print(a)
b=a
c=b
print('删除a')
del a
print('删除b')
del b
print('删除c') #这时候对象实例真的不再使用了
del c

'''
	自定义对象的运算,对魔法方法的重写，继承基本类型用他们的构造函数~
	__mul__、__truediv__、__flooediv__...
'''
class MyNum(float):
	def __add__(self,other):
		return float(self)+float(other)
	def __sub__(self,other):
		return float(self)-float(other)
num1=MyNum(2)
num2=MyNum(3)
print(num1+num2)
		
'''
属性访问方式和几个魔法方法
	__getattr__() 访问的属性不存在的时候先触发下面第一个再触发这个
	__getattribute__() __setattr__() __delattr__() 对应的时候触发。。。
	
	注意防止死循环陷阱
	
'''
class Test:
	def __init__(self,val):
		self.val=val
	def getVal(self):
		return self.val
	def setVal(self,val):
		self.val=val
	def delVal(self):
		del self.val
	val=property(getVal,setVal,delVal)
	
	def __getattr__(self,name):
		print('正在访问不存在的变量')
		
	def __getattribute__(self,name):
		print('访问变量')
		
	def __setattr__(self,name,value):
		print('设置变量')
	def __delattr__(self,name):
		print('删除变量')

t=Test(250)
print(t.val)
t.val=120
print(t.val)
del t.val