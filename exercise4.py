#!/usr/bin/python3
# coding:utf-8
from termcolor import colored

articles = list()
noT = list()  # all the non-terminators
with open('file4') as file:
    lines = file.readlines()
for line in lines:
    d = dict()
    d['left'] = line.split('::')[0]
    d['right'] = line.split('::')[1][0:-1]  # abandon '\n'
    articles.append(d)
    if line[0] not in noT:
        noT.append(line[0])


# input a string, output the first_set of this
def find_first_set(string):  # arg == dict['right']
    if not string:
        return ['#']
    elif (not string[0].isupper()) & (string[0] != '#'):  # terminator
        return [string[0]]
    elif string[0].isupper():  # non-terminator
        return find_nonT_first(string)
    elif string[0] == '#':  # '#'
        return ['#']


def find_nonT_first(nonT):
    candidate = list()
    first = list()
    for a in articles:
        if a['left'] == nonT[0]:
            candidate.append(a)

    for cand in candidate:
        if cand.get('first'):
            for e in cand.get('first'):
                first.append(e)
        elif (not cand.get('right')[0].isupper()) & (cand.get('right')[0] != '#'):  # terminator
            first.append(cand.get('right')[0])
        elif cand.get('right')[0].isupper():  # non-terminator
            for e in find_nonT_first(cand.get('right')):
                first.append(e)
        elif cand.get('right')[0] == '#':  # '#'
            first.append('#')
            # first.append(find_nonT_first(nonT[1:]))
            for e in find_nonT_first(nonT[1:]):
                first.append(e)

    first = list({}.fromkeys(first).keys())
    return first


for a in articles:
    a['first'] = find_first_set(a['right'])

follow = dict(zip(noT, [[] for i in noT]))
follow[lines[0][0]].append('$')
follow_tmp = dict()
for key in follow.keys():
    follow_tmp[key] = [e for e in follow[key]]

# algorithm in PPT Page 57
while 1:
    for arti in articles:  # for every production
        for idx, r in enumerate(arti['right']):
            if r in noT:
                fir = find_first_set(arti['right'][idx + 1:])
                fir = list({}.fromkeys(fir).keys())
                for e in fir:
                    if (e not in follow[r]) & (e != '#'):
                        follow[r].append(e)
                if '#' in fir:
                    for ele in follow[arti['left']]:
                        if ele not in follow[r]:
                            follow[r].append(ele)

    if follow_tmp == follow:
        break
    else:
        for key in follow.keys():
            follow_tmp[key] = [e for e in follow[key]]

for arti in articles:
    if '#' in arti['first']:
        tmp = [e for e in arti['first']]
        tmp.remove('#')
        for ele in follow[arti['left']]:
            if ele not in tmp:
                tmp.append(ele)
        arti['select'] = [e for e in tmp]
    else:
        arti['select'] = [e for e in arti['first']]

lefts = list()
sett = set()  # a set of duplicated left-value
for arti in articles:
    lefts.append(arti['left'])

for e in lefts:
    if lefts.count(e) > 1:
        sett.add(e)

is_LL1 = True
for s in sett:
    has_same_left = list()
    for arti in articles:
        if s == arti['left']:
            has_same_left.append(arti)

    for idx, e in enumerate(has_same_left):
        for ee in has_same_left[idx + 1:]:
            if e['select'] == ee['select']:
                is_LL1 = False
                print(colored('Not LL(1)', 'red'))
    if not is_LL1:
        break


if is_LL1:
    print(colored('Predicted table:', 'green'))
    for a in articles:
        print(a['left'], '--->', a['right'], '\t', 'select set is ', a['select'])

s = input(colored('\nPlease input a generator:\n', 'blue'))
gen_stack = []
stack = [lines[0][0]]
for c in s:
    gen_stack.append(c)

gen_stack.append('$')
gen_stack = gen_stack[::-1]
while stack:
    is_legal = False
    for a in articles:
        if (a['left'] == stack[-1]) & (gen_stack[-1] in a['select']):
            is_legal = True
            stack.pop()
            if a['right'][0] == gen_stack[-1]:
                print(a['left'], '--->', a['right'])
                print(colored('match ' + gen_stack[-1], 'yellow'))
                gen_stack.pop()
                for e in a['right'][::-1]:
                    if e in noT:
                        stack.append(e)
            elif a['right'][0] in noT:
                print(a['left'], '--->', a['right'])
                for e in a['right'][::-1]:
                    stack.append(e)
            elif a['right'][0] == '#':
                print(a['left'], '--->', a['right'])

            break

    if not is_legal:
        print(colored('\nNot legal', 'red'))
        break

