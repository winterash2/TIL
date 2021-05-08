def check_validation(place, x, y):
    valid = True

    # 상하좌우 확인
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for d in directions:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if place[ny][nx] == 'P':
            # print(nx, ny, place[ny][nx])
            valid = False
            break

    if valid:
        # 상상, 하하, 좌좌, 우우 확인
        for d in directions:
            nx = x + d[0] * 2
            ny = y + d[1] * 2
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if place[ny][nx] == 'P':
                if place[y+d[1]][x+d[0]] != 'X':
                    valid = False
                    break
    if valid:
        # 좌상
        nx = x - 1
        ny = y - 1
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            pass
        else:
            if place[ny][nx] == 'P':
                if place[y-1][x] != 'X' or place[y][x-1] != 'X':
                    valid = False

    if valid:
        # 우상
        nx = x + 1
        ny = y - 1
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            pass
        else:
            if place[ny][nx] == 'P':
                if place[y-1][x] != 'X' or place[y][x+1] != 'X':
                    valid = False

    if valid:
        # 좌하
        nx = x - 1
        ny = y + 1
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            pass
        else:
            if place[ny][nx] == 'P':
                if place[y][x-1] != 'X' or place[y+1][x] != 'X':
                    valid = False

    if valid:
        # 우하
        nx = x + 1
        ny = y + 1
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            pass
        else:
            if place[ny][nx] == 'P':
                if place[y+1][x] != 'X' or place[y][x+1] != 'X':
                    valid = False
    return valid


def solution(places):
    answer = []
    for place in places:
        valid = True
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    valid = check_validation(place, x, y)
                    if not valid:
                        break
            if not valid:
                break
        if valid:
            answer.append(1)
        else:
            answer.append(0)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
