cnt: int = 0
forest: list = []
visited: None

def rotate(forest) -> list:
    return [[row[i] for row in forest[::-1]] for i in range(len(forest[0]))]

def check(forest) -> None:
    global cnt
    max: int = -1
    for i, v in enumerate(forest):
        for j, u in enumerate(v):
            if max < int(u):
                print(f"i: {i}, j: {j}")
                if not visited[i][j]:
                    cnt += 1
                visited[i][j] = 1
                max = int(u)
        max = -1
    print("checking end")

while True:
    col: str = input()
    if col == "q": break
    forest.append(list(col))
visited = [[0 for _ in forest[0]] for _ in forest]

for i in range(4):
    check(forest)
    forest = rotate(forest)
    visited = rotate(visited)

print(cnt)
for i, v in enumerate(visited):
    print(''.join([f"[{forest[i][j]}:{u}] " for j, u in enumerate(v)]))