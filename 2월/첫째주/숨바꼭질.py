from sys import stdin

now, destination = map(int, stdin.readline().split())

def count_cnt(now, destination):
    if now == destination:
        return 0

    visit = []
    parent, cnt = [now], 1
    temp = [-1, 1, 2]
    while True:
        child = []
        for i in parent:
            for j in temp:
                if j == 2:
                    if i*j == destination:
                        return cnt
                    if destination // 2 <= i*j and i*j not in visit:
                        child.append(i*j)
                        visit.append(i*j)
                else:
                    if i+j == destination:
                        return cnt
                    if destination // 2 <= i+j and i+j not in visit:
                        child.append(i+j)
                        visit.append(i+j)
        cnt += 1
        parent = child

print(count_cnt(now, destination))
