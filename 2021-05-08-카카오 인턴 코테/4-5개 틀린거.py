import heapq

INF = float('inf')

def reverse_road(graph, cur_node):
    new_graph = [[] for _ in range(len(graph))]

    for Q, S in graph[cur_node]:
        new_graph[Q].append((cur_node, S))
    for P in range(len(graph)):
        if P == cur_node:
            continue
        for Q, S in graph[P]:
            if Q == cur_node:
                new_graph[Q].append((P, S))
            else:
                new_graph[P].append((Q, S))
    return new_graph


def solution(n, start, end, roads, traps):
    answer = 0

    visited = [[1e9, 1e9] for _ in range(n+1)]
    is_reversed = [0 for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]
    for road in roads:
        P, Q, S = road
        graph[P].append((Q, S))

    q = []
    q.append((0, start))
    while q:
        cur_time, cur_node = heapq.heappop(q)

        # 노드에 도착했을 때 트랩이면 반전이 됨
        # 반전이 된 후의 상태를 is_reversed 로 표시함
        # 최초의 상태를 기준으로 0이면 그대로고 1이면 바귄것임
        if cur_node in traps:
            graph = reverse_road(graph, cur_node)
            is_reversed[cur_node] = 0 if is_reversed[cur_node] == 1 else 1

        if visited[cur_node][is_reversed[cur_node]] <= cur_time:
            continue  # 이미 더 빠르게 지나쳐온 것임

        visited[cur_node][is_reversed[cur_node]] = cur_time

        if cur_node == end:
            answer = cur_time
            break

        for nxt_node, cost in graph[cur_node]:
            heapq.heappush(q, (cur_time + cost, nxt_node))

    return answer


n = 4
start = 1
end = 4
roads = [[1, 2, 1],
         [3, 2, 1],
         [2, 4, 1]]
traps = [2, 3]
result = 4
print(solution(n, start, end, roads, traps))
