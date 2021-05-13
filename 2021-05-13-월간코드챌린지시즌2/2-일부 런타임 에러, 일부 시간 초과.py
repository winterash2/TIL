def solution(numbers):
    answer = []

    for org in numbers:
        orgBin = [2 for _ in range(60)]
        idx = 0
        orgList = bin(org)[2:]

        for i in range(len(orgList)):
            orgBin[60 - len(orgList) + i] = int(orgList[i])

        cur = org + 1
        while True:
            newBin = [2 for _ in range(60)]
            newList = bin(cur)[2:]
            for i in range(len(newList)):
                newBin[60 - len(newList) + i] = int(newList[i])

            count = 0
            for i in range(60):
                if orgBin[i] != newBin[i]:
                    count += 1
                    if count >= 3:
                        break
            if count <= 2:
                answer.append(cur)
                break
            cur += 1

    return answer


print(solution([2, 7]))

# 테스트 1 〉	통과 (25.67ms, 10.4MB)
# 테스트 2 〉	통과 (4403.73ms, 26.3MB)
# 테스트 3 〉	통과 (4.82ms, 10.4MB)
# 테스트 4 〉	통과 (23.51ms, 10.4MB)
# 테스트 5 〉	통과 (60.15ms, 10.5MB)
# 테스트 6 〉	통과 (38.84ms, 10.3MB)
# 테스트 7 〉	통과 (9104.24ms, 26.7MB)
# 테스트 8 〉	통과 (5587.28ms, 26.3MB)
# 테스트 9 〉	통과 (6902.09ms, 25.7MB)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)