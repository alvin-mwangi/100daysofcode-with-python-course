
# Write a function called friends_teams that takes a list of friends, a team_size (type int, default=2) and order_does_matter (type bool, default False).
# Return all possible teams. Hint: if order matters (order_does_matter=True), the number of teams would be greater.

import itertools

friendsList = ['Joe', 'Bob', 'Chloe', 'Mike', 'Alvin', 'Jennifer']

def friends_teams(friendsList, team_size=2, order_does_matter=False):

    if(order_does_matter):
        return list(itertools.permutations(friendsList, team_size))
    else:
        return list(itertools.combinations(friendsList, team_size))

if __name__ == "__main__":
    print(friends_teams(friendsList, 3, False))





