from bisect import bisect_left


def solution(citations):
    answer = 0
    citations.sort()
    for i in range(max(citations)):
        if len(citations) - bisect_left(citations, i) >=  i:
            answer = i
    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))
