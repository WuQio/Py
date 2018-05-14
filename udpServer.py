#!/usr/bin/python3

from socket import *
from time import ctime

host = ''
port = 21567
bufsiz = 1024
addr = (host, port)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(addr)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(bufsiz)
    udpSerSock.sendto(('['+ctime()+'] '+data.decode()).encode(), addr)
    print('received from and returned to:', addr)

udpSerSock.close()