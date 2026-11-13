column = int(input("Enter the number of columns: "))

for n in range(1, 11):
    for y in range(1, column + 1):
        print(n, " x", y, "=", n*y, end= "\t\t\t")
    print()