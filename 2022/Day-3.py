check = {}
sameC = None
total = 0

while True:
    first = input()
    if first == "bye": break
    second = input()
    third = input()

    for c in list(first):
        check[c] = 1

    for c in list(second):
        check[c] = (2 if check.get(c, 0) == 1 or check.get(c, 0) == 2 else 0)

    for c in list(third):
        if check.get(c, 0) == 2:
            sameC = c
            break

    if ord(sameC) >= 65 and ord(sameC) <= 90:
        total += ord(sameC) - 38
    elif ord(sameC) >= 97 and ord(sameC) <= 122:
        total += ord(sameC) - 96
    check = {}
print(f"total: {total}")