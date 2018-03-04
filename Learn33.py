from urllib.request import urlopen
html = urlopen(
    "www.baidu.com"
).read().decode('utf-8')  # chinese, decode the text
