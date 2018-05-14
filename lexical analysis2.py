# coding:utf-8
# ! /usr/bin/python3
# 输出结果格式正确，但是还不能识别错误数字如018
import re

ops = [r'\+\+', '--', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', '%', '!', '&&', r'\|\|', '=', '>', '<']
seps = [r',', r':', r';', r'\(', r'\)', r'{', r'}']
consts = [r'\".+?\"', r'\'.\'', r'-?0x[A-Fa-f0-9]+|-?0[0-7]+|0|-?[1-9]\d*']
kws = ['int', 'char', 'void', 'if', 'else', 'switch', 'case', 'default', 'while', 'do', 'for', 'break', 'continue',
       'return']
id_pattern = r'[A-Za-z_]\w*'
ids = ['str', 'ch', 'num', 'kw_int', 'kw_char', 'kw_void', 'kw_if', 'kw_else', 'kw_switch', 'kw_case', 'kw_default',
       'kw_while', 'kw_do', 'kw_for', 'kw_break', 'kw_continue', 'kw_return', 'inc', 'dec', 'ge', 'le', 'equ', 'nequ',
       'add', 'sub', 'mul', 'div', 'mod', 'not', 'and', 'or', 'assign', 'gt', 'lt', 'comma', 'colon', 'simcon',
       'lparen', 'rparen', 'lbrac', 'rbrac', 'id', 'unknow']
# ids=consts+kws+ops+seps + id_pattern + unknow
ans = []
err = []

file = open('file')
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
for idx, pattern in enumerate(seps):  # 匹配运算符
    ret = re.findall(pattern, line)
    if ret:
        for item in ret:
            ans.append('(%s, %s)' % (ids[idx+absolute], item))
            line = re.sub(item, ' ', line)

absolute = len(consts)
for idx, pattern in enumerate(kws):  # 匹配运算符
    ret = re.findall(pattern, line)
    if ret:
        for item in ret:
            ans.append('(%s, %s)' % (ids[idx+absolute], item))
            line = re.sub(item, ' ', line)

# 匹配完关键字，再匹配标识符
ret = re.findall(id_pattern, line)
if ret:
    for item in ret:
        ans.append('(%s, %s)' % ('id', item))
        line = re.sub(item, ' ', line)

if not line.isspace():  # 确定最后的line不是空格组成的字符串
    unknow = re.split(r' +', line.rstrip().lstrip())  # 去掉左右的空格后以空格分隔，剩下的就是无法解析的词
    for item in unknow:
        err.append(item)

for item in ans:
    print(item)
for item in err:
    print('Error, there are unknown words: %s' % item)
