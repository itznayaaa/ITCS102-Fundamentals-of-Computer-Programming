rows = int(input("Enter row number: "))

for n in range(0, rows):
    for y in range(0, rows - n - 1):
        print(" ", end="")
    for y in range(0, n + 1):
        print("* ", end="")
    print()

for n in range(0, rows - 1):
    for y in range(0, n + 1):
        print(" ", end="")
    for y in range(0, rows - n - 1):
        print("* ", end="")
    print()