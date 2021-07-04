def boost_bin2hex(octStr):
    # 8비트 길이 2진수 문자열을 입력으로 16진수 문자열(0x 뒤는 전부 대문자로)로 바꿔서 리턴
    hexTohexStrDict = {0: '0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    hexStr = '0x'
    # 앞부분
    b8, b4, b2, b1 = int(octStr[0]), int(octStr[1]), int(octStr[2]), int(octStr[3])
    hexStr += hexTohexStrDict[8 * b8 + 4 * b4 + 2 * b2 + b1]
    # 뒷부분
    b8, b4, b2, b1 = int(octStr[4]), int(octStr[5]), int(octStr[6]), int(octStr[7])
    hexStr += hexTohexStrDict[8 * b8 + 4 * b4 + 2 * b2 + b1]
    return hexStr


def boost_dec2hex(dec):
    # 256 미만 10진수를 입력으로 16진수 문자열로 바꿔서 리턴
    hexTohexStrDict = {0: '0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    hexStr = ''
    #앞부분
    hexStr += hexTohexStrDict[int(dec) // 16]
    #뒷부분
    hexStr += hexTohexStrDict[int(dec) % 16]
    return hexStr


def solution(param0):
    answer = ''
    regToBitDict = {'A': '111', 'B': '000', 'C': '001', 'D': '010', 'E': '011', 'H': '100', 'L': '101'}

    inst = ''
    for idx in range(len(param0)):
        if param0[idx] != ' ':
            inst += param0[idx]
        else:
            param0 = param0[idx+1:]
            break
    # 없는 명령어인 경우, 혹은 공백이 잘못된 경우
    if inst != "LD" and inst != "LN":
        return "ERROR"

    param1 = ''
    param2 = ''
    for idx in range(len(param0)):
        if param0[idx] != ',':
            param1 += param0[idx]
        else:
            param2 = param0[idx+1:]
            break
    param1, param2 = param1.strip(), param2.strip()

    if inst == "LD":
        # 레지스터 문자 값이 7종류가 아닌 경우, 혹은 콤마가 잘못된 경우
        if param1 not in regToBitDict or param2 not in regToBitDict:
            return "ERROR"
        # 의미가 없는 경우
        if param1 == param2:
            return "NOOP"
        answer += '01'
        answer += regToBitDict[param1]
        answer += regToBitDict[param2]
        answer = boost_bin2hex(answer)
    elif inst == "LN":
        # 레지스터 문자 값이 7종류가 아닌 경우, 혹은 콤마가 잘못된 경우
        if param1 not in regToBitDict:
            return "ERROR"
        answer += '00'
        answer += regToBitDict[param1]
        answer += '110'
        answer = boost_bin2hex(answer)
        answer += boost_dec2hex(param2)

    return answer