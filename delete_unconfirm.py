#!/usr/bin/python2
# coding:utf-8
from time import sleep, time, localtime, strftime
import os

path = "/opt/tomcat/RECORD_PATH/"


def main():
    filesl = os.listdir(path)
    for filename in filesl:
        if '.' not in filename:
            os.remove(path+filename)
            print(strftime('[%Y-%m-%d %H:%M:%S]\t', localtime(time()))+"remove file: "+path+filename)


if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print(e.message)
    sleep(60)
