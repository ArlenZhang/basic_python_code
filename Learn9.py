"""
    python之文件操作

    r 默认只读、w 写入方式打开、x 若文件已经存在则打开异常、a 以追加方式打开、b 二进制打开
    t 文本格式打开、+ 可读写模式打开、U 通用换行符模式

    方法列举：close、read、readline、write、writelines、seek、tell
"""
# 1.打开文件并存入文件对象
fileObj = open('../data/file_op/file1.txt')
text = fileObj.read()  # read没参数就全部读取，read读到末尾，不关闭则无法再读
print(text)

# 2.移动read指针seek(offset,from)
#  参数数据 0:文件起始 1:当前 2:结尾 offset:偏移offset个字符
fileObj.seek(6, 0)

# 3.读取指定个数的字符
text = fileObj.read(5)
print(text)

# 4.当前read指针在哪
print(fileObj.tell())

# 5.按行读
lineStr = fileObj.readline()
print(lineStr)

print('========================================')
# 6.遍历每行
fileObj.seek(0, 0)
lines = list(fileObj)
for line in lines:
    print(line)

print('========================================')
# 7.更好的遍历方式
fileObj.seek(0, 0)
for line in fileObj:
    print(line + "<============")
fileObj.close()

# 8.写文件
fileObj = open('../data/file_op/file1.txt', 'a')  # append追加
list_w = ['zly', 'i help you.', 'where are you ?']
fileObj.writelines(list_w)
fileObj.close()
