def solution(param0):
    answer = ['' for _ in range(6)]
    answerArr = [[' ' for _ in range(6)] for _ in range(6)]

    while param0:
        l = param0.pop()
        y = param0.pop()
        x = param0.pop()
        for idx, dx in enumerate(range(l)):
            # 블록 중복 [] 리턴
            if y < 0 or y > 6 or x < 0 or x > 6 or x + dx > 6:
                return []
            # 보드 밖으로 나가면 [] 리턴
            if answerArr[y][x + dx] != ' ':
                return []
            answerArr[y][x + dx] = idx + 1

    # [ print(x) for x in answerArr]
    for x in range(6):
        count = 0
        for y in range(6):
            if answerArr[y][x] != ' ':
                count += answerArr[y][x]
        if count == 10:
            for y in range(6):
                answerArr[y][x] = ' '

    for y in range(6):
        for x in range(6):
            if answerArr[y][x] != ' ':
                answer[y] += str(answerArr[y][x])
            else:
                answer[y] += ' '

    return answer