'''
	正则表达式，python的re模块
'''
import re
#搜索指定字符串并返回首个位置信息
pos=re.search(r'arlen','arlen is very cool arlen')
print(pos)#用find其实也能搜索简单的串

# .号代表任何一个字符,\.代表字符串中的.本身
pos=re.search(r'do.','arlen is doing sth')#.代表了i
print(pos)

#关于反斜杠的使用，(xx)是一个子组,do do重复
pos=re.search(r'(do) \1','arlen is do do doing sth') #重点
print(pos,'+=====')

#[]里面的东西都变成最普通的字符看待，除了 - 、\
pos=re.search(r'do[.]','arlen is doing sth')#.代表了i
print(pos)

'''
	\d  数字、 \w 字母或者数字、 \s 各种空白换行等 、大写取非
	\b 匹配单词边界 
'''
pos=re.search(r'\d{4}ar[0-9]','1123arlen is do3322ar2ing sth')
print(pos)

pos=re.search(r'[ir]','1123arlen is do3322ar2ing sth')#或者(i|r)
print(pos)

'''
	sdfsdfsdfsdf11.231.1111.234erwed22.3.123.45dseeee3ra
	匹配到ip地址出来
	\d{2}|1\d{2}|2[0-5][0-5]
'''
print('==================ip==================')
pos=re.search(r'((\d{1,2}|1\d{2}|2[0-5][0-5])\.){3}(\d{1,2}|1\d{2}|2[0-5][0-5])','sdfsdfsdfsdf11.231.1111.234erwed22.3.123.45dseeee3ra')
print(pos)

#匹配开始和结束，^不放在括号中的情况
pos=re.search(r'(^arlen)\w*(arlen$)','arlen skdfhsheubhfhs arlen')
print(pos)
#当然了，^(脱字符)放在[]里面使用有排除的含义
pos=re.search(r'[^\w]','a2rlen skdfhsheubhfhs arlen')
print(pos,'<---')
#如果脱字符不放在最前面,匹配^本身
pos=re.search(r'[\d^\w]','  ^ssda2rlen skdfhsheubhfhs arlen')
print(pos,'<===') 

'''
	+ >=1 、 * >=0 、 ? 0 or 1
	python正则表达式默认开启贪婪模式，它匹配尽可能多的符合元素
'''
pos=re.search(r'<.+>','<html>dsdfsdf</html>dssdfs<br>')
print(pos)

#关闭贪婪模式，需要在表示重复的元字符后面加上一个?即可
pos=re.search(r'<.+?>','<html>dsdfsdf</html>dssdfs<br>')
print(pos,'<=====')


