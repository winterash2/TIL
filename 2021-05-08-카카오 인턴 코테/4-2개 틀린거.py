import heapq

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
    answer = 1e9

    visited = [[1e9, 1e9] for _ in range(n+1)]
    is_reversed = [0 for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]
    for road in roads:
        P, Q, S = road
        graph[P].append((Q, S))

    q = []
    q.append((0, start, graph))
    while q:
        cur_time, cur_node, graph = heapq.heappop(q)

        if cur_node == end:
            answer = min(answer, cur_time)
            continue

        # 노드에 도착했을 때 트랩이면 반전이 됨
        # 반전이 된 후의 상태를 is_reversed 로 표시함
        # 최초의 상태를 기준으로 0이면 그대로고 1이면 바귄것임
        if cur_node in traps:
            graph = reverse_road(graph, cur_node)
            is_reversed[cur_node] = 0 if is_reversed[cur_node] == 1 else 1

        if visited[cur_node][is_reversed[cur_node]] <= cur_time:
            continue  # 이미 더 빠르게 지나쳐온 것임

        visited[cur_node][is_reversed[cur_node]] = cur_time

        for nxt_node, cost in graph[cur_node]:
            heapq.heappush(q, (cur_time + cost, nxt_node, graph))

    return answer