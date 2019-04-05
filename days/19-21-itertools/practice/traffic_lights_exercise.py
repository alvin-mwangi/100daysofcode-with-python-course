import itertools
import sys
import time
import random

#lights = ['red', 'amber', 'green']

# US version
lights = ['red', 'green', 'amber']

lightsCycle = itertools.cycle(lights)
def random_timer():
    return random.randint(5,10)

def light_rotation(lightsCycle):
        
    # while True:
    #     lightColor = next(lightsCycle)
    for lightColor in lightsCycle:
        
        if(lightColor == 'red'): 
            sys.stdout.write(f'STOP! The light is {lightColor}\t\t\t')
            sys.stdout.flush()
            time.sleep(random_timer())
        elif(lightColor == 'green'):
            sys.stdout.write(f'Go! The light is {lightColor}\t\t\t')
            sys.stdout.flush()
            time.sleep(random_timer())
        else:
            sys.stdout.write(f'Caution! The light is {lightColor}\t\t\t')
            sys.stdout.flush()
            time.sleep(2)

        sys.stdout.write('\r')
        sys.stdout.flush()

if __name__ == '__main__':
    light_rotation(lightsCycle)

