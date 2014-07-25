#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

if len(sys.argv) < 2:
    print 'Command line IP argument required.'
    sys.exit()

# Make the socket. Equivalent to a file descriptor, this is a socket descriptor.

broad_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
reqst_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the UDP socket to a broadcast addr and a common port across the application.
# broad_sock.bind(("<broadcast>", 5000))
# Bind the TCP socket to an addr and a common port across the application.

reqst_sock.bind((sys.argv[1], 5001))

# TCP socket must listen to maximum of 5 connections.

reqst_sock.listen(5)

# For broadcasting, this socket must be initialized as a broadcast socket.

broad_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Get complete file path

file_path = raw_input('Enter file name to search over the LAN: ')

# Broadcast this file path over the LAN using the socket broad_sock

broad_sock.sendto(file_path, ('<broadcast>', 5000))

print 'List of computers having the file'
while True:
    (c, addr) = reqst_sock.accept()
    print addr
    c.close()
broad_sock.close()
reqst_sock.close()

			
