# coding:utf-8
# !/usr/bin/python3
x = "abcc"
y = "abcd"
l = []


def LCS(x, y, i, j):
    global l
    l.append((i, j))
    if i == 0 or j == 0:
        return 0
    if x[i - 1] == y[j - 1]:
        return LCS(x, y, i - 1, j - 1) + 1
    else:
        return max(LCS(x, y, i - 1, j), LCS(x, y, i, j - 1))


ret = LCS(x, y, len(x), len(y))
print(ret)
