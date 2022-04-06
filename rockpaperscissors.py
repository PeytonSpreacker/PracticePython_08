import getpass
def introduction():
    print("\nWelcome to Rock, Paper, Scissors!\n", 
          "Rules:\n", 
          "> Rock beats scissors\n", 
          "> Paper beats rock\n",
          "> Scissors beats paper\n")
    command = input("Do you want to play rock, paper, scissors? y/n: ")
    if command == "y" :
        game()
    elif command == "n":
        print("okay... :(")
        quit()
    else:
        print("Invalid input, please make a choice.")
def game():
    # player 1 inputs their selection privately
    player1 = getpass.getpass("Player 1: rock, paper, or scissors? ")
    # player 2 inputs their selection privately
    player2 = getpass.getpass("Player 2: rock, paper, or scissors? ")
    # game conditions
    if player1 == player2:
        print("Stalemate")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Rock smashes scissors! Player 1 wins!")
        else:
            print("Paper covers rock! Player 2 wins")
    elif player1 == "paper":
        if player2 == "rock":
            print("Paper covers rock! Player 1 wins!")
        else:
            print("Scissors cuts paper! Player 2 wins.")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Scissors cuts paper! Player 1 wins!")
        else:
            print("Rock smashes scissors! Player 2 wins.")
    else:
        print("Invald input! Please try again.")
    playagain()
def playagain():
    user_command = input("Do you want to play again? y/n ")
    if user_command == "y":
        game()
    elif user_command == "n":
        print("Thanks for playing!")
        quit()

introduction()
score_p1 = 0
score_p2 = 0