from sys import stdin

N = int(stdin.readline())
arr = [0] * 10
for i in range(1, N + 1):
    str_i = str(i)
    for j in str_i:
        arr[int(j)] += 1

for i in arr:
    print(i, end= ' ')