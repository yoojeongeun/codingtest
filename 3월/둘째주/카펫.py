def solution(brown, yellow):
    for num in range(yellow, int(yellow**0.5)-1, -1):
        if yellow % num == 0:
            if (num + 2) * (yellow//num + 2) == brown + yellow:
                return [num+2, yellow//num + 2]

