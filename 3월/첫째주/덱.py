from collections import deque
from sys import stdin

deq = deque()
for _ in range(int(stdin.readline())):
    temp = stdin.readline().strip().split()

    if temp[0] == 'push_front':
        deq.appendleft(int(temp[1]))
    elif temp[0] == 'push_back':
        deq.append(int(temp[1]))
    elif temp[0] == 'pop_front':
        print(deq.popleft()) if deq else print(-1)
    elif temp[0] == 'size':
        print(len(deq))
    elif temp[0] == 'pop_back':
        print(deq.pop()) if deq else print(-1)
    elif temp[0] == 'empty':
        print(0) if deq else print(1)
    elif temp[0] == 'front':
        print(deq[0]) if deq else print(-1)
    elif temp[0] == 'back':
        print(deq[-1]) if deq else print(-1)
