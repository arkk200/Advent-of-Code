history = []
size_history = []
sizes = []

total:int = 0
disk_space:int = 70000000
required_space:int = 30000000

def path(dir: str):
    global total, size_history, sizes
    
    size = 0
    history.append(dir)
    size_history.append(0)
    
    while True:
        print([f"{v}:{size_history[i]}" for i, v in enumerate(history)], end = " ")
        command: str = input()
        if command.startswith('$'):
            command: list = command.split(' ')

            if command[1] == "cd":
                if command[2] == "..":
                    sizes.append(size_history.pop())
                    history.pop()
                    total += size if size <= 100000 else 0
                    return size
                else:
                    path(command[2])

        elif not command.startswith('dir'):
            size = int(command.split(' ')[0])
            size_history = [i + size for i in size_history]

def binary_search(sizes: list, rs: int) -> int:
    i = 0
    j = sizes.__len__() - 1
    m = (i + j) // 2
    while not (sizes[m] < rs and rs < sizes[m+1]) and i < j:
        if sizes[m] > rs:
            j = m
        else:
            i = m + 1
        m = (i + j) // 2
    return m + 1

a = input()
path(a.split(' ')[2])
sizes.sort()
required_space = sizes[-1] - (disk_space - required_space)


m = binary_search(sizes, required_space)
print(sizes[m])