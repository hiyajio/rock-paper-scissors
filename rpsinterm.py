from random import randint

cont = "y"

while (cont == "y"):
    best_out_of = int(input("\nBest out of? (input number) "))

    while best_out_of % 2 == 0:
        print("Rounds have to be odd!\n")
        best_out_of = int(input("Best out of? (input number) "))
    majority = best_out_of//2 + 1

    p_wins = 0
    c_wins = 0

    while p_wins != majority and c_wins != majority:
        print("...Rock...")
        print("...Paper...")
        print("...Scissors...\n\n")

        p_choice = input("(Enter Player's choice): ").lower()
        while p_choice != "paper" and p_choice != "rock" and p_choice != "scissors":
            print("\nCan only choose between rock, paper, and scissors\n")
            p_choice = input("(Enter Player's choice): ")

        c_choice = randint(0,2)
        if c_choice == 0:
            c_choice = "rock"
        elif c_choice == 1:
            c_choice = "paper"
        else:
            c_choice = "scissors"

        print("\n\nSHOOT!\n")

        if (p_choice == "rock"):
            if (c_choice == "rock"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! It's a tie!\n")
            if (c_choice == "paper"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! Computer wins!\n")
                c_wins += 1
            if (c_choice == "scissors"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! Player wins!\n")
                p_wins += 1
        if (p_choice == "paper"):
            if (c_choice == "rock"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! Player wins!\n")
                p_wins += 1
            if (c_choice == "paper"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! It's a tie!\n")
            if (c_choice == "scissors"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! Computer wins!\n")
                c_wins += 1
        if (p_choice == "scissors"):
            if (c_choice == "rock"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! Computer wins!\n")
                c_wins += 1
            if (c_choice == "paper"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! Player wins!\n")
                p_wins += 1
            if (c_choice == "scissors"):
                print("Player chose " + p_choice + " and Computer chose " + c_choice + "! It's a tie!\n")

    if p_wins == majority:
        print(f"Recap: Best out of {best_out_of} rounds. Winner: Player! Congrats!\n\n")
    else:
        print(f"Recap: Best out of {best_out_of} rounds. Winner: Computer! Better luck next time!\n\n")

    cont = input("Do you want to keep playing? (y/n) ")
    
print("Thanks for playing! Bye!")
