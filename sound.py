#!/usr/bin/python2
# coding:utf-8
from pygame import mixer
import time
file = 'redbean.mp3'
mixer.init()
track = mixer.music.load(file)
mixer.music.play()
time.sleep(10)
mixer.music.stop(start=10)
