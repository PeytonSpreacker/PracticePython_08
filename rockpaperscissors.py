import getpass
import time

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
    global score_p1, score_p2
    # player 1 inputs their selection privately
    player1 = getpass.getpass("Player 1: rock, paper, or scissors? ")
    # player 2 inputs their selection privately
    player2 = getpass.getpass("Player 2: rock, paper, or scissors? ")
    # game conditions
    if player1 == player2:
        print("Stalemate")
        time.sleep(1.0)
    elif player1 == "rock":
        if player2 == "scissors":
            print("Rock smashes scissors! Player 1 wins!")
            score_p1 = score_p1 + 1
            time.sleep(1.0)
        else:
            print("Paper covers rock! Player 2 wins")
            score_p2 = score_p2 + 1
            time.sleep(1.0)
    elif player1 == "paper":
        if player2 == "rock":
            print("Paper covers rock! Player 1 wins!")
            score_p1 = score_p1 + 1
            time.sleep(1.0)
        else:
            print("Scissors cuts paper! Player 2 wins.")
            score_p2 = score_p2 + 1
            time.sleep(1.0)
    elif player1 == "scissors":
        if player2 == "paper":
            print("Scissors cuts paper! Player 1 wins!")
            score_p1 = score_p1 + 1
            time.sleep(1.0)
        else:
            print("Rock smashes scissors! Player 2 wins.")
            score_p2 = score_p2 + 1
            time.sleep(1.0)
    else:
        print("Invald input! Please try again.")
    print("Player 1: ", score_p1)
    print("Player 2: ", score_p2)
    playagain()
    
def playagain():
    user_command = input("Do you want to play again? y/n ")
    if user_command == "y":
        game()
    elif user_command == "n":
        print("Thanks for playing!")
        quit()

score_p1 = 0
score_p2 = 0
introduction()