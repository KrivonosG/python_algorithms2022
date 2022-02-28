#задача для меня оказалась непосильно сложной поэтому я воспользовалась вашим решением
# put your python code here
from collections import deque

queue = deque()
size, count = map(int, input().split())
for j in range(count):
    arrival, duration = map(int, input().split())
    while queue and queue[0] <= arrival:
        queue.popleft()

    if len(queue) < size:
        if queue:
            arrival = max(arrival, queue[-1])
        print(arrival)
        queue.append(arrival + duration)
    else:
        print(-1)