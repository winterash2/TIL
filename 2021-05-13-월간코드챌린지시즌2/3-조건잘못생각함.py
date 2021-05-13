# 더 작은 수로 만들기
from collections import deque


def solution(s):
    answers = []

    for elem in s:
        # print("---------------------------------------")
        # print(elem)
        numList = deque()
        for x in list(elem):
            numList.append(x)
        numList += ['2']

        answer = []
        stack = []
        while numList[0] == '0':
            answer.append(numList.popleft())

        idx = 0
        while True:
            if len(numList) >= 1 and numList[0] == '0':
                numList.popleft()
                answer += ['0']
            elif len(numList) >= 2 and numList[0] == '1' and numList[1] == '0':
                numList.popleft()
                numList.popleft()
                answer += ['1', '0']
            elif len(numList) >= 3 and numList[0] == '1' and numList[1] == '1' and numList[2] == '0':
                numList.popleft()
                numList.popleft()
                numList.popleft()
                answer += ['1', '1', '0']
            else:
                break

        while numList:
            # print("stack=", stack, "answer=", answer)
            if len(stack) >= 3 and stack[len(stack)-3] == '1' and stack[len(stack)-2] == '1' and stack[len(stack)-1] == '0':
                stack.pop()
                stack.pop()
                stack.pop()
                answer += ['1', '1', '0']
            else:
                stack.append(numList.popleft())

        answer += stack[:-1]
        answers.append(''.join(answer))
    return answers


s = ["1110", "100111100", "0111111010", "111111110000"]
result = ["1101", "100110110", "0110110111", '110110110110']
print(solution(s))
print(result)
