n, m = map(int, input().split())
answer = 0
graph = [[0 for _ in range(m+1)]]
for _ in range(n):
    graph.append([0]+[int(x) for x in input()])

for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 1:
            graph[i][j] = min(graph[i-1][j-1], graph[i-1][j], graph[i][j-1]) + 1
            answer = max(answer, graph[i][j])

print(answer*answer)
