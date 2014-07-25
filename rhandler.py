#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import os
import threading


def query_handler(file_path, addr, lock):
    if os.path.isfile(file_path) == True:
        addr = (addr[0], 5001)
        reqst_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        reqst_sock.connect(addr)
        reqst_sock.close()


# Make the socket. Equivalent to a file descriptor, this is a socket descriptor.

broad_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a broadcast addr and a common port across the application.

broad_sock.bind(('<broadcast>', 5000))

while True:
    (file_path, addr) = broad_sock.recvfrom(512)
    handler = threading.Thread(target=query_handler, args=(file_path, addr, lock))
    handler.start()

			
