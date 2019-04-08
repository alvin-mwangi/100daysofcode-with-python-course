from roll import Roll
from player import Player
import random

def build_the_three_rolls():
    return ['Rock', 'Paper', 'Scissors']

def print_header():
    print("----------------------------------------------")
    print("      Welcome to Rock, Paper, Scissors!       ")
    print("----------------------------------------------")
    print("")

def get_players_name():
    playerName = input("Please enter your name: ")
    return playerName

def get_player_roll():
    
    userEntry = ""
    
    validEntries = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    loopCount = 0
    maxAttempts = 3

    while loopCount <= maxAttempts:
        loopCount += 1
        userEntry = input("Enter [r]ock, [p]aper, or [s]scissors: ").lower()
        if validEntries.get(userEntry) == None:
            print("Invalid entry!")
        else:
            break
        if loopCount > maxAttempts:
            print("Too many invalid entries. Exiting...")
            break
    
    return Roll(validEntries.get(userEntry))

def game_loop(player1, player2, rolls):

    count = 1
    player1WinCount = 0
    player2WinCount = 0

    while count <= 3:    
        p1_roll = get_player_roll()
        p2_roll = Roll(random.choice(rolls))
        
        outcome = p1_roll.can_defeat(p2_roll)

        # display throws:
        print("\nRound {} results:\n".format(count))
        print("You rolled: {}".format(p1_roll.name))
        print("{} rolled: {}".format(player2.name, p2_roll.name))
        print("Outcome: You {}!\n".format(outcome))
        
        if outcome == 'Win':
            player1WinCount += 1
        if outcome == 'Lose':
            player2WinCount += 1
        
        count += 1

    print("\nGAME OVER\n")
    
    if player1WinCount > player2WinCount:
        print("Congratulations, {}! You Won!\n".format(player1.name))
    elif player1WinCount < player2WinCount:
        print("Sorry {}, you lost. Better luck next time!\n".format(player1.name))
    else:
        print("Game ended with a Tie\n")

def main():
    try:
            
        print_header()
        
        rolls = build_the_three_rolls()

        name = get_players_name()
        
        player1 = Player(name)
        player2 = Player("Computer")

        game_loop(player1, player2, rolls)

    except Exception as x:
        print("ERROR: {}".format(x))
        raise
    

if __name__ == "__main__":
    main()


    

