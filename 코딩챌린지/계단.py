from sys import stdin

M, J = map(int, stdin.readline().split())

if M >= J:
    print(M - J)
else:
    if (J-M) % 3 == 0:
        print((J-M)//3)
    else:
        print((J-M)//3 + 1 + 3- (J-M)%3)