# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(S):
    totalA = S.count('a')

    if totalA == 0: # 2개로 조합
        answer = (math.factorial(len(S)-1)) // (2 * math.factorial(len(S)-3))
        return answer
    elif totalA % 3 != 0: # 나누기 불가능
        return 0
    else: # 3개로 나누기
        perA = totalA // 3

        idxsA = []
        for idx in range(len(S)):
            if S[idx] == 'a':
                idxsA.append(idx)

        part1Len = idxsA[perA] - idxsA[perA - 1]
        part2Len = idxsA[perA * 2] - idxsA[perA * 2 - 1]
        return part1Len * part2Len


S = 'bbbbb'
solution(S)

'''
a와 b로 이루어진 문자열
세 파트로 나눠야 함
a의 개수가 같게 3파트로 나눠야 하는데 그 경우의 수는?
'''
'''
Example test:   'babaa'
WRONG ANSWER (got 1 expected 2)

Example test:   'ababa'
WRONG ANSWER (got 1 expected 4)

Example test:   'aba'
WRONG ANSWER (got 1 expected 0)

Example test:   'bbbbb'
WRONG ANSWER (got 1 expected 6)
'''
