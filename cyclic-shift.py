#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import datetime
# Use Python built_in method
l = []
i = 23333
n = 100000
for tmp in range(n):
    l.append(tmp)
begin = datetime.now()
new_l = (l[0:i][::-1]+l[i:n][::-1])[::-1]
end = datetime.now()
print 'it costs', end-begin, 'seconds.'
