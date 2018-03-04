import re
import urllib.request
#===========================方法使用=====================================
print('===========方法来了=============')
#1.search()方法上面比比皆是

#2.findall方法，查找所有匹配的元素并构成列表返回，厉害了
listF=re.findall(r'\d{3}','ds33wwe453rtdffssa111e')
print(listF)

#3.compile方法，编译一次 处处运行
p=re.compile(r'[a-z]')
print(p.search('2132aaa')) #编译过的对象提供了搜索起止点，可选参数
print(p.findall('324s4f5hh56'))

#4.group方法获取匹配结果,正则表达式中的子组从前往后可以通过group参数获取
result=re.search(r"(\w+) (\w+)","I love china!")
print(result.group(1))
print(result.group(2))

#5.start和end方法给出起始和结束下标
print(result.start())
print(result.end())

#6.span方法给出范围元组
print(result.span())

#7.findall方法结合子组能高效率截取子串,匹配到的字符串中只选取子组中的数据作为列表元素
#使用在之前的抓取任务中
list=re.findall('<img src="([^"]*\.png)"','saddaf<img src="https://www.baidu.com/img/bd_logo1.png">ghgdhghg<br>saddaf<img src="https://www.baidu.com/img/bd_logo1.png">ghgdhghg<br>')
print(list)
#执行下载
for eachUrl in list:
	filename = eachUrl.split("/")[-1]
	#根据\进行分割并把最后的一段作为文件名
	#下载
	urllib.request.urlretrieve(eachUrl,filename,None)

'''
8.ip地址在做正则表达式获取的时候如果用findall将和search有不一样的结果，在这里小括号被当做是内容的输出，所以考虑如何
解除小括号的这个作用。
'''
'''
	sdfsdfsdfsdf11.231.1111.234erwed22.3.123.45dseeee3ra
	匹配到ip地址出来
	(\d{2}|1\d{2}|2[0-5][0-5]\.){3}(\d{2}|1\d{2}|2[0-5][0-5])
	
'''
print('==================ip==================')
pos=re.findall(r'((\d{1,2}|1\d{2}|2[0-5][0-5])\.){3}(\d{1,2}|1\d{2}|2[0-5][0-5])','sdfsdfsdfsdf11.231.1111.234erwed22.3.123.45dseeee3ra')
print(pos)
#输出[('123.', '123', '45')],考虑让findall方法不自作聪明地把小括号内容当做子组,左括号+ ?:
print('==================ip==================')
pos=re.findall(r'(?:(?:\d{1,2}|1\d{2}|2[0-5][0-5])\.){3}(?:\d{1,2}|1\d{2}|2[0-5][0-5])','sdfsdfsdfsdf11.231.1111.234erwed22.3.123.45dseeee3ra')
print(pos)

#9. finditer()将搜索结果变成迭代器，按照迭代器方式访问即可
iter=re.finditer(r"(\w+) (\w+)","I love china!")


s='''

'''

if re.match(r'^[\s]+$',s):
	print("ok")

