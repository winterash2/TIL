def solution(param0):
    answer = []
    names = []
    files = dict()
    for name in param0:
        name, extension = name.split('.')

        start = 0
        for idx in range(len(name)):
            if name[idx] == '/':
                start = idx + 1
                continue
            if name[idx] == '_':
                name = name[:idx]
                break
        name = name[start:]
        name = name + '.' + extension


        if name in files:
            files[name] = files[name] + 1
        else:
            names.append(name)
            files[name] = 1

    for name in names:
        if files[name] > 1:
            answer.append(name)
            answer.append(str(files[name]))
    return answer