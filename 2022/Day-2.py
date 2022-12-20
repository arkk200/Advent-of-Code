"""
A, X for Rock       | 1
B, Y for Paper      | 2
C, Z for Sissors    | 3

win
A, Y : A - Y = -1   | 2
B, Z : B - Z = -1   | 3
C, X : C - X = 2    | 1

lose
A, Z : A - Z = -2   | 3
B, X : B - X = 1    | 1
C, Y : C - Y = 1    | 2
"""

lose = {
    'A': 3,
    'B': 1,
    'C': 2
}
draw = {
    'A': 1,
    'B': 2,
    'C': 3
}
win = {
    'A': 2,
    'B': 3,
    'C': 1
}

total = 0
while True:
    a, b = input().split()
    if a == "bye" and b == "bye": break
    if b == 'X':
        total += lose[a]
    elif b == 'Y':
        total += draw[a] + 3
    elif b == 'Z':
        total += win[a] + 6
print(f"total: {total}")