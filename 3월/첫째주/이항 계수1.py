from sys import stdin

large, small = stdin.readline().split()
large, small = int(large), int(small)

num = [1] * (large + 1)
for i in range(1, large + 1):
    num[i] = num[i-1] * i

print(num[large]//(num[large-small] * num[small]))


