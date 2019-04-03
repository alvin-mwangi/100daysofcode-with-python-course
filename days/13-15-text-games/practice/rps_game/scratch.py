# userEntry = ""
# validEntries = ['r', 'p', 's']
# loopCount = 0
# while userEntry not in validEntries:
#     loopCount += 1
#     userEntry = input("Enter [r]ock, [p]aper, or [s]scissors: ").lower()
#     if userEntry not in ['r', 'p', 's']:
#         print("Invalid entry!")
#     if loopCount >= 3:
#         print("Too many invalid attempts. Exiting...")
#         break

# validEntries = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
# print(validEntries.get(None))



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
    
    return validEntries.get(userEntry)


playerRoll = get_player_roll()
print("Player roll is: {}".format(playerRoll))
