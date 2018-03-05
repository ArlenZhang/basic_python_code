from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.cs.toronto.edu/~weifeng/software.html").read().decode("utf-8")
print(html)

# 定义soup来解析html代码
soup = BeautifulSoup(html, features='lxml')  # 有几种解析方式，这里可以选lxml解析方法

# 用对象和属性的方式获取html中的元素
# 例如:
