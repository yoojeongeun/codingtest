from sys import stdin

N, M = map(int, stdin.readline().split())
result = []
dic_name, dic_num, cnt = {}, {}, 1
b = 1

while len(result) != M:
    temp = stdin.readline().rstrip()
    print(temp, b)
    if ord(temp[0]) < 65:
        result.append(dic_num[int(temp)])
    else:
        if temp not in dic_name:
            dic_num[cnt] = temp
            dic_name[temp] = cnt
            cnt += 1
        else:
            result.append(dic_name[temp])

    b += 1