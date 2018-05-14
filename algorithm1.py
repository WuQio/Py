# coding:utf-8
def sqrt(x):
    y = x
    while abs(y*y - x) > 1e-6:
        y = (y+x/y)/2
    return y

a = input("Please input a number:")
print(sqrt(float(a)))
