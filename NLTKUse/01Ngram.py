'''
 本节掌握nltk包中对Ngram模型的基本使用
'''
import jieba
import nltk
from nltk import *
train_corpus = "测试数据库,用户支付表,支付金额,支付用户,测试数据库,用户支付表,支付金额,支付用户"
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

finder = BigramCollocationFinder.from_words(jieba.cut(train_corpus))
finder.apply_word_filter(lambda w: w.lower() in [',', '.', '，', '。'])
finder.nbest(bigram_measures.pmi, 10)

finder = TrigramCollocationFinder.from_words(jieba.cut(train_corpus))
finder.apply_word_filter(lambda w: w.lower() in [',', '.', '，', '。'])
finder.nbest(trigram_measures.pmi, 10)
