from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
target = list(map(int, stdin.readline().split()))
candy = deque([i for i in range(1, N+1)])
result = 0
for t in target:
    if (idx := candy.index(t)) <= len(candy) - idx:
        for i in range(idx):
            cd = candy.popleft()
            candy.append(cd)
            result += 1
    else:
        for i in range(len(candy) - idx):
            cd = candy.pop()
            candy.appendleft(cd)
            result += 1
    candy.popleft()

print(result)