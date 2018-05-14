#!/usr/bin/python2
# coding:utf-8

from dingtalkchatbot.chatbot import DingtalkChatbot
webhook = "https://oapi.dingtalk.com/robot/send?access_token=53dd6ead74feaa6a246e42b6f00979f2790e6f28f26748649f4fc668b5af4906"
xiaoding = DingtalkChatbot(webhook=webhook)
xiaoding.send_text(msg="大家好啊！", is_at_all=True)
