"""
    gui
"""
import easygui as g
from easygui import *
import sys

# ====msgbox,重写按钮最简单方法
g.msgbox('你想升学吗？', ok_button='是啊')

# ====ccbox 核实框 Continue 或者 Cancel, 返回整型的 1 或 0，不是布尔类型的 True 或 False
if ccbox('要再来一次吗？', choices=['要啊要啊^_^', '算了吧T_T']):
    msgbox('不给玩了，再玩就玩坏了......')
else:
    sys.exit(0)  # 记得先 import sys 哈

# ====ynbox
ynbox(msg='Shall I continue?', title=' ', choices=['Yes', 'No'], image=None)
# ====butonbox显示自定义一组按钮
buttonbox(msg='', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, root=None)
# ====基本跟上边一样，区别就是当用户选择第一个按钮的时候返回序号 0， 选择第二个按钮的时候返回序号 1。
indexbox(msg='Shall I continue?', title=' ', choices=['Yes', 'No'], image=None)
# ====boolbox() 如果第一个按钮被选中则返回 1，否则返回 0。
boolbox(msg='Shall I continue?', title=' ', choices=['Yes', 'No'], image=None)

# ====在 buttonbox 里边显示图片
buttonbox('大家说我长得帅吗？', image='../data/pictures/hanoid.png', choices=['帅', '不帅', '!@#$%'])

# ==== choicebox
chosen = choicebox(msg='Pick something.', title=' ', choices=['arlen', 'chaoyue', 'ligq'])
print(chosen)

# ====multchoicebox(),多选，返回列表
print(multchoicebox(msg='Pick as many items as you like.', title='买宠物', choices=('狗狗', '毛毛', '虾子')))

# ====enterbox()用户输入
write = enterbox(msg='Enter something.', title='输入学号', default='110', strip=True, image=None, root=None)
print(write)

# ====integerbox 给用户输入一定区间以内的数据
integerWrite = integerbox(msg='输入你的年龄：', title='登记', default=10, lowerbound=0, upperbound=120, image=None, root=None)
print(integerWrite)

# ====multenterbox() 为用户提供多个简单的输入框
list1 = ['用户名:', '密码:']
g.multpasswordbox(msg='请输入用户名和密码', title='登录', fields=list1)

# ====passwordbox()输入密码
passwordbox(msg='Enter your password.', title='title', default='123', image=None, root=None)

# multpasswordbox() 跟 multenterbox() 使用相同的接口，但当它显示的时候，最后一个输入框显示为密码的形式（"*"）
multpasswordbox(msg='Fill in values for the fields.', title='pwd', fields=['姓名', '年龄', '密码'], values=[1, 2, 3])

# ================文本显示==================
textbox(msg='sssss:', title='tt ', text='aaaaaaaaaaaaaaaaaaaaaa\ndfsertetwee\nrrtrt', codebox=0)
# textbox(text= open('E:\\学习材料\\Python\\Index.txt','r'))

# codebox相当于上面的codebox=1
# diropenbox用于提供一个对话框，返回用户选择的目录名（带完整路径哦），如果用户选择"Cancel"则返回 None。
path = diropenbox(msg=None, title=None, default=None)
print(path)

# fileopenbox同上对于文件路径
path = fileopenbox(msg=None, title=None, default='*', filetypes=None)
print(path)

# filesavebox() 函数提供一个对话框，让用于选择文件需要保存的路径
filesavebox(msg=None, title=None, default='', filetypes=None)

# 捕获异常 exceptionbox()
try:
    print('I Love FishC.com!')
    int('FISHC')  # 这里会产生异常
except:
    exceptionbox()
