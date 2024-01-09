import random

tsp = 0
tsc = 0

print("Welcome to Rock, Paper, Scissor Game")

choices = ["y", "n"]
play = None

while True:
    play = input('\nDo you wanna play? (y/n) ').lower()
    if play in choices:
        break
    else:
        print(f'Invalid {play} input. Please try again.')

if play == "y":
    while True:
        choices = ["rock", "paper", "scissor"]
        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input("Rock, Paper, Scissor? ").lower()

        print("\nPlayer : " + player)
        print("Computer : " + computer)

        if player == computer:
            print("Tie")
            tsp += 0
            tsc += 0
        elif player == "rock":
            if computer == "scissor":
                print("You Win!!")
                tsp += 1
            elif computer == "paper":
                print("You Lose!!")
                tsc += 1
        elif player == "paper":
            if computer == "scissor":
                print("You Lose!!")
                tsc += 1
            elif computer == "rock":
                print("You Win!!")
                tsp += 1
        elif player == "scissor":
            if computer == "rock":
                print("You Lose!!")
                tsc += 1
            elif computer == "paper":
                print("You Win!!")
                tsp += 1

        play_again = ["y", "n"]
        play = None
        while True:
            play = input('\nDo you wanna play? (y/n) ').lower()
            if play in play_again:
                break
            else:
                print(f'Invalid {play} input. Please try again.')

        if play != "y":
            score_player = tsp
            score_computer = tsc
            if score_player > score_computer:
                print("\nGREAT!! YOU WIN AGAINST A COMPUTER!!")
            else:
                print("\nNICE TRY BUDDY, COMPUTER'S BETTER THAN YOU")

            print("Thank you for playing!! \n\nResults \nPlayer : " +
                  str(tsp) + "\nComputer : " + str(tsc))
            break
else:
    print("\nThank You!!")
