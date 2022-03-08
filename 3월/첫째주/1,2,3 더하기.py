from sys import stdin

def dp(num, target):
    global result
    if num == target:
        result += 1
        return

    elif num > target:
        return

    dp(num+1, target)
    dp(num+2, target)
    dp(num+3, target)


for _ in range(int(stdin.readline())):
    result = 0
    dp(0, int(stdin.readline()))
    print(result)