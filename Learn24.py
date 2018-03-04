'''
	模块是更高级的封装,例如Learn7.py就是一个模块，导入使用,提高代码的复用性
'''
import Model1 as m
#import Model1
#from Model1 import* #导入所有函数
print(m.addA2B(1,3))

'''
	理解__name__变量
'''
print(__name__) #当前程序的__name__值是__main__
print(m.__name__)#杯倒入模块的__name__值是该模块的文件名
'''
	上面的导入很简单，导入同一文件架下面的文件，如果文件存在一定结构，运用
搜索路径实现。
'''
#先查看一下系统路径分布
import sys
print(sys.path)
#不存在我要导入的文件路径，这时候添加路径
sys.path.append('E:\\学习材料\\Python\\files')
print(sys.path)
import test1 as t1
t1.func()

'''
	文件导入还挺麻烦-->包的创建和导入
	在file下面创建新的文件夹例如package,将之前的test1模块放进包中，在包中创建一个
名称为__init__.py的文件，内容可以为空-->进行导入
'''
import packages.test1 as t2
t2.func()
#导入整个包？




