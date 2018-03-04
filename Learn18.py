'''
	和类相关的内置函数
'''
#1.issubclass(classA,classB)判断A是不是B的子类的函数
class A:
	pass
class B(A):
	pass
class C:
	pass
print(issubclass(B,A))
print(issubclass(B,B))
print(issubclass(B,object))#object类是所有类的基类
print(issubclass(B,C))
print('====================================================')

#2.isinstance(instance,classC)判断一个实例对象是不是一个类的对象
b=B()
print(isinstance(b,A))
print(isinstance(b,C))
print('====================================================')

#3.hasattr(obj,attr)判断一个实例是否包含一个属性
#4.getattr(obj,attr)获取属性值，参数3可选
b.attr1=12 #新建属性
if hasattr(b,'attr1'):
	print(getattr(b,'attr1','您访问的参数不存在'))

#5.setattr(obj,name,value)设置属性值
setattr(b,'attr2','21')

#6.delattr(obj,attr)删除指定属性，不存在则抛出异常
delattr(b,'attr1')
print('====================================================')

#7.property(fget=None,fset=None,fdel=None,doc=None)用属性定义属性，简化操作
class D:
	def __init__(self,size):
		self.size=size
	def getSize(self):
		return self.size
	def setSize(self,value):
		self.size=value
	def delSize(self):
		del self.size
	represent=property(getSize,setSize,delSize)
d=D(10)
print(d.represent)
d.represent=110
print(d.represent)
del d.represent
print(d.represent)




