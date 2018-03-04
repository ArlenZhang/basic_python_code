# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 20:26:12 2017

@author: arlen

好玩的编程和灵活的编程思想:柔（灵活，预防，全面）
多进程
"""

import os
from multiprocessing import Pool
from multiprocessing import Process

print("进程(%s)开始运行..." % os.getpid())

pid = os.fork()  # 操作系统将当前进程复制，创建子进程
if pid == 0:
    print("子进程，父进程id为(%s %s)" % (os.getpid(), os.getppid()))
else:
    print('我刚刚创建了(%s %s)子进程' % (os.getpid(), pid))


# 更简单的方式
def run_proc_a(name):
    for item in range(1000):
        print("进程(%s)：" % name, item)


def run_proc_b(name):
    for item in range(1000):
        print("进程(%s)：" % name, item)


p_a = Process(target=run_proc_a, args=('test_a',))
p_b = Process(target=run_proc_b, args=('test_b',))
print("开辟两个进程并发执行。")
p_a.start()
# p_a.join()#等待子进程结束之后继续往下运行，用于进程间的同步
p_b.start()
p_b.join()
print("跑完所有任务！")

'''
    如果启用大量进程，使用进程池
'''


def must_work(name):
    print("进程(%s)正在完成必要配置。" % name)


pool = Pool()
# 批量开辟5个进程
