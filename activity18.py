#boolean variable

come = True

while come:
    ask = input("Hey, are you still there?: ")

    if ask.lower() == "yes":
        print("Great! Let's continue.")

    else: 
        print("Hmm... I guess you're not interested. Goodbye!")
        break