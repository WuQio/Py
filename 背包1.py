# coding:utf-8
# !/usr/bin/python3
cost = [4, 5, 6, 2, 2]
value = [6, 4, 5, 3, 6]
container = 10
table = [[0 for i in range(container)]for j in range(len(cost))]
for j in range(0, container):
    table[0][j] = value[0] if j+1 >= cost[0] else 0

for i in range(1, len(cost)):
    for j in range(0, container):
        if j+1 >= cost[i]:
            table[i][j] = max(table[i-1][j], (table[i-1][j-cost[i]]if j-cost[i] >= 0 else 0) + value[i])
        else:
            table[i][j] = table[i-1][j]

print(table)
