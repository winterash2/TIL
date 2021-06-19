# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    answer = []
    emailDict = dict()
    emailSuf = '@' + C.lower() + '.com'
    for fullName in S.split(','):
        sepName = fullName.strip().split(' ')
        email = '' + sepName[0] + '.' + sepName[1] if len(sepName) == 2 else '' + sepName[0] + '.' + sepName[2]
        email = email.replace("-", "").lower()

        if email in emailDict:
            emailDict[email] = emailDict[email] + 1
            email += str(emailDict[email])
        else:
            emailDict[email] = 1
        answer.append(fullName + ' <' + email + emailSuf + '>')
    
    return ','.join(answer)


S = 'John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker'
C = 'Example'
solution(S, C)