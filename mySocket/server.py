#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    conn, addr = s.accept()
    print('address: {}'.format(addr))
    # conn.send('welcome to here!')

    data = conn.recv(1024)
    conn.send(data.upper())
conn.close()