import heapq

N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(graph, start):
    result = [1e9 for _ in range(len(graph))]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, cur = heapq.heappop(q)
        if cost < result[cur]:
            result[cur] = cost
            for nxt, ncost in graph[cur]:
                heapq.heappush(q, (cost+ncost, nxt))
    return result

Cto = dijkstra(graph, C)
count = -1 # 자기 자신 제외
max_time = 0
for elem in Cto[1:]:
    if elem < 1e9:
        count += 1
        max_time = max_time if max_time > elem else elem

print(count, max_time)

"""
3 2 1
1 2 4
1 3 2
"""