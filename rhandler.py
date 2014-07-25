#!/usr/bin/python

import socket
import os

#Make the socket. Equivalent to a file descriptor, this is a socket descriptor.
broad_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
reqst_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind the socket to a broadcast addr and a common port across the application.
broad_sock.bind(("<broadcast>", 5000))
while True:
	file_path, addr = broad_sock.recvfrom(512)
	if os.path.isfile(file_path) == True:
		addr = list(addr)
		addr[1] = 5001
		addr = tuple(addr)
		reqst_sock.connect(addr)
		reqst_sock.close()
	


