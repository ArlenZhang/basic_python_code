"""
    模型训练和测试
    训练语言模型，用语言模型对句子进行分类，判断哪个属于酒店评论
"""
from code.work1.fetch_eval_data import *
from code.utils.ngram_model import *
from code.work1.update_data import *

if __name__ == "__main__":
    # 配置
    pages = 20
    file_dir = "../../data/work1"
    # 趴数据
    do_fetch(pages, file_dir)
    # update 当时写的，现在 看不出用处
    do_update(file_dir)
    sent1 = "酒店交通很方便，魔拜去的恭王府和故宫、北海、景山、天安门，坐地铁也很方便，但是看着床缦订的花梨木套房失望了，人没入住管家已帮我快递收好了"
    sent2 = "改革开放，是1978年12月十一届三中全会中国开始实行的对内改革、对外开放的政策，我们要高举这个旗帜，发展中国经济和建设中国特色社会主义。"
    model_t = ngram_model(file_dir)
    count1, p1 = model_t.eval(sent1)
    count2, p2 = model_t.eval(sent2)
    print("第一个句子的出现概率：", p1)
    print("第二个句子的出现概率：", p2)
    if p1 > p2:
        print(sent1)
    else:
        print(sent2)
