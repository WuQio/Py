#!/usr/bin/python3
# coding:utf-8
import pywifi
import sys
import time
from pywifi import const


def bies():
    wifi = pywifi.PyWiFi()  # 创建一个无限对象
    ifaces = wifi.interfaces()[0]  # 取一个无限网卡
    ifaces.scan()  # 扫描
    bessis = ifaces.scan_results()
    for data in bessis:
        print(data.ssid)  # 输出wifi名称


bies()
