# !/usr/bin/python3
# -*- coding:utf-8 -*-
import zmail
from requests import get
from bs4 import BeautifulSoup
import re
from time import sleep

sever = None


def main():
    global server
    server = zmail.server("896834344@qq.com", "gkyommydyiozbbec")
    url = "http://wap.xt.beescrm.com/base/electricityHd/queryResult/ele_id/7/community_id/57/building_id/287/floor_id/2096/room_id/36105/flag/1"
    ret = get(url=url)
    html = ret.content.decode()
    # print(html)
    soup = BeautifulSoup(html, "html5lib")
    content = str(soup.find(attrs={'class', "price"}))

    lst = re.split(r"<.*?span.*?>", content)
    balance = "".join(lst)

    low_balance = {
        "subject": "电费余额不足",
        "content": "电费余额不足，请充值。当前余额" + balance
    }
    balance_info = {
        "subject": "电费信息",
        "content": "电费余额："+balance
    }
    if float(balance[0:-1]) < 15:
        server.send_mail("896834344@qq.com", low_balance)
        server.send_mail("gan.shen@outlook.com", low_balance)
        server.send_mail("huxu1110@qq.com", low_balance)
    else:
        server.send_mail("896834344@qq.com", balance_info)
        server.send_mail("gan.shen@outlook.com", balance_info)
        server.send_mail("huxu1110@qq.com", balance_info)


if __name__ == '__main__':
    while 1:
        try:
            main()
        except Exception as e:
            server.send_mail("896834344@qq.com", "电费脚本抛出异常~~~\n"+str(e))
        sleep(86400)
