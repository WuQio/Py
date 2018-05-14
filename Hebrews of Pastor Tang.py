# coding:utf-8
from urllib import request

static = 32896
url = "https://www.fuyin.tv/content/download/movid/654/urlid/"


for i in range(46, 158):
    request.urlretrieve(url + str(static + i), r"E:\Hebrews\%s.mp4" % (i + 1))
    print(i, 'Downloaded!')
