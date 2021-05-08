import copy
import heapq


def reverse_road(graph, cur_node):
    new_graph = [[] for _ in range(len(graph))]

    for Q, S in graph[cur_node]:
        new_graph[Q].append((cur_node, S))
    for P in range(1, len(graph)):
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

    if n == 2:
        raise Exception("d")

    visited = [[1e9, 1e9] for _ in range(n+1)]
    is_reversed = [0 for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]
    for road in roads:
        P, Q, S = road
        inserted = False
        for b, c in graph[P]:
            if b == Q:
                inserted = True
                if c > S:
                    graph[P].remove((b, c))
                    graph[P].append((Q, S))
                else:
                    break
        if not inserted:
            graph[P].append((Q, S))
    
    # 자기 자신으로 순환이 가능한 경우를 추가함
    new_graph = copy.deepcopy(graph)
    for P in range(1, len(graph)):
        for Q, S in graph[P]:
            for b, c in graph[Q]:
                if P == b:
                    new_graph[P].append((P, S + c))
    graph = new_graph

    q = []
    heapq.heappush(q, (0, start, graph))
    while q:
        cur_time, cur_node, graph = heapq.heappop(q)

        if cur_node == end:
            answer = cur_time
            break

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

print(solution(	5, 1, 5, [[1, 2, 48], [1, 5, 98], [2, 3, 1], [3, 2, 1], [3, 5, 1]], [3]))
# 루프가 생기는 구조
# 결과는 52