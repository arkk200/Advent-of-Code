X: int = 1
cycle: int = 0
row = 0
display = [[] for _ in range(6)]

def check() -> None:
    global cycle, X
    if X - 1 <= (cycle - 1) % 40 and (cycle - 1) % 40 <= X + 1:
        display[(cycle-1) // 40].append('#')
    else:
        display[(cycle-1) // 40].append('.')

while True:
    cmd = input()
    if cmd == "q": break
    cycle += 1
    check()
    if cmd.startswith("addx"):
        cycle += 1
        check()
        X += int(cmd.split(' ')[1])
for i in display:
    print(''.join(i))