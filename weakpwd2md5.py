#!/usr/bin/python3
import hashlib

filename = "weakpwd.csv"
newFileName = "strongpwd.csv"
newFile = open(newFileName, "w")
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        mingw = line.split(",")[0][1:-1]
        print(mingw)
        m2 = hashlib.md5()
        m2.update(mingw.encode("utf-8"))
        miw = m2.hexdigest()
        newFile.write(mingw+","+miw+"\n")
newFile.close()

