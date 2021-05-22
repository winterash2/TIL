N, M = map(int, input().split())
dducks = list(map(int, input().split()))

answer = 0
start = 1
end = 1000000
while start <= end:
    mid = (start + end) // 2
    count = 0
    for dduck in dducks:
        remain = dduck - mid
        if remain > 0:
            count += remain
    if count >= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)