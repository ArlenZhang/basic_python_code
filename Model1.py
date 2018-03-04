'''
	模块1：基本运算实现
'''
def addA2B(a,b):
	return a+b

'''
	模块测试
'''
def test():
	print('进行测试：\n',addA2B(2,4))
	
	print('测试结束!')
#导入之后不希望运行测试代码
if __name__=="__main__" :
	test()