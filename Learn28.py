"""
问题分析：
    新建存储文件夹
    访问的页面网址存在规律：http://jandan.net/ooxx/page-145#comments 之间数字部分
    跳转网页不货源代码并找到图片链接 <img src='xxx.jpg'
    145-145+number-1这number张图片连接搜索提取
"""
import os
import urllib.request

def download_pic(folder, pages=2):
    # 1. 新建文件夹
    # os.mkdir(folder)
    os.chdir(folder)  # 工作目录切换进去

    # 2.访问指定数量的页面
    count = 0
    while count < pages:
        page_url = 'http://jandan.net/ooxx/page-' + str(145 + count) + '#comments'
        # 访问页面并返回该页面中的一组图片链接
        pic_list = []
        pic_list += visit_page(page_url)
        # print(picList)
        # 根据链接下载图片保存
        save_pic(pic_list)
        count += 1

# 根据链接返回数据
def visit_url(url,  type_t):
    url = 'http:' + url
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/59.0.3071.115 Safari/537.36')
    response = urllib.request.urlopen(url)
    if type_t == 1:
        data = response.read().decode('utf-8')  # 图片不能够用utf-8解码
    else:
        data = response.read()
    return data


# visitPage访问页面
def visit_page(page_url):
    content = visit_url(page_url, 1)
    link_list = []
    a = content.find('img src=')
    while a != -1:
        b = content.find('.jpg', a, a + 255)
        if b != -1:
            link_list.append(content[a + 9:b + 4])
        else:
            b = a + 9
        a = content.find('img src=', b)
    return link_list


# 图片下载
def save_pic(pic_list):
    for pLink in pic_list:
        data = visit_url(pLink, 2)
        filename = pLink.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(data)


# 执行
download_pic('../data/pictures/web_crawler', 2)
