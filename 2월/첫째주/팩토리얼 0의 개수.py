# https://www.acmicpc.net/problem/1676
# 백준 1676
from sys import stdin

N = int(stdin.readline())
result = 1
for i in range(1, N+1):
    result *= i

print(result)
print(len(str(result)) - len(str(int(str(result)[::-1]))))