#!/usr/bin/python2
# coding:utf-8
import os, shutil
from time import sleep, time, localtime, strftime
path = "/opt/tomcat/RECORD_PATH/"
movepath = "/opt/tomcat/CANCEL/"


def main():
    files_l = os.listdir(path)
    for filename in files_l:
        if '.cancel' in filename:
            shutil.move(path+filename, movepath+filename)
            print(strftime('[%Y-%m-%d %H:%M:%S]\t', localtime(time())) + "move cancel file: " + filename)


if __name__ == '__main__':
    while 1:
        try:
            main()
        except Exception, e:
            print(e)
        sleep(60)
