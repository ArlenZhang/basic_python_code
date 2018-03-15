# -*- coding: utf-8 -*-
"""
    Created on Wed Oct 11 13:10:40 2017
    author: arlen
    爬取携程网用户评论数据，找到评论的规律
        我们在携程网http://hotels.ctrip.com/hotel/beijing1#ctm_ref=hod_hp_sb_lst前十家酒店的序号获取
        遍历这十个序号到：http://hotels.ctrip.com/hotel/dianping/(序号)_p(评论页)t0.html
        对三家酒店的前十条评论数据进行保存。
"""
import urllib.request
import re
import os
import pickle

# 检测表情符号函数
def check_emoji(eva_t):
    str_new = ""
    for content in eva_t:
        if u"\U0001F600" <= content <= u"\U0001F64F":
            continue
        elif u"\U0001F300" <= content <= u"\U0001F5FF":
            continue
        elif u"\U0001F680" <= content <= u"\U0001F6FF":
            continue
        elif u"\U0001F1E0" <= content <= u"\U0001F1FF":
            continue
        else:
            str_new += content
    return str_new

def do_fetch(hotel_num, file_dir):
    hotels_url = 'http://hotels.ctrip.com/hotel/beijing1#ctm_ref=hod_hp_sb_lst'
    req = urllib.request.Request(hotels_url)
    response = urllib.request.urlopen(req)

    htmlData = response.read().decode('utf-8')

    # 用正则表达式得到前十个酒店的序列号
    # <h2 class="hotel_name" data-id="375265"><a href="http://hotels.ctrip.com/hotel/375265.html?isFull=F#ctm_ref=hod_sr_lst_dl_n_1_1" data-dopost="T" data-ctm="#ctm_ref=hod_sr_lst_dl_n_1_1" tracekey="nhtllistroomclick" tracevalue="clicktype=htlname;hotelid=375265;roomid=;isdefaultdisplay=;defaultdisplaypos=;htlpos=1;rompos=;" target="_blank" title="北京京都信苑饭店" tracekey1="" tracevalue1=""><span class="hotel_num">1</span>北京京都信苑饭店</a></h2>
    seqList = re.findall(r'<h2 class="hotel_name" data-id="(\d*)">', htmlData)
    # 遍历序号访问评论区
    evaluation_list = list()
    # 训练数据
    test_list = list()
    count = 0
    for seq in seqList:
        if count == hotel_num:
            break
        count += 1
        baseEvaUrl = 'http://hotels.ctrip.com/hotel/dianping/' + str(seq) + '_p'
        # 每个酒店遍历前十个页面的所有评论
        for i in range(10):
            tempEvaUrl = baseEvaUrl + str(i + 1) + 't0.html'
            response = urllib.request.urlopen(tempEvaUrl)
            pageData = response.read().decode('utf-8')
            # 用评论的正则表达公式获取用户评论区内容
            findEvaList = re.findall(r"<div class='J_commentDetail'>([^(</div>)]*)</div>", pageData)
            if count < hotel_num-1:
                evaluation_list.extend(findEvaList)
            else:
                test_list.extend(findEvaList)

    # 评论内容存储，用pickle泡菜同时存储在txt文件中
    count = 1
    with open(os.path.join(file_dir, "eva_text.txt"), 'a') as file_obj:
        for eva in evaluation_list:
            try:
                file_obj.write(eva + "\n")
            except Exception:
                # 符号检测和字符串重建
                eva = check_emoji(eva)
                file_obj.write(eva + "\n")
            count += 1

    with open(os.path.join(file_dir, "eva.pkl"), 'wb') as pkl_obj:
        pickle.dump(evaluation_list, pkl_obj)

    with open(os.path.join(file_dir, "test.pkl"), 'wb') as pkl_obj:
        pickle.dump(test_list, pkl_obj)
