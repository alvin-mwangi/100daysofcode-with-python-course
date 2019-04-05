

import itertools 

draw = 'GARYTEV'
#listOutput = [''.join(n).lower() for n in list(itertools.permutations(draw, 7))]
listOutput = [x for l in range(2, len(draw)) for x in itertools.permutations(draw, l)]




