import urllib.request
'''
	urllib包结合了url和lib,我们掌握urllib.request模块
	urlopen(url,data) data参数没有写就是get,写了就变成post提交方式，我们构建有道词典
请求也这样做实现对返回数据的爬取。
'''

response=urllib.request.urlopen('http://www.baidu.com')
html=response.read()
html=html.decode('utf-8')#网页是utf-8，这时候对这个子串用该编码方式解码
print(html)

'''
	当然urlopen参数也可以是request对象，下面用这方式爬图片
'''
req=urllib.request.Request('http://placekitten.com/600/700')
response=urllib.request.urlopen(req)
print('====================================')
print(response.geturl())
print(response.info())
print(response.getcode())

catPic=response.read()
with open('E:\\学习材料\\Python\\files\\spider\\cat-600-700.jpg','wb') as f:
	f.write(catPic)