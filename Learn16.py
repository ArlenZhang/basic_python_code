'''
	面向对象编程，数据封装、函数封装
	掌握类的定义使用方法，数据的初始化，方法调用
'''
class Person:
	__password='123456'
	username='arlen'
	def __init__(self,uname): #两个下划线初始化 不能有返回值
		self.uname=uname
	def setName(self,name):
		self.name=name
	def introduce(self):
		print('hello! I am %s' % self.name)
	#定义访问私有变量的公有函数
	def getPWD(self):
		return self.__password
	
arlen = Person('none')
arlen.setName('arlen')
arlen.introduce()

#self是什么？默认参数，内有任意多的数据变量，根据需求

'''
	其中init方法是魔法方法
	私有函数和变量的定义方式只用在前面加上两个下划线即可
	注意：内部函数访问变量记得传递self参数调用
	伪私有变量  _ClassName__vName即可访问
'''
blue=Person('blue') #相当于构造函数

print('username: '+blue.username)
#print('userPWD: '+blue.__password) #私有变量直接访问失败
print('userPWD: '+blue.getPWD())

'''
	类的继承机制
'''
class Fish:
	def __init__(self):
		self.length=100
		self.weight=200
	def breath(self):
		print('我是鱼我要呼吸')
	
class SalmonFish(Fish):
	name='三文鱼'
	def myDish(self):
		print('我是%s,我被做成三文鱼大餐,我的体重是%d' % (self.name,self.weight))

class DeadFish(Fish):
	#自定义死亡时间，设置初始化方法将覆盖父类初始化方法
	def __init__(self):
	
		#两种方法调用父类init
		#Fish.__init__(self)
		super().__init__() #建议使用
		self.deadTime=10
	def desc(self):
		print('我死了%d年了，当时我长度是%d'%(self.deadTime,self.length))
	
	def breath(self):
		print('我是死鱼，我不呼吸~')


sFish=SalmonFish()#先调用父类初始化方法

sFish.breath()#方法继承
sFish.myDish()#孩子方法
dFish=DeadFish()
dFish.breath()#方法重写
dFish.desc()

'''
	多继承写法 Class(class1,Class2) 尽量使用单继承
'''
