def solution(numbers):
    answer = []

    for org in numbers:
        orgBin = ['0' for _ in range(60)]
        idx = 0
        orgList = bin(org)[2:]

        count = 0
        for elem in orgList:
            if elem == '0':
                count += 1
        if count == 0:
            orgList = '0b10' + ''.join(orgList[1:])
            answer.append(int(orgList, 2))
        else:
            orgList = list(orgList)
            for i in range(len(orgList) - 1, -1, -1):
                if orgList[i] == '0':
                    if i == len(orgList) - 1:
                        orgList[i] = '1'
                    else:
                        orgList[i] = '1'
                        orgList[i+1] = '0'
                    break
            answer.append(int('0b' + ''.join(orgList), 2))

    return answer


print(solution([2, 7]))
# 답 [3, 11]

# 테스트 1 〉	통과 (3.88ms, 10.3MB)
# 테스트 2 〉	통과 (347.90ms, 26.1MB)
# 테스트 3 〉	통과 (0.50ms, 10.4MB)
# 테스트 4 〉	통과 (3.19ms, 10.3MB)
# 테스트 5 〉	통과 (3.57ms, 10.3MB)
# 테스트 6 〉	통과 (3.67ms, 10.3MB)
# 테스트 7 〉	통과 (415.24ms, 25.2MB)
# 테스트 8 〉	통과 (417.75ms, 24.5MB)
# 테스트 9 〉	통과 (384.31ms, 24.3MB)
# 테스트 10 〉	통과 (620.51ms, 26.9MB)
# 테스트 11 〉	통과 (640.68ms, 26.8MB)