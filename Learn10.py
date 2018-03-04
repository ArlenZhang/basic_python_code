"""
对文件的基本操作练习：
    对文件file1内容进行分割和存储，提取我说的话和三个模块话
"""
file = open('../data/file_op/file1.txt')
resultIndex = 0
writeFile1 = open('../data/file_op/result1.txt', 'a')
writeFile2 = open('../data/file_op/result2.txt', 'a')
writeFile3 = open('../data/file_op/result3.txt', 'a')
writeFile4 = open('../data/file_op/result4.txt', 'a')
writeObj = [writeFile1, writeFile2, writeFile3, writeFile4]
for line in file:
    if line[:4] != "====":
        writeObj[resultIndex].write(line)
        if line[:5] == "arlen":
            writeObj[3].write(line)
    else:
        resultIndex += 1
        writeObj[resultIndex].write(line)
file.close()
writeFile1.close()
writeFile2.close()
writeFile3.close()
writeFile4.close()
