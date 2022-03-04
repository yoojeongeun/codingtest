from sys import stdin

length = int(stdin.readline())
temp = stdin.readline().strip()
result = [(ord(alpha)-96) * (31**i) for i, alpha in enumerate(temp)]

print(sum(result) % 1234567891)