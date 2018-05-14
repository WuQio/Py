#!/usr/bin python3
import threading


def job(num):
    global lock
    lock.acquire()
    with open("file5", "a") as file:
        file.write(str(num))
        file.write('\n')
    file.close()
    lock.release()


if '__main__' == __name__:
    lock = threading.Lock()
    for i in range(10):
        new_thread = threading.Thread(target=job, args=(i,))
        new_thread.start()