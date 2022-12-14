n = 9
container = [[] for _ in range(n)]
while True:
    col = list(input())
    if col == ['q']: break
    try:
        while (stackPos := col.index('[')) != -1:
            contIndex = stackPos // 4
            container[contIndex].insert(0, col[stackPos + 1])
            col[stackPos] = '!'
    except:
        pass
print("end----------------------")

while True:
    cmd = input()
    if cmd == "q": break
    cmd = cmd.split(" ")
    stacksToMove = int(cmd[1])
    from_ = int(cmd[3]) - 1
    to_ = int(cmd[5]) - 1
    container[to_].extend(container[from_][-stacksToMove::])
    del container[from_][-1: -1-stacksToMove: -1]
for i in container:
    print(list(reversed([j for j in i]))[0], end="")
print()