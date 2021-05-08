import bisect


def solution(n, k, cmd):
    answer = ''

    erased = []

    idx = k
    table = [i for i in range(n)]
    for command in cmd:
        command = command.split()
        if command[0] == 'U':
            idx -= int(command[1])
        elif command[0] == 'D':
            idx += int(command[1])
        elif command[0] == 'C':
            if idx == len(table) - 1:
                idx -= 1
                erased.append(table[idx + 1])
                del(table[idx + 1])
            else:
                erased.append(table[idx])
                del(table[idx])
        elif command[0] == 'Z':
            insert = erased.pop()
            insert_idx = bisect.bisect_left(table, insert)
            if insert_idx <= idx:
                idx += 1
            table.insert(insert_idx, insert)

    answer = ['X' for _ in range(n)]
    for idx in table:
        answer[idx] = 'O'
    answer = ''.join(answer)

    return answer


print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
