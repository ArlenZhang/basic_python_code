'''
	工具
	'1 戴相龙 _ NR _ _ 2 VMOD _ _ '
	对上面的字符串匹配
'''
import re
fileObj=open('E:\\学习材料\\Python\\files\\data.txt' , encoding='UTF-8')
text=fileObj.read()
resultList=re.findall(r'\d* \w* _ \w* _ _ \d* \w* _ _ ',text)

#写入
fileObj=open('E:\\学习材料\\Python\\files\\dict1.txt','w')

for result in resultList :
    fileObj.write(result+'\n')
fileObj.close()