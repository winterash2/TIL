# ---

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 1000000007
import sys
sys.setrecursionlimit(1200)

N, K = map(int, input().split())
arr = [False for _ in range(N)]
answer = 0

def dfs(idx, count):
	global N, K, answer, arr
	if idx == N: # 마지막까지 일 한 경우
		answer += 1
		answer = answer % 1000000007
	else:
		if idx >= 7: # 이미 지나간 결석기록 빼기
			if arr[idx - 7] == True:
				count -= 1
		
		if count == K-1: # 제한까지 다 결근한 경우
			arr[idx] = False
			dfs(idx+1, count)
		elif count < K-1: # 아직 더 결근할 수 있는 경우
			arr[idx] = False
			dfs(idx+1, count)
			arr[idx] = True
			dfs(idx+1, count+1)

dfs(0, 0)
print(answer)

# 10 4
# 322

# 8 2
# 10

# 9 3
# 66

# dp 문제임, 나중에 다시 풀어볼 것

