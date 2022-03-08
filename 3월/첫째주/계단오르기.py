from sys import stdin

num = int(stdin.readline())
stair = [int(stdin.readline()) for _ in range(num)]
max_score = [0] * num

max_score[0] = stair[0]
if num >= 2:
    max_score[1] = stair[0] + stair[1]
    if num >= 3:
        max_score[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, num):
    max_score[i] = max(max_score[i-3] + stair[i-1] + stair[i], max_score[i-2] + stair[i])

print(max_score[-1])