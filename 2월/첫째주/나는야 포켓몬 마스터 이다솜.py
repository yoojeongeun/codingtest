# https://www.acmicpc.net/problem/1620

from sys import stdin

N, M = map(int, stdin.readline().split())
dic_name, dic_num, cnt = {}, {}, 1
b = 0

while b != M:
    temp = stdin.readline().rstrip()
    if ord(temp[0]) < 65:
        print(dic_num[int(temp)])
        b += 1
    else:
        if temp not in dic_name:
            dic_num[cnt], dic_name[temp] = temp , cnt
            cnt += 1
        else:
            print(dic_name[temp])
            b += 1


