def solution(n, computers):
    visit = [0] * n
    result = 0
    for i, computer in enumerate(computers):
        if visit[i] == 0:
            result += 1
            visit[i] = 1
            child = [i]
            while child:
                temp = []
                for network in child:
                    for j, net in enumerate(computers[network]):
                        if visit[j] == 0 and net == 1:
                            temp.append(j)
                            visit[j] = 1

                child = temp


    return result




print(solution(3, [[1,0,1], [0, 1, 1], [1, 1, 1]]))