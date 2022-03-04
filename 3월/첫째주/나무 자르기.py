from sys import stdin
from collections import Counter

N, length = map(int, stdin.readline().split())
trees = Counter(list(map(int,stdin.readline().split())))
left, right = 0, max(trees)

while right >= left:
    mid = (right+left) // 2
    result = sum([(tree-mid) * trees[tree] for tree in trees if tree > mid])

    if result >= length:
        left = mid + 1
    else:
        right = mid - 1


print(right)