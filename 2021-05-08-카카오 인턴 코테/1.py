
def solution(s):
    answer = ""

    idx = 0
    while idx < len(s):
        cur = s[idx]
        if not cur.isalpha():  # 만약 숫자면
            answer += str(cur)
        else:
            if cur == 'z':
                idx += 3
                answer += '0'
            elif cur == 'o':
                idx += 2
                answer += '1'
            elif cur == 't':
                if s[idx+1] == 'w':
                    idx += 2
                    answer += '2'
                else:
                    idx += 4
                    answer += '3'
            elif cur == 'f':
                if s[idx+1] == 'o':
                    idx += 3
                    answer += '4'
                else:
                    idx += 3
                    answer += '5'
            elif cur == 's':
                if s[idx+1] == 'i':
                    idx += 2
                    answer += '6'
                else:
                    idx += 4
                    answer += '7'
            elif cur == 'e':
                idx += 4
                answer += '8'
            elif cur == 'n':
                idx += 3
                answer += '9'
            else:
                print(cur)
                raise Exception("일치하는 알파벳이 없습니다")
        idx += 1
    answer = int(answer)

    return answer


print(solution("zerotwoone4seveneight"))


# zero - z
# one  - o
# two  - t
# three- t
# four - f
# five - f
# six  - s
# seven- s
# egith- e
# nine - n
