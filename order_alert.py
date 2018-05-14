#!/usr/bin/python2
# coding:utf-8
from dingtalkchatbot.chatbot import DingtalkChatbot
from time import sleep, time
import os

path = "/opt/tomcat/RECORD_PATH/"
filesl = os.listdir(path)
webhook = "https://oapi.dingtalk.com/robot/send?access_token=53dd6ead74feaa6a246e42b6f00979f2790e6f28f26748649f4fc668b5af4906"


def send2WQ(msg):
    DingtalkChatbot(webhook).send_text(msg=msg, at_mobiles=['18100174475'])


def send2all(msg):
    DingtalkChatbot(webhook).send_text(msg=msg, is_at_all=True)


def main():
    for filename in filesl:
        if filename.find(".") < 0:
            try:
                os.remove(path + filename)
            except Exception, e:
                send2WQ(e.message)
        if filename.find(".asyncConfirm") > 0:
            try:
                os.rename(path + filename, path + filename.split(".")[0] + ".read")
                filename = filename.split(".")[0] + ".read"
                with open(path + filename) as f:
                    fileContent = f.read()
                msg = "客户已下单，外部订单号：" + filename.split(".")[0] + "\n" + "订单信息" + fileContent
                send2all(msg)
            except Exception, e:
                send2WQ("脚本 " + __file__ + " 抛出异常，异常信息：" + e.message)


record_point = 0
if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        if time() - record_point > 86400:
            send2WQ("脚本 " + __file__ + " 抛出异常，异常信息：" + e.message)
            record_point = time()
    sleep(10 * 60)
