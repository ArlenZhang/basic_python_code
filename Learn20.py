import time as t
class MyTime():
	'''
		掌握魔法方法之对象的输出字符串设计
	'''
	def __str__(self):
		return "我让你输出对象了吗？"
		
	__repr__=__str__
	
	
	#开始计时
	def start(self):
		self.startT=t.localtime()
		print('开始计时')
		print(self.startT)
	
	def stop(self):
		self.stopT=t.localtime()
		print('计时结束')
		print(self.stopT)
		self._calc()
	
	def _calc(self):
		self.last=[]
		self.str='总时间：'
		flag=True
		for index in range(6):
			self.last.append(self.stopT[index]-self.startT[index])
			if self.last[index]!=0 and flag :
				self.str+=str(self.last[index])
				flag=False
			elif not flag :
				self.str+=str(self.last[index])
		print(self.str)

t1=MyTime()
t1.start()
a=0
for index in range(10000) :
	a+=index
print(a)
t1.stop()

print(t1)