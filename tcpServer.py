#!/usr/bin/python3
from socket import *
from threading import Lock, Thread


def job():
    global lock
    host = ''
    port = 1508
    bufsiz = 1024
    addr = (host, port)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(addr)
    tcpSerSock.listen(20)

    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...conntected from:', addr)

        while True:
            try:
                data = tcpCliSock.recv(bufsiz)
            except ConnectionResetError:
                data = b""

            data = data.decode()
            lock.acquire()
            with open("recv.txt", "a") as file:
                file.write(data)
            file.close()
            lock.release()
            if not data:
                break

        tcpCliSock.close()
        print("connection close...\n\n")

    tcpSerSock.close()


if "__main__" == __name__:
    lock = Lock()
    for i in range(20):
        new_thread = Thread(target=job())
        new_thread.start()
