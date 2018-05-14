# coding:utf-8
# !/usr/bin/python3
# 错误理解要求的输出
import re

ops = [r'\+\+', '--', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', '%', '!', '&&', r'\|\|', '=', '>', '<']
seps = [r',', r':', r';', r'\(', r'\)', r'{', r'}']
consts = [r'\".+?\"', r'\'.\'', r'0\.\d+|-?[1-9]\d*\.\d+|0|-?[1-9]\d*']
kws = ['int', 'char', 'void', 'if', 'else', 'switch', 'case', 'default', 'while', 'do', 'for', 'break', 'continue',
       'return']
id_pattern = r'[A-Za-z_]\w*'  # ids=consts+kws+ops+seps + id_pattern + unknow
ids = ['str', 'ch', 'num', 'kw_int', 'kw_char', 'kw_void', 'kw_if', 'kw_else', 'kw_switch', 'kw_case', 'kw_default',
       'kw_while', 'kw_do', 'kw_for', 'kw_break', 'kw_continue', 'kw_return', 'inc', 'dec', 'ge', 'le', 'equ', 'nequ',
       'add', 'sub', 'mul', 'div', 'mod', 'not', 'and', 'or', 'assign', 'gt', 'lt', 'comma', 'colon', 'simcon',
       'lparen', 'rparen', 'lbrac', 'rbrac', 'id', 'unknow']

ans = dict(zip(ids, [0] * len(ids)))


def my_filter(absolute, iter, line):
    for idx, pattern in enumerate(iter):
        ret = re.subn(pattern, ' ', line)  # 返回值ret是一个二元组，替换后的字符串和替换的个数
        ans[ids[idx + absolute]] += ret[1]
        line = ret[0]
    return line


file = open('file')
lines = file.readlines()
file.close()
for line in lines:
    for idx, pattern in enumerate(consts):  # 匹配常量
        ret = re.findall(pattern, line)
        if ret:  # 返回非空list 某个常量模式匹配到的所有结果
            ans[ids[idx]] += len(ret)  # 保存匹配到的结果数
            for item in ret:
                line = re.sub(item, ' ', line)  # 将匹配到的子串用空格替换，以进行下一次匹配

    line = my_filter(len(consts), kws,  # 三层嵌套
                     my_filter(len(consts) + len(kws) + len(ops), seps,
                               my_filter(len(consts) + len(kws), ops, line)))
    ret = re.subn(id_pattern, ' ', line)  # 匹配完标识符，再匹配关键字
    ans['id'] += ret[1]
    line = ret[0]

    if not line.isspace():  # 确定最后的line不是空格组成的字符串
        ans['unknow'] += len(re.split(r' +', line.rstrip().lstrip()))  # 去掉左右的空格后以空格分隔，剩下的就是无法解析的词
for item in ans.keys():
    if ans[item]:
        print("(%s, %d)" % (item, ans[item]))
