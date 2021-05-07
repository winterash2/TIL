import heapq

# A -> K -> X
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
X, K = map(int, input().split())


def dijkstra(graph, start):
    result = [1e9 for _ in range(len(graph))]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, cur = heapq.heappop(q)
        if cost < result[cur]:
            result[cur] = cost
            for nxt in graph[cur]:
                heapq.heappush(q, (cost+1, nxt))
    return result


OneTo = dijkstra(graph, 1)
KTo = dijkstra(graph, K)
answer = OneTo[K] + KTo[X]
if answer >= 1e9:
    print(-1)
else:
    print(answer)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""