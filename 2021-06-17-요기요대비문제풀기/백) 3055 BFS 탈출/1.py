import copy
import heapq
import sys
input = sys.stdin.readline

def expand_water(graph):
    n, m = len(graph), len(graph[0])
    expanded = copy.deepcopy(graph)
    for y in range(n):
        for x in range(m):
            if graph[y][x] == '*':
                for d in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    nx = x + d[0]
                    ny = y + d[1]
                    if 0 > nx or 0 > ny or nx >= m or ny >= n:
                        continue
                    if expanded[ny][nx] == '.' or expanded[ny][nx] == 'S':
                        expanded[ny][nx] = '*'
    return expanded


n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
graph = []
for _ in range(n):
    graph.append([x for x in input()])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            x = j
            y = i
# print(graph[49][49])

# [print(x) for x in graph]

q = []
q.append((0, (x, y)))  # (움직인 거리, 고슴도치위치, 지도)

time = 0
answer = 0
count = 0
while q:
    move, (x, y) = heapq.heappop(q)
    if time != move:
        time = move
        graph = expand_water(graph)
    if graph[y][x] == '*':
        continue

    for d in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0 > nx or 0 > ny or nx >= m or ny >= n:
            continue
        if visited[ny][nx]:
            continue
        if graph[ny][nx] == 'D':
            answer = move + 1
            break
        elif graph[ny][nx] == '.':
            visited[ny][nx] = True
            heapq.heappush(q, (move+1, (nx, ny)))
    if answer != 0:
        break

if answer == 0:
    print("KAKTUS")
else:
    print(answer)

"""
5 4
.D.*
....
..X.
S.*.
....
"""
