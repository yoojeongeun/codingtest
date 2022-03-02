from sys import stdin

N = int(stdin.readline())

game_over_list = []
answer = []
flug = False
for i in range(N):
    temp = stdin.readline().rstrip()
    temp = temp.replace('.', '0')
    temp = temp.replace('*', '1')
    li = [int(tp) for tp in temp]
    game_over_list.append(li)

for i in range(N):
    result = ''
    temp = stdin.readline().rstrip()
    for j in range(N):
        if temp[j] == 'x':
            if game_over_list[i][j] == 1:
                result += "*"
                flug = True
                continue
            else:
                num = 0
                b1_i = i-1 if i != 0 else i
                b1_j = j-1 if j != 0 else j
                b2_i = i+1 if i != N-1 else N-1
                b2_j = j+1 if j != N-1 else N-1

                for b in range(b1_i, b2_i+1):
                    num += sum(game_over_list[b][b1_j:b2_j+1])
                result += str(num)
        else:
            if game_over_list[i][j] == 1:
                result += '*'
                continue
            result += '.'
    answer.append(result)


if flug == True:
    for a in answer:
        print(a)
else:
    for a in answer:
        print(a.replace('*', '.'))
