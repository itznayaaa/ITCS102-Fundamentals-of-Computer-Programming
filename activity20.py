#act twenty

books = []

isContinue = True

while isContinue == True:
    ans = input("Do you know any book? (y/n): ").lower()
    if ans == "yes":
        title = input("Enter the title of the book: ")
        books.append(title)
        ans = input("Do you want to add another book? (y/n): ").lower()
        if ans == "yes":
            isContinue = True
            print("You can add another book.")
            continue
    else:
        print("You have chosen not to add any more books.")