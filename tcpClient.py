from socket import *
from threading import Lock, Thread


def job(i):
    host = 'www.wuqio.xin'
    host = "127.0.0.1"
    # host = "101.132.124.124"
    # host = "192.168.1.100"
    port = 80
    port = 1508
    addr = (host, port)
    bufsiz = 1024

    tcpSock = socket(AF_INET, SOCK_STREAM)
    tcpSock.connect(addr)
    print("...connected")

    # while True:
    #     data = input('> ')
    #     tcpSock.send(data.encode())
    #     if not data:
    #         print('data is None, break')
    #         break
    #     data = tcpSock.recv(bufsiz).decode()
    #     print(data)
    tcpSock.send((str(i)+'\n').encode())
    tcpSock.close()


if "__main__" == __name__:
    for i in range(10):
        new_thread = Thread(target=job, args=(i,))
        new_thread.start()