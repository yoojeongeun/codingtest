from sys import stdin

N = int(stdin.readline())
line = list(map(int,stdin.readline().split()))
n1, n2 = map(int, stdin.readline().split())
print(min(line[n1-1:n2]))