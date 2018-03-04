# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:50:27 2017

@author: arlen
"""

#==================赋值魔法==============================
print('==================赋值魔法和序列解包==========================')
x,y,z=1,2,3
print(x,y,z)
x,y=y,x
print(x,y,z)

#当返回元组时候很好用
dict={'a':'apple','b':'blue'}
print(dict)
key,value=dict.popitem()#这个才会有返回值的啊
print(key,value)

#链式复制，基本变量是复制，特殊变量是同指向
v1=v2=[2,3,4]#链式赋值也是适用
v1.pop()
print(v2)

#会被编译器当做false的元素：False None 0 "" () {} []

#======pass del exec三人行=================
'''
如果程序什么事都没做但是存在这个函数，就用pass

exec的作用：能动态的改变代码结构，注意命名冲突，所以要涉及命名空间
'''

#======手机参数* 和 **这两个方式的区别,前者返回元组，后者返回字典 =======
def funcForAttr(name,*args,**dicts):
    print (name)
    print (args)
    print (dicts)
funcForAttr('arlen','aaa',14,foo=1,boo=2)

