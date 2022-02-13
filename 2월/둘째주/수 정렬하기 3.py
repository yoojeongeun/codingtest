# https://www.acmicpc.net/problem/10989
# 백준 10989

from sys import stdin
arr = [0]
count = [0] * 10001

for _ in range(int(stdin.readline())):
    count[int(stdin.readline())] += 1

for cnt in range(len(count)):
    if count[cnt] > 0:
        for _ in range(count[cnt]):
            print(cnt)


