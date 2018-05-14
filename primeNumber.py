#!/usr/bin/python3
# coding:utf-8
from math import sqrt


def judge(x):
    if (x == 2) | (x == 3):
        return True
    i = 2
    while i <= sqrt(x):
        if x % i == 0:
            return False
        i += 1
    return True


def main():
    num = 2488512967
    file = open("primeNumber", "w")
    while 1:
        if judge(num):
            file.seek(0)
            file.write(str(num) + '\n')
        num += 1


if "__main__" == __name__:
    main()

