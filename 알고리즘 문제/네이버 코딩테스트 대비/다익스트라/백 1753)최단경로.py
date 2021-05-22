import heapq
import sys
input = sys.stdin.readline
# INF = float("inf")


def dijkstra(graph, start):
    q = []
    q.append((0, start))
    arr = [1e9 for _ in range(len(graph))]
    while q:
        cost, now = heapq.heappop(q)
        if cost < arr[now]:
            arr[now] = cost
            for nxt in graph[now]:
                heapq.heappush(q, (cost+nxt[1], nxt[0]))
    return arr


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

StartTo = dijkstra(graph, K)

for i in range(1, V+1):
    if StartTo[i] == 1e9:
        print("INF")
    else:
        print(StartTo[i])
