#!/usr/bin/python3
# coding:utf-8
# i+i*i
# i+(i)*i
# (i*i)
# iii
# a
s = input('Please input a generator:\n')
gen_stack = []
symbols = ['E', 'E_', 'T', 'T_', 'F', ]
for c in s:
    gen_stack.append(c)

gen_stack.append('$')
gen_stack = gen_stack[::-1]
stack = ['$', 'E']
is_gen = True


def Efunc():
    stack.pop(-1)
    stack.append('T')
    stack.append('E_')
    Tfunc()
    E_func()


def E_func():
    stack.pop(-1)
    if gen_stack[-1] == '+':
        stack.append('T')
        stack.append('E_')
        print('In E_func, match \'+\'')
        gen_stack.pop(-1)
        Tfunc()
        E_func()
    else:
        pass


def Tfunc():
    stack.pop(-1)
    stack.append('F')
    stack.append('T_')
    Ffunc()
    T_func()


def T_func():
    stack.pop(-1)
    if gen_stack[-1] == '*':
        stack.append('F')
        stack.append('T_')
        print('In T_func, match \'*\'')
        gen_stack.pop(-1)
        Ffunc()
        T_func()
    else:
        pass


def Ffunc():
    stack.pop(-1)
    global is_gen
    if gen_stack[-1] == '(':
        stack.append('E')
        gen_stack.pop(-1)
        print('In Func1, match \'(\'')
        Efunc()
        if gen_stack[-1] == ')':
            print('In Ffunc, match \')\'')
            gen_stack.pop(-1)
        else:
            print('Bad match')
            is_gen = False
            gen_stack.pop(-1)
    elif gen_stack[-1] == 'i':
        print('In Ffunc, match \'i\'')
        gen_stack.pop(-1)
    else:
        print('Bad match')
        is_gen = False
        gen_stack.pop(-1)


Efunc()
if len(gen_stack)>1:
    is_gen = False
if is_gen:
    print('Yes, it can be a generation.')
else:
    print('No, it cannot be a generation.')