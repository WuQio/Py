#!/usr/bin/python3
from socket import *
from time import sleep


def main():
    # ip = "127.0.0.1"
    # ip = "101.132.124.124"
    ip = "www.mixue.ink"
    port = 1509
    bufsiz = 1024 * 20
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect((ip, port))
    ret = tcpCliSock.recv(bufsiz).decode()
    issue = []
    for i in ret.split('\n'):
        issue.append(i)
    for i in issue[:10]:
        print(eval(i)["question"])


if __name__ == '__main__':
    while 1:
        main()
        print('\n')
        sleep(2)
