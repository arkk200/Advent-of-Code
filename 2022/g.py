forest: list = []
total: list = []
max_num: int = -1

while True:
    col: str = input()
    if col == "q": break
    forest.append(list(col))
    # 곱하기를 할 것이므로 1로 total 배열을 채움
    total.append([1] * len(forest[0]))



def add(e: int, i: int, n: int) -> int:
    return (e + 1) if i > n else 1

def rotate(forest) -> list:
    return [[row[i] for row in forest[::-1]] for i in range(len(forest[0]))]

def set_total_map(forest) -> None:
    arr: list = [0] * 10 # arr[n] = n일 때 보이는 나무들의 개수
    for i, v in enumerate(forest):
        for j, u in enumerate(v):
            u: int = int(u)
            total[i][j] *= arr[u] # 조건에 따라 값을 곱해줌
            # 다음 나올 나무의 키에 따른 값, arr에 저장
            arr = list(map(add, arr, [k for k in range(10)], [u] * 10))
            # print(f"[{u}]: {total[i][j]} next arr[{u}]: " + ' '.join(map(str, arr)))
        arr = [0] * 10
    # print("rotating...")


for i in range(4):
    set_total_map(forest)
    forest = rotate(forest)
    total = rotate(total)
max_num = max(sum(total, []))

# for i, v in enumerate(total):
#     print(''.join([f"[{forest[i][j]}:{u}] " for j, u in enumerate(v)]))
print(f"max: {max_num}")