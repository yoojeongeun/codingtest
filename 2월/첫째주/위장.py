# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
# 프로그래머스 - 위장

def solution(clothes):
    clothes_dic = {}
    result = 1
    for cth in clothes:
        if cth[1] not in clothes_dic:
            clothes_dic[cth[1]] = 1
        else:
            clothes_dic[cth[1]] += 1
    clothes = list(clothes_dic.values())
    for type in clothes:
        result *= (type + 1)

    return result - 1

print(solution([
                ["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]
                ]))

