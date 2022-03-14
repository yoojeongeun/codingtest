def solution(num):
    num_str = ''.join(sorted(num, reverse=True))
    print(num_str)
    num = int(num_str)
    result = 0
    for i in range(2, num + 1):
        li = str(i)
        flug = True
        for cnt in li:
            if li.count(cnt) > num_str.count(cnt):
                flug = False
                break

        if flug:
            for sosu in range(2, int(i ** 0.5) + 1):
                if i % sosu == 0:
                    flug = False
                    break

            if flug:
                result += 1

    return result

print(solution('011'))