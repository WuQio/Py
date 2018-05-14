#!/usr/bin/python3

from socket import *

host = 'TXCloud'
port = 21567
bufsiz = 1024
addr = (host, port)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode(), addr)
    data, addr = udpCliSock.recvfrom(bufsiz)
    if not data:
        break
    print(data.decode())

udpCliSock.close()
