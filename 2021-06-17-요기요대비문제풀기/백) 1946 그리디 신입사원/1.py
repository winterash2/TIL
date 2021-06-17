import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    scores = []

    N = int(input())
    answer = N
    for i in range(N):
        ps, ivs = map(int, input().split())
        scores.append((ps, ivs))
    scores.sort()

    for i in range(1, len(scores)):
        if scores[i-1][1] < scores[i][1]:
            scores[i] = scores[i-1]
            answer -= 1
    print(answer)


"""
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
"""

"""
T = int(input())
for _ in range(T):
    papers = []
    interviews = []

    N = int(input())
    for i in range(N):
        ps, ivs = map(int, input().split())
        papers.append((ps, i))
        interviews.append((ivs, i))

    papers.sort()
    interviews.sort()

    papers = [x for ( _, x) in papers]
    interviews = [x for ( _, x) in interviews]

    print(papers)
    print(interviews)
"""

# 맞았음 4008ms
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    scores = []

    N = int(input())
    answer = N
    for i in range(N):
        ps, ivs = map(int, input().split())
        scores.append((ps, ivs))
    scores.sort()

    for i in range(1, len(scores)):
        if scores[i-1][1] < scores[i][1]:
            scores[i] = scores[i-1]
            answer -= 1
    print(answer)
"""