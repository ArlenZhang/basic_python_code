'''
    对现行支持向量分类的fit与predict

'''
from sklearn.svm import LinearSVC
clf = LinearSVC(C=1.0, penalty='l1',loss='squared_hinge', dual=False, tol=1e-7)
datas=[[1],[-1],[3]] #每个元素包括一个数字向量代表样本特征
labels=['people','animal','people']#每个元素包括一个向量，代表元素的对应标签，可以是字符串或者是数字向量
clf.fit(datas,labels)
result=clf.predict(8)
print('result: ',result)
