"""
                pickle模块掌握
    将数据存储在文件里很容易，但是恢复数据难，python提供了pickle模块，我们用这个模块可以
将像集合、列表、字典、类的实例存储到文件中构成二进制结构的文件进行存储，易于恢复。

例：当共享数据量很大的时候，比如中国的若干城市信息存储，使用直接导入即可。
"""
import pickle
import json
import urllib.request
# 1.字典存储
myDict = {"a": "arlen", 2: "blue", "list": [1, 2, 3]}
pklFile = open("../data/pkl/myDict.pkl", 'wb')  # wb二进制写入形式打开
pickle.dump(myDict, pklFile)  # 将数据倒入该文件
pklFile.close()

# 2.数据恢复
pklFile = open("../data/pkl/myDict.pkl", 'rb')  # rb二进制读取形式打开
reviveDict = pickle.load(pklFile)
print(reviveDict)

# 3.用pickle结合中国天气网的接口设计天气查询系统，city已经做成泡菜
cityFile = open('../data/pkl/city_data.pkl', 'rb')
city = pickle.load(cityFile)
password = input("请输入城市名称：")
name1 = city[password]
print(name1)

File1 = urllib.request.urlopen('http://m.weather.com.cn/data/' + name1 + '.html')
weatherHTML = File1.read().decode('utf-8')
weatherJSON = json.JSONDecoder().decode(weatherHTML)
weatherInfo = weatherJSON['weatherinfo']
# 打印
print(weatherInfo)
