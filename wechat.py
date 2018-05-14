# coding:utf-8
import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return u'我已收到'+msg['Text']


itchat.auto_login()
itchat.run()
