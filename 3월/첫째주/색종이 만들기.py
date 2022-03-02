from sys import stdin

def make_paper(x,y,N):
    for x1 in range(x, x+N):
        for y1 in range(y, y+N):
            if paper[x1][y1] != paper[x][y]:
                N = N//2
                make_paper(x,y,N)
                make_paper(x+N, y, N)
                make_paper(x, y+N, N)
                make_paper(x+N, y+N, N)

                return

    if paper[x][y] == 1:
        count[1] += 1
    else:
        count[0] += 1

    return


num = int(stdin.readline())

paper = [list(map(int,stdin.readline().strip().split())) for _ in range(num)]
count = [0, 0]
make_paper(0,0, num)
for i in count : print(i)