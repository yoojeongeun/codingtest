# https://www.acmicpc.net/problem/1927
# 백준 1927
from sys import stdin
import heapq

N, heap = int(stdin.readline()), []

for _ in range(N):
    if (num := int(stdin.readline())) == 0:
        print(0 if len(heap) == 0 else heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
