import random, sys

print("Rock, Paper, Scissors")

# variables below keep track of wins and losses

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter your move: rock (r), paper (p), scissors (s), or quit (q)')
        playerMove = input()
        if playerMove == "q":
            sys.exit() # this will quit and end the game
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break # this breaks out of the player input loop
        print('Type in r, p, s, or q')

    #below is the code for the display of what the player chooses
    if playerMove == "r":
        print('ROCK versus...')
    elif playerMove == "p":
        print('PAPER versus...')
    elif playerMove == "s":
        print('SCISSORS versus...')
        
    #below is the code for the display of what the computer randomly chooses
    randomNumber = random.randint(1,4)
    if randomNumber == 1:
        computerMove = "r"
        print('ROCK')
    elif randomNumber == 2:
        computerMove = "p"
        print('PAPER')
    elif randomNumber == 3:
        computerMove = "s"
        print('SCISSORS')

    #below is the code for the display of the record of wins, losses, and ties
    if playerMove == computerMove:
        print("It's a TIE")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You WIN")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You WIN")
        wins = wins + 1 
    elif playerMove == "s" and computerMove == "p":
        print("You WIN")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("you LOSE")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("you LOSE")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("you LOSE")
        losses = losses + 1
