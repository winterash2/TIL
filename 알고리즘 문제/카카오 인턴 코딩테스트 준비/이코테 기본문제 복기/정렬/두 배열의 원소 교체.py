N, K = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
answer = []

arr1.sort(reverse=True)
arr2 += arr1[N-K:]
answer += arr1[:N-K]
arr2.sort(reverse=True)
answer += arr2[:K]
print(sum(answer))

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
