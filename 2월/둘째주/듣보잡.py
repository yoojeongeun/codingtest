# https://www.acmicpc.net/problem/1764
# 백준 1764번

from sys import stdin

N, M = map(int, stdin.readline().split())

no_listen, no_see = [], []
for _ in range(N):
    no_listen.append(stdin.readline().rstrip())

for _ in range(M):
    no_see.append(stdin.readline().rstrip())

result = sorted(list(set(no_listen).intersection(no_see)))
print(len(result))

for answer in result:
    print(answer)
