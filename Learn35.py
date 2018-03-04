# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:04:48 2017
@author: arlen
Desc:基于pymysql的数据库编程基本
"""

import pymysql.cursors  # 游标概念

# 1. 数据库配置连接
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='jyb450816',
    db='pythontasks',
    charset='utf8'
)

# 2. 获取游标
cursor = connect.cursor()

# 插入数据
# sql = "INSERT INTO User (userName,userPWD,gender,age) VALUES ( '%s', '%s', '%s' ,'%d' )"
# data = ('arlen','123456','男',23)
# cursor.execute(sql % data)
# connect.commit()#提交执行
# print('成功插入', cursor.rowcount, '条数据')
# input("查看是否插入成功？")

# 修改数据
sql = "UPDATE User SET userPWD = %s WHERE userName = '%s' "
data = ('654321', 'arlen')
cursor.execute(sql % data)
connect.commit()
print('成功修改', cursor.rowcount, '条数据')
input("查看是否修改成功？")

# 查询数据
userID = 0
sql = "SELECT id,userName,userPWD,gender,age FROM User WHERE userName = '%s' "
data = ['arlen']
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("id:%d\tName:%s\tPWD:%s\tgender:%s\tage:%d" % row)
    userID = row[0]
print('共查找出', cursor.rowcount, '条数据')
result = input("是否删除该用户？(y/n)")

# 删除数据
if result == 'y':
    sql = "DELETE FROM User WHERE userName = '%s' LIMIT %d"
    data = ('arlen', 1)
    cursor.execute(sql % data)
    connect.commit()
    print('成功删除', cursor.rowcount, '条数据')

# ===================重点掌握-事务处理====================
sql_1 = "UPDATE Transaction SET saving = saving + 1000 WHERE userID =" + str(userID)
sql_2 = "UPDATE Transaction SET expend = expend + 1000 WHERE userID =" + str(userID)
sql_3 = "UPDATE Transaction SET income = income + 2000 WHERE userID =" + str(userID)
print(sql_1)
'''
    银行在这里的计算方式：存储=收入-支出
    这里的计算流程，先是收入增加2000，花了1000块还剩1000存在银行。。
'''

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    # 设置系统故障
    wrong = 2 / 0
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    connect.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    connect.commit()  # 事务提交，不提交的都可以执行回滚~
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
connect.close()
