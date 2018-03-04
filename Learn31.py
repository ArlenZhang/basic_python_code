"""
    高级语言能检测异常处理错误
    爬虫过程中当我们访问的url没有反应的时候通常会返回一个urlerror异常，捕获异常并处理。

"""
import urllib.request
import urllib.error

req = urllib.request.Request('http://www.jb51.net/article/33')  # 抓不存在的网址数据
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:  # 小范围的异常错放在前面，不然不会执行小范围的异常处理程序
    print(e.code)
# print(e.read())

except urllib.error.URLError as e:
    print(e.reason)

# HTTPError是URLError的一个子类，返回值那几个，你懂的
