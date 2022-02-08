from sys import stdin

now, destination = map(int, stdin.readline().split())

def count_cnt(now, destination):
    if now == destination:
        return 0

    visit = [False]*100001
    parent, cnt = [now], 1
    while True:
        child = []
        for i in parent:
            for j in [-1, 1, 2]:
                if j == 2:
                    if i*j == destination:
                        return cnt
                    if i*j <= 100000 and i*j >= 0 and not visit[i*j]:
                        child.append(i*j)
                        visit[i*j] = True
                else:
                    if i+j == destination:
                        return cnt
                    if i+j <= 100000 and i+j >= 0 and not visit[i+j]:
                        child.append(i+j)
                        visit[i+j] = True
        cnt += 1
        parent = child


print(count_cnt(now, destination))
