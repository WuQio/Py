def func(x):
    l = 0
    r = x
    y = (l + r) / 2
    while abs(y * y - x) > 1e-6:
        if y * y > x:
            r = y
        else:
            l = y
        y = (l + r) / 2
    return y
print(func(5))
