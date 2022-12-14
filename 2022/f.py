def path(dir: str):
    size: int = 0
    command: int = input()
    if command.startswith('$'):
        command: list = command.split(' ')
        if command[1] == "cd":
            if command[2] == "..":
                return path(command[2]) + size
        elif command[1] == "ls":
            list_: str = None
            while not (list_ := input()).startswith('$'):
                if not list_.startswith("dir"):
                    size += int(list_.split(' ')[0])
                
a = input()
path(a.split()[2])


def path(dir: str):
    size: int = 0
    while True:
        command: int = input()
        if command.startswith('$'):
            command: list = command.split(' ')
            if command[1] == "cd":
                if command[2] == "..":
                    return size
                else:
                    size += path(command[2])
        elif command[0] != "dir":
            size += int(command[0])
a = input()
path(a.split()[2])