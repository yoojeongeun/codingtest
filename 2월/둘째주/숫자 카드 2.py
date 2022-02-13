# https://www.acmicpc.net/problem/10816
# 백준 10816

from sys import stdin
from collections import Counter

N = int(stdin.readline())
number = list(map(int, stdin.readline().split()))
number = Counter(number)
M = int(stdin.readline())
answer = list(map(int, stdin.readline().split()))

for ans in answer:
    print(number[ans], end=' ')

