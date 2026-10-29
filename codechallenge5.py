rows = 5

for n in range(rows, 0, -1):
    for y in range(1, n + 1):
        print("*", end=" ")
    print()

for c in range(1, rows + 1):
    for d in range(1, c + 1):
        print("*", end=" ")
    print()

