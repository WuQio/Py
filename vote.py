# coding:utf-8
from urllib import request
from pytesser3 import image_file_to_string
url="http://60th.zafu.edu.cn/system/resource/survey/createsurveycheckimg.jsp?random="
for i in range(1, 100):
    request.urlretrieve(url, r"D:\pycharm-project\exercise\pic\%s.jpg" % i)

f = open(r"D:\pycharm-project\exercise\pic\code.txt", "w+")

for i in range(1, 100):
    try:
        code = image_file_to_string(r"D:\pycharm-project\exercise\pic\%s.jpg" % i)
        f.write(code)
    except UnicodeDecodeError:
        f.write('\n')
f.close()
