#part1 #jeepneymoment

passengers = ["Nhyn", "Norman", "Noren"]
passengers.append("Nolan")
passengers.insert(0,"Nomar")

passengers.remove("Norman")
x = passengers.pop(2)
y = passengers.pop(0)
len(passengers)

"Nhyn" in passengers 
passengers.reverse()

#part2 #interactivejourney

route = ["MOA", "Intramuros", "BGC", "Cubao"]
passengers = []
SEATS = 6
FARE = 13
total = 0

while True:
    print()
    print("Sakay po kayo, " , passengers , "!")
    print(len(passengers), "of", SEATS, "seats")
    print("1 Sakay\n2 Priority\n3 Para po!")
    print("\n4 Baba sa pinto \n5 Baba sa harap")
    print("\n6 Seat check \n7 Balikan \n 8 Exit")
    choice = input("Choice:  ")

    if choice == "1":
        if len(passengers) == SEATS:
            print("Sorry, the jeep is full.")
        else:
            name = input("Enter your name: ")
            passengers.append(name)
            total += FARE
            print("Welcome aboard,", name, "!")

    elif choice == "2":
        if len(passengers) == SEATS:
            print("Sorry, the jeep is full.")
        else:
            name = input("Enter your name: ")
            passengers.insert(0, name)
            total += FARE
            print(name, "has priority seating. Welcome aboard!")

    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passengers:
            passengers.remove(name)
            total -= FARE
            print(name, "has gotten off. Thank you for riding!")
        else:
            print(name, "is not in the jeep.")

    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else:
            left = passengers.pop()
            print(left, "got off from the back door.")

    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else:
            front = passengers.pop(0)
            print(front, "got off from the front door.")

    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", i + 1, ":", passengers[i])
        route.reverse()
        print("Route:", route)

    elif choice == "7":
        print("Total fare collected: ₱", total)
        break
    else:
        print("Invalid choice. Please try again.")