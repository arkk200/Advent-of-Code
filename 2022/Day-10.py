X: int = 1
cycle: int = 0
total: int = 0
duration = 20

def check() -> None:
    global cycle, duration, total, X
    if cycle == duration:
        total += X * duration
        # print(f" - {X}, {duration}")
        duration += 40

while True:
    cmd = input()
    if cmd == "q": break
    cycle += 1
    check()
    if cmd.startswith("addx"):
        cycle += 1
        check()
        X += int(cmd.split(' ')[1])
print(f"total: {total}")