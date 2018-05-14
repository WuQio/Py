#!/usr/bin/python3
# coding:utf-8
from pywifi import *
import time


def main():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(1)
    scanres = iface.scan_results()

    profile = Profile()

    for s in scanres:
        if s.ssid == 'meilan':
            profile.ssid = s.ssid
            profile.auth = s.auth
            profile.akm.append(s.akm[0])
            profile.cipher = s.cipher
            break
    key = 'abcdefgg'
    profile.key = key
    profile = iface.add_network_profile(profile)
    iface.remove_all_network_profiles()
    iface.connect(profile)
    time.sleep(30)
    print(iface.status())

main()
