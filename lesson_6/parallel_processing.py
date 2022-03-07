import heapq
from collections import deque

core, amount = list(map(int, input().split()))
tasks = deque(list(map(int, input().split())))

timing = []
plate = [i for i in range(core) if core >= 1]
res = []

for cpu in plate:
    heapq.heappush(timing, (0, cpu))

while tasks:
    process = tasks.popleft()
    curr_cpu = heapq.heappop(timing)
    res.append(f'{curr_cpu[1]} {curr_cpu[0]}')
    new_process = (process+curr_cpu[0], curr_cpu[1])
    heapq.heappush(timing, new_process)
print(*res, sep='\n')




