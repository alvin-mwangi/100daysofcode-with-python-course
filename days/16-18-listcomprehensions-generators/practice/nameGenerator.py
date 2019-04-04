import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

# use the same list to make a little generator
# randomly return a pair of names
# try to make this work:

def gen_pairs(names=NAMES):
    # for i in names:
    #     yield "{} teams up with {}".format(i.split()[0].title(), 
    #                                         random.choice(names).split()[0].title()
    #                                       )
    while True:
        first_names = [name.split()[0].title() for name in names]

        first, second = None, None

        while first == second:
            first, second = random.sample(first_names, 2)

        yield f'{first} teams up with {second}'

pairs = gen_pairs()

for _ in range(100):
    print(next(pairs))




