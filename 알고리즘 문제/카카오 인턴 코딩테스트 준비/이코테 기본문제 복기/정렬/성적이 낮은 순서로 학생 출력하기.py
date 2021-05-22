N = int(input())
arr = []
for _ in range(N):
    name, score = input().split()
    score = int(score)
    arr.append((score, name))

arr.sort()

for score, name in arr:
    print(name, end=" ")
