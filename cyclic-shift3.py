#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import datetime

# use recursion method
l = []
i = 2
n = 8


def recursion(lst, left_sub_len):
    # print 'in recursion, lst ==', lst, 'left ==', left_sub_len, 'l ==', l
    if len(lst) == 2 * left_sub_len:
        lst[0:left_sub_len], lst[left_sub_len:len(lst)] = lst[left_sub_len:len(lst)], lst[0:left_sub_len]
        print lst[0:left_sub_len], lst[left_sub_len:len(lst)], 'exchanged, and recursion over, l ==', l
        return
    elif len(lst) < 2 * left_sub_len:  # left_sub is longer
        lst[0:len(lst)-left_sub_len], lst[left_sub_len:len(lst)] = lst[left_sub_len:len(lst)], lst[0:len(lst)-left_sub_len]
        print lst[0:len(lst)-left_sub_len], lst[left_sub_len:len(lst)], 'exchanged, l ==', l
        return recursion(lst[len(lst)-left_sub_len:len(lst)], 2*left_sub_len-len(lst))
    else:  # left_sub is shorter
        # print 'left_sub is shorter'
        lst[0:left_sub_len], lst[len(lst)-left_sub_len:len(lst)] = lst[len(lst)-left_sub_len:len(lst)], lst[0:left_sub_len]
        print lst[0:left_sub_len], lst[len(lst)-left_sub_len:len(lst)], 'exchanged, l ==', l
        return recursion(lst[0:len(lst)-left_sub_len], left_sub_len)

for tmp in range(n):
    l.append(tmp+1)
print l
recursion(l, i)
print l
