# https://www.acmicpc.net/problem/1931
# 백준 1931

from sys import stdin

data = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]

data.sort(key=lambda x:x[0])
data.sort(key=lambda x:x[1])

end_time, cnt = -1, 0
for d in data:
        if end_time <= d[0]:
                end_time = d[1]
                cnt += 1

print(cnt)