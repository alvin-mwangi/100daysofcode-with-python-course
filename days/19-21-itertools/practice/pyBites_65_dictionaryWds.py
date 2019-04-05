import itertools
import os
import urllib.request

# PREWORK

DICTIONARY = os.path.join(os.getcwd(), 'dictionary.txt')
print(DICTIONARY)
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    perms = _get_permutations_draw(draw)
    allWords = set([''.join(w).lower() for w in perms]) #convert list of letters to actual words (strings), so we can compare against dictionary words
    possibleWords = allWords & dictionary
    return possibleWords
   

def _get_permutations_draw(draw):
    return [x for l in range(2, len(draw)) for x in itertools.permutations(draw, l)]

if __name__ == "__main__":
    print(get_possible_dict_words('GARYTEV'))
