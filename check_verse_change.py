#!/usr/bin/python3
# coding:utf-8

import time
import requests
from bs4 import BeautifulSoup
import re
import zmail

url = "http://www.hdchurch.org/devotional/weekly-verse?page=1"


def main():
    verse = get_verse()
    server = zmail.server("896834344@qq.com", "gkyommydyiozbbec")
    subject = {
        "subject": "金句",
        "content": verse
    }
    server.send_mail("896834344@qq.com", subject)


def get_verse():
    ret = requests.get(url=url)
    html = ret.content.decode()
    soup = BeautifulSoup(html, "html5lib")
    content = soup.find_all("div", attrs={"class", "footer-verse"})[-1]
    lst = re.split("<.*?div.*?>", content.__str__())
    verse = "".join(lst)
    return verse


if __name__ == '__main__':
    while 1:
        hour = time.localtime(time.time())[3]
        if hour == 23 or hour == 1:
            main()
        time.sleep(3600)
