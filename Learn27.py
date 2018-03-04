"""
    有道词典数据爬取
"""
import urllib.parse
import json

content = input('请输入：')

# 有道翻译地址
url = 'http://fanyi.youdao.com/translate'
# 有的商业软件通过检测user-agent看是否是机器访问，因此要设置heads为认为访问值
head = dict()
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.' \
                     '115 Safari/537.36'
# 要查询的数据封装成数据包传给服务器
data = dict()
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'utf-8'
data['typoResult'] = 'true'
# 编码
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data, head)  # 将带数据访问，制定请求头信息到对应URL下
# 也可以通过req.add_header()方法追加head (key,value)

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)

print(target)

'''
    循环访问的时候会被检测-->使用代理
'''
url = 'http://www.whatismyip.com.tw'
proxy_support = urllib.request.ProxyHandler({'http': '144.255.14.123'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/59.0.3071.115 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
