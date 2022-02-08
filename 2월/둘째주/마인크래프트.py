# https://www.acmicpc.net/problem/18111
# 백준 18111

from sys import stdin
from collections import Counter

N, M, B = map(int, stdin.readline().split())
data = []
for _ in range(N):
    data.extend(list(map(int,stdin.readline().split())))
data = Counter(data)
result, height = float("inf"), 0
min_h, max_h = min(data), max(data)

for h in range(min_h, max_h + 1):
    stack, pop = 0, 0
    for d in data:
        if d >= h:
            pop += (d-h) * data[d]
        else:
            stack += (h-d) * data[d]
    if stack <= B + pop:
        time = stack + pop * 2
        if result >= time:
            result, height = time, h

print(result, height)

