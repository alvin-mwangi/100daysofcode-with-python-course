from collections import namedtuple
"""
Roll

name of roll
rolls that can be defeated by self
rolls that defeated self

"""

class Roll:
    
    def __init__(self, name):
        self.name = name
        
    def can_defeat(self, playerRoll): #playerRoll must be a Roll object; else this will fail        
        # print("playerRoll is {}".format(playerRoll.name)) # convert to log message
        # print("self roll is {}".format(self.name)) # conver to log message

        if(playerRoll.name == 'Rock'):
            if(self.name == 'Scissors'):
                return 'Lose'
            elif(self.name == 'Paper'):
                return 'Win'
            else:
                return 'Tie'
        elif(playerRoll.name == 'Scissors'):
            if(self.name == 'Rock'):
                return 'Win'
            elif(self.name == 'Paper'):
                return 'Lose'
            else:
                return 'Tie'
        elif(playerRoll.name == 'Paper'):
            if(self.name == 'Rock'):
                return 'Lose'
            elif(self.name == 'Scissors'):
                return 'Win'
            else:
                return 'Tie'
        else:
            return None
    

    

            