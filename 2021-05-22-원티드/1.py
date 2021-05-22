from collections import deque

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())
capacitys = list(map(int, input().split()))
caps = [] # 값, 순서, 본래 idx
for i in range(len(capacitys)):
	val = capacitys[i]
	if i >= K-1: # i가 2면 K가 3일때 처음임
		order = i - K + 1
	else:
		order = i + N
	idx = i + 1
	caps.append((val, order, idx))
caps.sort(key = lambda x : (x[0], x[1]))

answer = []
for elem in caps:
	print(elem[2], end = " ")
	answer.append(elem[2])

