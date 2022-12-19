from copy import deepcopy

visited: list[list[bool]] = [[False for _ in range(1000)] for _ in range(1000)]
visited[0][0] = True

cnt: int = 1

H: list[int] = [0, 0]

T: list[int] = [0, 0]

dir: dict[str, list[int]] = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [1, 0],
    'D': [-1, 0]
}

def isAway(a, b) -> bool:
    # print(f"a: {a}, b: {b}")
    # print(f"abs(a-b[0]): {abs(a[0] - b[0])}")
    # print(f"abs(a-b[1]): {abs(a[1] - b[1])}")
    return abs(a[0] - b[0]) == 2 or abs(a[1] - b[1]) == 2

def move(direction, length) -> None:
    global H, T, dir, cnt
    for _ in range(length):
        prev: list[int] = deepcopy(H)
        H[0] += dir[direction][0]
        H[1] += dir[direction][1]
        # print(f"H: {H}")
        if isAway(H, T):
            T = deepcopy(prev)
            # print(f"T: {T}")
            if visited[T[0]][T[1]] == False: cnt += 1
            visited[T[0]][T[1]] = True
        # print("--------------------------------")

while True:
    cmd: str = input()
    if cmd == "q": break
    cmd = cmd.split(' ')
    direction: str = cmd[0]
    length: int = int(cmd[1])
    move(direction, length)

print(f"cnt: {cnt}")