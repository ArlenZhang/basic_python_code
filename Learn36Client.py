# -*- coding: utf-8 -*-
"""
    Created on Sat Oct  7 19:03:53 2017

    @author: arlen
    客户机端程序
"""
import socket

s = socket.socket()  # 创建客户端套接字
print('即将建立连接...')
host = socket.gethostname()
port = 1234
print('即将建立连接...')
s.connect((host, port))  # 与服务器套接字绑定的一致

# 输入数据
cmd = input('please input :').encode()
s.sendall(cmd)

# 接收数据
data = s.recv(1024).decode()

# 获取服务端发来的数据
print('接收的数据：', data)
