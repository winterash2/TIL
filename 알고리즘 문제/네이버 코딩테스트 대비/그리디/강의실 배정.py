# https://www.acmicpc.net/problem/11000

import heapq

N = int(input())
lectures = []
for _ in range(N):
    start, end = map(int, input().split())
    lectures.append((start, end))
lectures.sort()

answer = 0
count = 0
q = []
for start, end in lectures:
    time = start
    while q and q[0] <= start:
        heapq.heappop(q)
        count -= 1
    heapq.heappush(q, end)
    count += 1
    if count > answer:
        answer = count

print(answer)

"""
3
1 3
2 4
3 5
"""
