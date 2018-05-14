#!/usr/bin/python3
from random import sample
from socket import *
from threading import *


def main():
    with open("json", "rb") as file:
        issueStr = file.read()
        file.close()
    issueList = eval(issueStr.decode())
    print(len(issueList))
    Server(issueList)


def Server(issueList):
    ip = ""
    port = 1509
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind((ip, port))
    tcpSerSock.listen(1)

    while 1:
        ret = ""
        seq = sample([i for i in range(len(issueList))], 10)

        for s in seq:
            ret += str(issueList[s])
            ret += '\n'

        print("waiting for connection...")
        tcpCliSock, addr = tcpSerSock.accept()
        print("...connect from ", addr)
        tcpCliSock.send(ret.encode())
        tcpCliSock.close()
        print("...connection close")


if __name__ == '__main__':
    for i in range(20):
        new_thread = Thread(target=main())
        new_thread.start()

