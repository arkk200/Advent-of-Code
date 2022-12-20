from copy import deepcopy
from math import copysign

visited: list[list[bool]] = [[False for _ in range(1000)] for _ in range(1000)]
visited[5][11] = True

cnt: int = 1

roap: list[list[int]] = [[5, 11] for _ in range(10)]

dir: dict[str, list[int]] = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [1, 0],
    'D': [-1, 0]
}

def print_visited() -> None:
    global visited
    for i, v in reversed(list(enumerate(visited))):
        print(''.join([('#' if u == True else '.') if [i, j] not in roap else str(roap.index([i, j])) if roap.index([i, j]) != 0 else 'H' for j, u in enumerate(v)]))


def move_roap(head_prev, roap) -> bool:
    global cnt, visited
    sign = lambda x: int(copysign(1, x)) if x != 0 else 0
    vector: list[int] = [head_prev[0] - roap[1][0], head_prev[1] - roap[1][1]]
    # print(f"vector: {vector}")
    # print(roap)
    # print(f"prev: {prev}")
    for i in range(9):
        # if abs(roap[i][0] - roap[i+1][0]) != 0 and abs(roap[i][1] - roap[i+1][1]) != 0:
        vector = deepcopy([sign(roap[i][0] - roap[i+1][0]), sign(roap[i][1] - roap[i+1][1])])
        # print(f"test[{i}]: {roap[i][0] - roap[i+1][0]} {roap[i][1] - roap[i+1][1]}")
            # print(f"p[1] - r[i][1]: {prev[0] - roap[i][0]}, p[1] - r[i][1]: {prev[1] - roap[i][1]}")
        if abs(roap[i][0] - roap[i+1][0]) == 2 or abs(roap[i][1] - roap[i+1][1]) == 2:
            # print(f"abs1: {abs(roap[i][0] - roap[i+1][0])}, abs2: {abs(roap[i][1] - roap[i+1][1])}")
            roap[i+1][0] += vector[0]
            roap[i+1][1] += vector[1]
            # print(f"moved pos: {roap[i+1]} vec: {vector}")
            if i + 1 == 9 and visited[roap[i+1][0]][roap[i+1][1]] == False:
                visited[roap[i+1][0]][roap[i+1][1]] = True
                cnt += 1
                # print(roap[i+1][0], roap[i+1][1])
    # print_visited()
    # print(f"after: {roap}")

def move(direction, length) -> None:
    global roap, dir, cnt
    for _ in range(length):
        head_prev: list[int] = deepcopy(roap[0])
        roap[0][0] += dir[direction][0]
        roap[0][1] += dir[direction][1]
        move_roap(head_prev, roap)
        # for i, v in enumerate(roap):
        # print("-------------------")

while True:
    cmd: str = input()
    if cmd == "q": break
    cmd = cmd.split(' ')
    direction: str = cmd[0]
    length: int = int(cmd[1])
    move(direction, length)

print(f"cnt: {cnt}")