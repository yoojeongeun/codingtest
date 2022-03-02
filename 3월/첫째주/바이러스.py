from sys import stdin

def bfs(network):
    visit = [0] * (len(network) + 1)
    visit[1] = 1
    child = network[1]
    while child:
        temp = []
        for c in child:
            if visit[c] == 0:
                visit[c] = 1
                temp.extend(network[c])
        child = temp

    return sum(visit) - 1

network = dict()
for n in range(int(stdin.readline())):
    network[n+1] = []

for n in range(int(stdin.readline())):
    net = list(map(int, stdin.readline().strip().split()))
    network[net[0]].append(net[1])
    network[net[1]].append(net[0])

print(bfs(network))
