N = int(input())
dp = [[0 for _ in range(N)] for _ in range(9)]
prv = [0 for _ in range(10)]
nxt = [0 for _ in range(10)]
answer = 0
for i in range(9):
    prv[i+1] = 1
    for _ in range(N-1):
        nxt = [0 for _ in range(10)]
        for i in range(10):
            if i-1 >= 0:
                nxt[i] += prv[i-1]
            if i+1 <= 9:
                nxt[i] += prv[i+1]
            prv = nxt
    
    answer += sum(prv)

print(answer)