def solution(numbers, target):
    child = [0]

    for num in numbers:
        temp = []
        while child:
            tp = child.pop()
            temp.append(tp + num)
            temp.append(tp - num)
        child = temp

    return child.count(target)