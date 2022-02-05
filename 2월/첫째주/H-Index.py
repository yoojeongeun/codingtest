# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
# 프로그래머스 - H-Index

def solution(citations):
    citations = sorted(citations, reverse=True)
    max = 0
    for i in range(len(citations)):
        if citations[i] >= i+1:
            max = i+1

    return max


print(solution([5,5,5,5]))