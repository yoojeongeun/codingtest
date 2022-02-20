# https://www.acmicpc.net/problem/1907
# 백준 1907

from sys import stdin

def answer(temp):
    for i in range(1,11):
        for j in range(1,11):
            for k in range(1,11):
                if sorted(temp[0] * i + temp[1] * j) == sorted(temp[2] * k):
                    return i, j, k


temp = stdin.readline().rstrip().split('=')
temp = temp[0].split('+') + temp[-1:]
for i in range(len(temp)):
    change = ''
    for tp in temp[i]:
        if tp.isdigit():
            change += change[-1] * (int(tp) - 1)
        else:
            change += tp
    temp[i] = change


result = answer(temp)

print(result[0], result[1], result[2])