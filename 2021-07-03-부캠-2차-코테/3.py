answer = []  
stack = []
regA = None
regB = None

def solution(params):

    def POPA():
        global answer, stack, regA, regB
        if stack:
            regA = stack.pop()
        else:
            answer.append("EMPTY")

    def POPB():
        global answer, stack, regA, regB
        if stack:
            regB = stack.pop()
        else:
            answer.append("EMPTY")

    def ADD():
        global answer, stack, regA, regB
        if regA == None or regB == None:
            answer.append("ERROR")
        elif len(stack) == 8:
            answer.append("OVERFLOW")
        else:
            stack.append(regA + regB)

    def SUB():
        global answer, stack, regA, regB
        if regA == None or regB == None:
            answer.append("ERROR")
        elif len(stack) == 8:
            answer.append("OVERFLOW")
        else:
            stack.append(regA - regB)

    def PUSH0():
        global answer, stack, regA, regB
        if len(stack) == 8:
            answer.append("OVERFLOW")
        else:
            stack.append(0)

    def PUSH1():
        global answer, stack, regA, regB
        if len(stack) == 8:
            answer.append("OVERFLOW")
        else:
            stack.append(1)

    def PUSH2():
        global answer, stack, regA, regB
        if len(stack) == 8:
            answer.append("OVERFLOW")
        else:
            stack.append(2)

    def PUSH3():
        global answer, stack, regA, regB
        if len(stack) == 8:
            answer.append("OVERFLOW")
        else:
            stack.append(3)

    def SWAP():
        global answer, stack, regA, regB
        global regA, regB
        regA, regB = regB, regA

    def PRINT():
        global answer, stack, regA, regB
        if stack:
            answer.append(str(stack.pop()))
        else:
            answer.append("EMPTY")


    for inst in params:
        # print(stack, regA, regB)
        if inst in locals():
            locals()[inst]()
        else:
            answer.append("UNKNOWN")

    return answer