def solution(record):
    answer = []
    result = []
    id = {}
    for i in record:
        temp = i.split()
        if temp[0] == 'Enter':
            id[temp[1]] = temp[2]
            answer.append([temp[1], "님이 들어왔습니다."])
        elif temp[0] == 'Leave':
            answer.append([temp[1], "님이 나갔습니다."])
        else:
            id[temp[1]] = temp[2]

    for aw in answer:
        result.append(id[aw[0]]+aw[1])

    return result


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
