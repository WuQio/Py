#!/usr/bin/python3
import datetime
import os
import shutil
import time

path = "/opt/tomcat/RECORD_PATH/"
unconfirm_path = "/opt/tomcat/UNCONFIRM/"
fmt = "%Y%m%d%H%M%S"


def main():
    filesl = os.listdir(path)
    for filename in filesl:
        if ("." not in filename) & (time.time() - getUnixTime(filename) > 86400):
            shutil.move(path + filename, unconfirm_path)


def getUnixTime(s):
    return time.mktime(datetime.datetime.strptime(s[0:-5], fmt).timetuple())


if __name__ == '__main__':
    while 1:
        try:
            main()
        except Exception as e:
            print(e)
        time.sleep(86400)
