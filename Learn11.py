"""
    有了OS模块，我们不需要关心什么操作系统下使用什么模块，OS模块会帮我们选择正确的模块调用
本页内容掌握os模块对文件本身和文件夹等操作。

os函数列举：
getcwd()、chdir()改变工作目录、listdir('path')、mkdir("")单层目录创建、mkdirs("")多层
remove(path)删除文件、rmdir(path)删除空文件夹、removedirs(path)删除多层目录
rename(old,new)重命名、system("")运行系统shell命令

os常量：
    curdir当前目录、pardir上一级目录、sep系统路径分隔符、linesep行终止符、name当前操作系统对于
    路径字符串 的操作见小甲鱼扩展阅读
"""
import os

print(os.getcwd())  # 获取当前工作目录
print(os.listdir('E:/学习材料/Python'))  # 列举指定目录下的所有文件名
os.system('calc')  # 打开计算机
print(os.curdir)
print(os.name)  # window 基于ns架构
