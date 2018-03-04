"""
	图形界面编程: EasyGui工具包  http://easygui.sourceforge.net
"""
# 第一个方式导入需要加easygui对象
import easygui

easygui.msgbox('嗨，小甲鱼！')  # 消息

# 第二种导入，内部函数
from easygui import *

msgbox('Still fine')

# 建议使用方式
import easygui as g

g.msgbox('good for us')

# =============例子几种用法========
import sys

while 1:
    g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
    msg = "请问你希望在鱼C工作室学习到什么知识呢？"
    title = "小游戏互动"
    choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
    choice = g.choicebox(msg, title, choices)
    g.msgbox("你的选择是: " + str(choice), "结果")
    msg = "你希望重新开始小游戏吗？"
    title = "请选择"
    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
