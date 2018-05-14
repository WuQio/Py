#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import datetime
# Cyclic shift, use for loop.
l = []
i = 2333
n = 100000
for tmp in range(n):
    l.append(tmp)
begin = datetime.now()
ll = l[0:i]
for tmp in range(n-i):
    l[tmp] = l[tmp+i]
for tmp in range(i):
    l[n-i+tmp] = ll[tmp]
end = datetime.now()
print 'it costs', end-begin, 'seconds.'
