"""
    模型训练和测试
    训练语言模型，用语言模型对句子进行分类，判断哪个属于酒店评论
"""
from code.work1.fetch_eval_data import *
from code.utils.ngram_model import *
from code.work1.update_data import *
import numpy as np

if __name__ == "__main__":
    # 配置
    hotel_num = 4
    file_dir = "../../data/work1"
    # 趴数据
    # do_fetch(hotel_num, file_dir)
    # update 当时写的，现在 看不出用处
    # do_update(file_dir)
    model_t = ngram_model(file_dir)

    # 对测试句子集合的概率计算
    count_list, p_list = model_t.eval_all()
    p_list = np.array(p_list)
    mean_p = np.mean(p_list)
    print("概率列表: ", p_list)
    print("句子群的平均概率：", mean_p)

    # 单个句子测试
    sent = "参加机器学习国际会议，从中学到很多算法和思想。"
    count, p = model_t.eval(sent)
    print("外部句子出现概率：", p)

