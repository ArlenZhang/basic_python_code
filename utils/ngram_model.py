# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:36:40 2017
@author: arlen
Ngram模型的Python程序构建：
    构建模型用酒店评论数据训练该模型，用随机话语检测该语句是否属于酒店评论类型的句子。
    熟悉苏州大学集群使用，链接节点开发程序
    fiddler
    本程序实现Ngram的python基本实现，bigram以及文本距离计算
    极大似然估计的推导结果：P(x|y)=P(x,y)/p(y)=count(x,y)/count(y)
"""
import pickle
import os


class ngram_model:
    def __init__(self, file_dir):
        self.bigram_list = None
        self.trigram_list = None
        self.pkl_file = open(os.path.join(file_dir, "eva.pkl"), 'rb')  # rb二进制读取形式打开
        self.str_list = pickle.load(self.pkl_file)
        self.pkl_file = open(os.path.join(file_dir, "test.pkl"), 'rb')  # rb二进制读取形式打开
        self.test_list = pickle.load(self.pkl_file)

    # 距离计算函数
    def compute_distence(self, str_a, str_b):
        dist = 0
        print(str_a, str_b)
        return dist

    # 对字符串的二位切割
    def get_bi_sublist(self, str_in):
        result_list = list()
        for i in range(len(str_in) - 2):
            result_list.append(str_in[i:i + 2])
        return result_list

    # 对字符串的三位切割
    def get_tri_sublist(self, str_in):
        result_list = list()
        for i in range(len(str_in) - 3):
            result_list.append(str_in[i:i + 3])
        return result_list

    # Bigram概率模型构建，用字符串列表训练模型
    def create_bigram(self, str_list_t):
        result_list = list()
        for strTemp in str_list_t:
            result_list.extend(self.get_bi_sublist(strTemp))
        return result_list

    def create_trigram(self, str_list_t):
        result_list = list()
        for strTemp in str_list_t:
            result_list.extend(self.get_tri_sublist(strTemp))
        return result_list

    # 根据最大似然估计的类似观点，出现次数多越是符合段落类型
    def count_single(self, str_t, str_list_t):
        count = 0
        for tempStr in str_list_t:
            for i in tempStr:
                if i == str_t:
                    count += 1
        return count

    def count_exist(self, str_t, bigram_list_t):
        count = 0
        for item in bigram_list_t:
            if item == str_t:
                count += 1
        return count

    def count_tri_exist(self, str_t, trigram_list_t):
        count = 0
        for item in trigram_list_t:
            if item == str_t:
                count += 1
        return count

    # 计算Bigram概率函数
    def bigram_test(self, str_c, bigram_list_t):
        # 为每个词对应计数器
        test_list = self.get_bi_sublist(str_c)
        count = 0
        '''算法思路：涉及遍历的时候我们让总量小的多次遍历，让总量多的一次遍历？未必'''
        for strT in test_list:
            count += self.count_exist(strT, bigram_list_t)
        return count

    # 计算句子出现的概率
    def probability_comp(self, str_test, bigram_list_t, trigram_list_t, str_list_t):
        probability = 1
        # 计算count(wiw(i+1)w(i+2)) count(wiw(i+1))
        bi_list = self.get_bi_sublist(str_test)
        tri_list = self.get_tri_sublist(str_test)
        # 计数三位
        index = 0
        # 这是从第三位的概率算起
        for strT in tri_list:
            tri_count = self.count_tri_exist(strT, trigram_list_t)
            str_bi = bi_list[index]
            index += 1
            bi_count = self.count_exist(str_bi, bigram_list_t)
            print(str_bi, '---', strT, "\n")
            # 得到p(wi|w(i-1)(i-2)) -> count(w(i-2)w(i-1)wi/w(i-2)w(i-1))，当前i从3开始
            if bi_count != 0 and tri_count != 0:
                probability *= tri_count / bi_count
        # 计算p(w2|w1)->count(w1w2)/count(w1)
        w1w2 = str_test[0:2]
        w1 = str_test[0]
        count1_t = self.count_exist(w1w2, bigram_list_t)
        count2_t = self.count_single(w1, str_list_t)
        if count1_t != 0 and count2_t != 0:
            probability *= (count1_t / count2_t)
        probability = 0 if probability == 1 else probability
        return probability

    def train(self):
        # 模型训练
        self.bigram_list = self.create_bigram(self.str_list)
        self.trigram_list = self.create_trigram(self.str_list)

    """
        提供数据所在路径用于训练模型
        提供用于计算概率的句子
        返回句子的概率
    """

    def eval(self, sent):
        # 如果不为空则不驯连
        if self.bigram_list is None or self.trigram_list is None:
            print("训练")
            self.train()
        count = self.bigram_test(sent, self.bigram_list)
        p = self.probability_comp(sent, self.bigram_list, self.trigram_list, self.str_list)
        return count, p

    def eval_all(self):
        # 如果不为空则不驯连
        if self.bigram_list is None or self.trigram_list is None:
            print("训练")
            self.train()
        c_list = list()
        p_list = list()
        for sent in self.test_list:
            count = self.bigram_test(sent, self.bigram_list)
            p = self.probability_comp(sent, self.bigram_list, self.trigram_list, self.str_list)
            c_list.append(count)
            p_list.append(p)
        return c_list, p_list


if __name__ == "__main__":
    sent1 = "酒店交通很方便，魔拜去的恭王府和故宫、北海、景山、天安门，坐地铁也很方便，但是看着床缦订的花梨木套房失望了，人没入住管家已帮我快递收好了"
    sent2 = "改革开放，是1978年12月十一届三中全会中国开始实行的对内改革、对外开放的政策，我们要高举这个旗帜，发展中国经济和建设中国特色社会主义。"
    model = ngram_model("../../data/work1/eva.pkl")
    count1, p1 = model.eval(sent1)
    count2, p2 = model.eval(sent2)
    print("第一个句子的出现概率：", p1)
    print("第二个句子的出现概率：", p2)
    if p1 > p2:
        print(sent1)
    else:
        print(sent2)
