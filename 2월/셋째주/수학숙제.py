# https://www.acmicpc.net/problem/2870
# 백준 2870

import re
from sys import stdin

m = []
p = re.compile('[0-9]+')
for _ in range(int(stdin.readline())):
    m.extend(p.findall(stdin.readline().rstrip()))

m = sorted(list(map(int, m)))
for result in m:
    print(result)