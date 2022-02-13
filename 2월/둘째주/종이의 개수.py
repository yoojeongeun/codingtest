# https://www.acmicpc.net/problem/1780
# 백준 1780

from sys import stdin

def paper(x,y, N):
    for x1 in range(x, x+N):
        for y1 in range(y, y+N):
            if arr[x][y] != arr[x1][y1]:
                N = N//3
                paper(x,y, N)
                paper(x, y+N , N)
                paper(x, y+N*2, N)

                paper(x+N, y, N)
                paper(x+N, y+N, N)
                paper(x+N, y+N*2 , N)

                paper(x+N*2, y, N)
                paper(x+N*2, y+N, N)
                paper(x+N*2, y+N*2, N)

                return

    if arr[x][y] == -1:
        count[0] += 1
    elif arr[x][y] == 0:
        count[1] += 1
    else:
        count[2] += 1
    return


N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
count = [0,0,0]

paper(0,0,N)
print(count[0])
print(count[1])
print(count[2])

