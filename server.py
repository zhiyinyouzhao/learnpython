# -*- coding: utf-8 -*-

import socket
import sys
reload(sys)
sys.setdefaultencoding('utf8')


sk = socket.socket()

sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(("127.0.0.1", 10086))

sk.listen(10)

print ("准备等待客户端开始连接")
conn, address = sk.accept()
print ("客户端连接成功")

conn.send("你好啊，来了妹子".encode("utf-8"))

msg_bytes = conn.recv(1024)
print "111111"
print type(msg_bytes)
s = msg_bytes.decode("utf-8")
print "服务器接收到的数据是:",s
print type(s)
