# https://www.acmicpc.net/problem/1541
# 백준 1541
from sys import stdin

sik = stdin.readline().rstrip().split('-')
length = len(sik)
result = sum(list(map(int, sik[0].split('+'))))
for i in range(1,length):
    result -= sum(list(map(int, sik[i].split('+'))))

print(result)