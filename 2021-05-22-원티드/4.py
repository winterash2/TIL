# ---

import heapq
import sys
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[[] for _ in range(N+1)] for _ in range(2)]

for _ in range(M):
	a, b = map(int, input().split())
	graph[0][a].append(b) # graph[0]은 방향이 원래대로일 때
	graph[1][b].append(a) # graph[1]은 방향이 반대로일 때

answer = []
for start in range(1, N+1):
	dp = [[0 for _ in range(N+1)] for _ in range(2)]
	visited = [False for _ in range(N+1)]
	cur = start
	score = 0
	status = 0 # 방향이 원래대로 일 때
	
	q = []
	q.append((score, cur, status, visited))
	while q:
		score, cur, status, visited = heapq.heappop(q)
		
		if visited[cur] == False:
			score += 1
			visited[cur] = True
		
		if dp[status][cur] >= score:
			continue # 이미 여기에 크거나 같은 값으로 왔으면 스킵
		dp[status][cur] = score
		
		# if start == 2:
		# 	print(score, cur, status, visited, dp)
		
		for nxt in graph[status][cur]:
			nxtStatus = 0 if status == 1 else 1
			nxtVisited = [ x for x in visited]
			heapq.heappush(q, (score, nxt, nxtStatus, nxtVisited))
	# print(dp)
	answer.append(( max(max(dp[0]), max(dp[1]) ), start))

answer.sort(key = lambda x : (-x[0], x[1]))
print(answer[0][1], answer[0][0])