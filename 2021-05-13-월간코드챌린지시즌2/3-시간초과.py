def solution(s):
    answers = []

    for elem in s:
        answer = []
        numList = [x for x in list(elem)]
        while numList:
            if len(numList) <= 2:
                answer = answer + numList
                break
            # 아래는 길이가 최소 3인 경우임
            if numList[0] == '0':
                answer = answer + ['0']
                numList = numList[1:]
            elif numList[0] == 1 and numList[1] == '0':  # 10인 경우
                answer = answer + ['1', '0']
                numList = numList[2:]
            elif numList[0] == '1' and numList[1] == '1' and numList[2] == '0':
                answer = answer + ['1', '1', '0']
                numList = numList[3:]
            else:
                # 앞에 3개가 다 1인 경우
                # 일단 110이 있나 찾음
                exist = False
                for i in range(2, len(numList)):
                    if numList[i] == '0' and ''.join(numList[i-2:i+1]) == '110':
                        answer = answer + ['1', '1', '0']
                        numList = numList[:i-2] + numList[i+1:]
                        exist = True
                        break
                if not exist:
                    answer = answer + numList
                    break
        answers.append(''.join([x for x in answer]))