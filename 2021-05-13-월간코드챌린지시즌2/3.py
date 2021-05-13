# 더 작은 수로 만들기
from collections import deque


def solution(s):
    answers = []

    for elem in s:
        numList = deque()
        for x in list(elem):
            numList.append(x)
        numList += ['2']

        answer = []
        stack = []

        count110 = 0
        while numList:
            # print("stack=", stack, "answer=", answer)
            if len(stack) >= 3 and stack[len(stack)-3] == '1' and stack[len(stack)-2] == '1' and stack[len(stack)-1] == '0':
                stack.pop()
                stack.pop()
                stack.pop()
                count110 += 1
            else:
                stack.append(numList.popleft())

        answer += stack[:-1]

        answerSuf = []
        for i in range(len(answer)-2):
            if answer[i] == '1' and answer[i+1] == '1' and answer[i+2] == '1':
                answerSuf = answer[i:]
                answer = answer[:i]
                break
        for _ in range(count110):
            answer += ['1', '1', '0']
        if answerSuf:
            answer += answerSuf
        answers.append(''.join(answer))
    return answers


s = ["1110", "100111100", "0111111010", "111111110000"]
result = ["1101", "100110110", "0110110111", '110110110110']
print(solution(s))
print(result)
