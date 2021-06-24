def solution(param0):
    answer = ''
    answerConcat = ''
    idx = 0

    for elem in param0:
        if elem == "BOOL":
            answerConcat += '#'
            idx += 1
        elif elem == "SHORT":
            padLen = 2 - idx % 2 if idx % 2 != 0 else 0
            for _ in range(padLen):
                answerConcat += '.'
            answerConcat += "##"
            idx += padLen + 2
        elif elem == "FLOAT":
            padLen = 4 - idx % 4 if idx % 4 != 0 else 0
            for _ in range(padLen):
                answerConcat += '.'
            answerConcat += "####"
            idx += padLen + 4
        elif elem == "INT":
            padLen = 8 - idx % 8 if idx % 8 != 0 else 0
            for _ in range(padLen):
                answerConcat += '.'
            answerConcat += "########"
            idx += padLen + 8
        elif elem == "LONG":
            padLen = 8 - idx % 8 if idx % 8 != 0 else 0
            for _ in range(padLen):
                answerConcat += '.'
            answerConcat += "################"
            idx += padLen + 16

    # 마지막 패딩
    padLen = 8 - idx % 8 if idx % 8 != 0 else 0
    for _ in range(padLen):
        answerConcat += '.'

    # 128 바이트를 넘으면 HALT
    if len(answerConcat) > 128:
        answer = "HALT"
    # 아닌 경우 8바이트마다 ,를 추가하면서 answer 생성
    else:
        for idx, char in enumerate(answerConcat):
            if idx % 8 == 0 and idx != 0:
                answer += ','
            answer += char

    return answer