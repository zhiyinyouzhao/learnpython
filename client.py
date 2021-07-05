# -*- coding: utf-8 -*-
import socket
import sys

reload(sys)
sys.setdefaultencoding('utf8')

sk = socket.socket()

print ("准备开始连接服务器")
sk.connect(("127.0.0.1", 10086))

print ("服务器连接成功 ")

msg_bytes = sk.recv(1024)

s = msg_bytes.decode("utf-8")
print "客户端接收到的数据是:", s

sk.send("大哥，今天来的有点晚".encode("utf-8"))
