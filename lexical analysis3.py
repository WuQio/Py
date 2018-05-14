# coding:utf-8
# ! /usr/bin/python3
# 可以识别如018的错误数字，视为error
import re

ops = [r'\+\+', '--', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', '%', '!', '&&', r'\|\|', '=', '>', '<']
seps = [r',', r':', r';', r'\(', r'\)', r'{', r'}']
consts = [r'\".+?\"', r'\'.\'']
num = r'-?0x[A-Fa-f0-9]+|-?0[0-7]+|0|-?[1-9]\d*'
kws = ['int', 'char', 'void', 'if', 'else', 'switch', 'case', 'default', 'while', 'do', 'for', 'break', 'continue',
       'return']
id_pattern = r'[A-Za-z_]\w*'
ids = ['str', 'ch', 'kw_int', 'kw_char', 'kw_void', 'kw_if', 'kw_else', 'kw_switch', 'kw_case', 'kw_default',
       'kw_while', 'kw_do', 'kw_for', 'kw_break', 'kw_continue', 'kw_return', 'inc', 'dec', 'ge', 'le', 'equ', 'nequ',
       'add', 'sub', 'mul', 'div', 'mod', 'not', 'and', 'or', 'assign', 'gt', 'lt', 'comma', 'colon', 'simcon',
       'lparen', 'rparen', 'lbrac', 'rbrac', 'id', 'unknow']
# ids=consts+kws+ops+seps + id_pattern + unknow
ans = []
err = []

file = open('file1')
line = file.read()
file.close()
line = line.replace('\n', ' ')
# print(line)

for idx, pattern in enumerate(consts):  # 匹配常量
    ret = re.findall(pattern, line)
    if ret:  # 返回非空list 某个常量模式匹配到的所有结果
        for item in ret:
            ans.append('(%s, %s)' % (ids[idx], item))
            line = re.sub(item, ' ', line)  # 将匹配到的子串用空格替换，以进行下一次匹配

absolute = len(consts) + len(kws)  # ids内运算符的起始索引
for idx, pattern in enumerate(ops):  # 匹配运算符
    ret = re.findall(pattern, line)
    if ret:
        for item in ret:
            ans.append('(%s, %s)' % (ids[idx+absolute], item))
            line = line.replace(item, ' ')

absolute += len(ops)  # ids内分隔符的起始索引
for idx, pattern in enumerate(seps):
    ret = re.findall(pattern, line)
    if ret:
        for item in ret:
            ans.append('(%s, %s)' % (ids[idx+absolute], item))
            line = re.sub(item, ' ', line)

absolute = len(consts)
for idx, pattern in enumerate(kws):
    ret = re.findall(pattern, line)
    if ret:
        for item in ret:
            ans.append('(%s, %s)' % (ids[idx+absolute], item))
            line = re.sub(item, ' ', line)

# 剩余数字、标识符、不能识别的模式
ret = re.split(r' +', line.rstrip().lstrip())  # 返回由空格分隔的词组成的list
for idx, item in enumerate(ret):
    mat = re.match(num, item)
    if mat is not None and mat.group() == item:
        ans.append('(num, %s)' % item)
        continue
    mat = re.match(id_pattern, item)
    if mat is not None and mat.group() == item:
        ans.append('(%s, %s)' % ('id', item))
        continue
    err.append(item)

for item in ans:
    print(item)
for item in err:
    print('Error, there is a unknown word: %s' % item)

