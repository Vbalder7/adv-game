def Starting_Dialogue():
    print("Welcome to the Wonderful World of Tarish!")
    print("")
    p_name = input("What is your name Young master?:  ")
    print("Ahh " + p_name + " it is then!")
    print("")
    p_age = input("And what might your age be?:  ")
    print("Ah i see so you are " + p_name + " and you are " + p_age + " years old?")
    print("")
    confirm = input("Please confirm y/n: ")
    if int(p_age)  <=35 :
        print("You appear to be quite a young adventurer!")
        print("")
    elif int(p_age) >35:
        print("You seem to be quite along in your age!")
        print("")
    while confirm == confirm:
        if confirm == "n":
            p_name = input("What is your name Young master?:  ")
            print("Ahh " + p_name + " it is then!")
            print("")
            p_age = input("And what might your age be?:  ")
            print("Ah i see so you are " + p_name + " and you are " + p_age + " years old?")
            print("")
            confirm = input("Please confirm y/n: ")
        else:
            print("Excellent, then we can Start your adventure!")
            print("")
            break
    print("""
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """)

Starting_Dialogue()