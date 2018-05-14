# coding:utf-8
# !/usr/bin/python3
import re


def main():
    def judge(f):  # 判断是DFA还是NFA
        with open(f) as file:
            line = file.read()
            file.close()
        if '~' in line or ',' in line:
            return 'NFA'
        else:
            return 'DFA'

    def NFA_get_trans(lines, acc_list):
        Ntrans = [[] for i in range(len(lines[2:-1]))]  # 组装NFA转换表 3维
        for idx, line in enumerate(lines[2:-1]):
            line = line.lstrip().rstrip()
            line = re.sub(r' +', ' ', line)
            lst = line.split()  # lst 以空格为分隔的元素列表
            for e in lst:  # e 转换表某一行中的每个元素
                if ',' in e:
                    tmp_list = e.split(',')
                    l = [int(tmp) for tmp in tmp_list]
                    Ntrans[idx].append(l)
                elif e.isdigit():
                    Ntrans[idx].append([int(e)])
                elif e == '%':
                    Ntrans[idx].append([])

        e_closure = [0]  # 寻找ε闭包
        for idx, row in enumerate(Ntrans):
            if 0 in row[-1]:
                e_closure.append(idx)
        states = [e_closure]  # 组装DFA状态列表 2维列表
        Dtrans = []  # 组装DFA状态转换表 3维列表
        for state in states:
            new_row = [[] for i in range((len(Ntrans[0]) - 1))]  # NFA子集法得到的DFA新状态集合 2维
            for e in state:
                for idx, tmp in enumerate(Ntrans[e][0:-1]):  # 约束条件：Ntrans必须有ε的一列
                    for s in tmp:
                        new_row[idx].append(s) if s not in new_row[idx] else None

            for st in new_row:
                states.append(st) if st not in states else None

            Dtrans.append(new_row)

        new_acc_list = []
        for idx, state in enumerate(states):
            for acc in acc_list:
                new_acc_list.append(idx) if acc in state else None

        new_Dtrans = [[] for i in range(len(states))]  # DFA中的状态集重命名 2维
        for idx, row in enumerate(Dtrans):  # 将states中的状态序号作为DFA的状态号 加入new_Dtrans中
            for st in row:
                new_Dtrans[idx].append(states.index(st))

        return new_Dtrans, new_acc_list

    def DFA_get_trans(lines):
        Dtrans = [[] for i in range(len(lines[2:-1]))]
        for idx, line in enumerate(lines[2:-1]):
            line = line.lstrip().rstrip()
            line = re.sub(r' +', ' ', line)
            elements_list = line.split()
            for e in elements_list:
                Dtrans[idx].append(int(e) if e.isdigit() else [])

        return Dtrans

    lines = open('file').readlines()
    state_num = int(lines[0])  # 状态数
    states = [e for e in range(state_num)]
    symbol = []  # 输入符号
    for i in lines[1]:
        None if i.isspace() else symbol.append(i)
    symbol.pop(-1) if symbol[-1] == '~' else None
    acc_list = [int(e) for e in lines[-1].split()]
    if judge('file') == 'NFA':
        Dtrans, acc_list = NFA_get_trans(lines, acc_list)
    elif judge('file') == 'DFA':
        Dtrans = DFA_get_trans(lines)

    # DFA的最小化
    groups = [[e for e in states if e not in acc_list], acc_list]

    def minimize():
        oldgroups = groups
        groupset = [set(e) for e in groups]
        for idx, s in enumerate(symbol):
            for g in groups:
                next_states = set([])  # 接受一个符号后的状态集
                for e in g:
                    next_states.add(Dtrans[e][idx])

                boo = next_states in groupset  # 输入符号后，到达状态集合是否等于groups中的某个组
                boo_list = []  # 到达状态是否为某个组的子集
                for grp in groupset:
                    boo_list.append(next_states.issubset(grp))

                if sum(boo_list, boo) == 0:  # 既不是某个组 也不是某个组的子集
                    for e in g:
                        if Dtrans[e][idx] not in groups[idx]:
                            groups[idx].pop(e)
                            groups.append([e])
        if groups == oldgroups:
            return None
        else:
            return minimize()
    print('DFA table:')
    print('No.\t', end='')
    [print(s, end='\t') for s in symbol]
    for idx, i in enumerate(Dtrans):
        print('\n', idx, end='\t')
        for ii in i:
            print(ii, end='\t')
    minimize()
    print('\nNon-accept status:')
    for g in groups[0]:
        print(g, end='\t')
    print('\nAccept status:')
    for g in groups[1]:
        print(g, end='\t')
    new_Dtrans = [[] for i in range(len(groups))]  # 2维
    new_acc_list = []
    for gidx, g in enumerate(groups):  # 得到最小化的Dtrans
        for i in range(len(symbol)):
            for idx, gr in enumerate(groups):
                if Dtrans[g[0]][i] in gr:
                    new_Dtrans[gidx].append(idx)
                    break

    for acc in acc_list:  # 得到最小化状态后的接受状态列表
        for idx, g in enumerate(groups):
            if (acc in g) & (idx not in new_acc_list):
                new_acc_list.append(idx)

    str = input('\n输入测试符号串\n')
    state = 0
    print(0, end='')
    for s in str:
        state = new_Dtrans[state][symbol.index(s)]
        print(state, end='')
        if state is None:
            print('\nERROR! Cannot receive this symbol', state, '.')
            return
    if state not in new_acc_list:
        print('\nERROR! The last state is not accept state.')
        return


if __name__ == '__main__':
    main()
