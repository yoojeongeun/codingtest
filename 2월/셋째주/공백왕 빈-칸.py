# https://www.acmicpc.net/problem/3518
# 백준 3518

from sys import stdin

length = [0] * 180
answer = []
for i in range(1000):
    temp = stdin.readline().strip().split()
    if not temp:
        break
    for i, tp in enumerate(temp):
        if length[i] < len(tp):
            length[i] = len(tp)
    answer.append(temp)

for results in answer:
    temp = ''
    for i, result in enumerate(results):
        temp += result + (length[i] - len(result) + 1 ) * ' '
    print(temp.rstrip())


