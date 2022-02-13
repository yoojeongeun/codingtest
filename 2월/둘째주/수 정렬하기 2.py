# https://www.acmicpc.net/problem/2751
# 백준 2751

from sys import stdin

N = int(stdin.readline())
number = sorted([int(stdin.readline()) for i in range(N)])
for num in number:
    print(num)

