import heapq

def solution(operations):
    max_heap = []
    min_heap = []

    for operation in operations:
        operation = operation.split()
        if operation[0] == 'I':
            heapq.heappush(min_heap, int(operation[1]))
            heapq.heappush(max_heap, -int(operation[1]))
        else:
            if operation[1] == '1' and max_heap and min_heap:
                temp = heapq.heappop(max_heap)
                min_heap.remove(-temp)
                heapq.heapify(min_heap)

            elif operation[1] == '-1' and max_heap and min_heap:
                temp = heapq.heappop(min_heap)
                max_heap.remove(-temp)
                heapq.heapify(max_heap)
    if min_heap:
        return [-max_heap[0], min_heap[0]]

    else:
        return [0, 0]

print(solution(	["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]))