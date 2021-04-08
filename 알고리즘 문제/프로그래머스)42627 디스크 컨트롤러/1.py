import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) != 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now-current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))


# 선점 방식인 줄 알았는데 비선점이라고 함
"""
import heapq


def solution(jobs):
    answer = 0
    q = []
    jobs.sort(key=lambda x: (x[0], x[1]))
    idx = 0
    cur_time = 0
    while True:
        while idx < len(jobs) and jobs[idx][0] >= cur_time:
            heapq.heappush(q, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if not q:
            if idx < len(jobs):
                cur_time += 1
                continue
            else:
                break
        else:
            spend, start = heapq.heappop(q)
            cur_time += spend
            answer += (cur_time - start)

    answer = answer // len(jobs)

    return answer
"""

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))  # 9
