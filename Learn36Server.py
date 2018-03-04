# -*- coding: utf-8 -*-
"""
    Created on Sat Oct  7 18:20:21 2017
    @author: arlen
    Desc:网络编程基础
        服务器端套接字和客户短套接字的使用，发送和监听消息。在创建一个套接字之后，让她等待链接，进行交互。
    一个套接字就是socket的一个实例，它的实例化需要3个参数：地址族、流、使用的协议。
        服务器端套接字使用bind方法之后再调用listen方法监听某个特定的地址。客户端套接字使用connect方法
    连接到服务器端的套接字，connect方法中使用的地址与服务器端的bind方法绑定的地址(host:port)一致。服务器端
    开始监听之后能调用accept方法接受客户端的连接请求，这时候该方法会阻塞（等待）直到客户端连接，并返回一个（
    client,address)的元组，client为客户端套接字。处理完这次连接之后，服务器端accept方法继续监听并处理新的
    连接。
        套接字有两个方法：send和recv用于传输数据，

        通信失败的原因，windows下的并发是多线程并发，而两个程序的运行是两个进程不能同时运行，在Linux上面则
    没有这个问题~~pass
"""
# 服务器端程序
import socket

# 创建服务器端套接字
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
# 调用listen监听客户端请求,参数代表允许的最大连接数
s.listen(5)
while True:
    print('阻塞状态')
    client, addr = s.accept()
    print("即将建立和客户端的连接: ", addr)
    send_data = client.recv(1024)  # 一次接收的数据，1024字节
    client.sendall(send_data)  # 发送到客户端,与客户端交互的函数
    client.close()
