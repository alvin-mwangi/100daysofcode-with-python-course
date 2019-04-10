from roll import Roll
from player import Player
import random
import logbook
import sys


app_log = logbook.Logger('App')

def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename: 
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()
    
    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )

    logger = logbook.Logger('Startup')
    logger.notice(msg)


def build_the_three_rolls():
    return ['Rock', 'Paper', 'Scissors']

def print_header():
    print("----------------------------------------------")
    print("      Welcome to Rock, Paper, Scissors!       ")
    print("----------------------------------------------")
    print("")

def get_players_name():
    playerName = input("Please enter your name: ")
    app_log.trace(f"Player name is '{playerName}'")
    return playerName

def get_player_roll():
    
    userEntry = ""
    
    validEntries = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    loopCount = 0
    maxAttempts = 3

    while loopCount <= maxAttempts:
        loopCount += 1
        userEntry = input("Enter [r]ock, [p]aper, or [s]scissors: ").lower()
        app_log.trace(f"User entered '{userEntry}'")

        if validEntries.get(userEntry) == None:
            msg = 'Invalid entry!'
            print(msg)
            app_log.warn(msg)
        else:
            msg = 'Entry is valid'
            app_log.trace(msg)
            break

        if loopCount > maxAttempts:
            msg = "Too many invalid entries. Exiting..."
            print(msg)
            app_log.error(msg)
            sys.exit(0)
        
    
    return Roll(validEntries.get(userEntry))

def game_loop(player1, player2, rolls):

    count = 1
    player1WinCount = 0
    player2WinCount = 0
    maxRounds = 3

    while count <= maxRounds:    
        p1_roll = get_player_roll()
        p2_roll = Roll(random.choice(rolls))
        
        outcome = p1_roll.can_defeat(p2_roll)

        # display throws:
        print(f"\nRound {count} results:\n")  
        
        print(f"You rolled: {p1_roll.name}") 
        app_log.trace(f"Player1 rolled {p1_roll.name}")
        
        print(f"{player2.name} rolled: {p2_roll.name}") 
        app_log.trace(f"Player2 rolled {p2_roll.name}")

        print(f"Outcome: You {outcome}!\n") 
        
        app_log.trace(f"Round {count} complete.")
        if outcome == 'Win':
            player1WinCount += 1 
            app_log.trace(f"Player1 Won. Incremented player1WinCount to {player1WinCount}")
        if outcome == 'Lose':
            player2WinCount += 1
            app_log.trace(f"Player2 Won. Incremented player2WinCount to {player2WinCount}")
        
        count += 1

    print("\nGAME OVER\n")
    app_log.trace(f"Game Over. Final score is Player1: {player1WinCount}, Player2: {player2WinCount}")
    # log final counts here 
    if player1WinCount > player2WinCount:
        print("Congratulations, {}! You Won!\n".format(player1.name))
        app_log.trace("Player1 won the game.")
    elif player1WinCount < player2WinCount:
        print("Sorry {}, you lost. Better luck next time!\n".format(player1.name))
        app_log.trace("Player2 won the game.")
    else:
        msg = "Game ended with a Tie"
        print(msg + "\n")
        app_log.trace(msg)

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
    init_logging('rps_game.log')
    main()


    

