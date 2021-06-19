# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    answer = 1
    for elem in A:
        if elem < 0:
            continue
        elif elem == answer:
            answer += 1
        elif elem < answer:
            continue
        elif elem > answer:
            return answer
    return answer
