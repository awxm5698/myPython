#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket

c = socket.socket()
host = socket.gethostname()
port = 12345

c.connect((host, port))
while True:
    msg = 'welcome to here'
    c.send(msg.encode('utf-8'))
    data = c.recv(1024)
    print('recv: {}'.format(data.decode()))
    # c.close()

