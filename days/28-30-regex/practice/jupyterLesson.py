#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'days\28-30-regex\practice'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Regular Expressions in Python
# 
# > Some people, when confronted with a problem, think, "I know, I'll use regular expressions." Now they have two problems. - Jamie Zawinski
# 
# ## First day: quick overview
# 
# This first day we will explore the basics of the `re` (standard libary) module so you can start adding this powerful skill to your Python toolkit.

#%%
import re

#%% [markdown]
# ### When not to use regexes? 
# 
# Basically when regular string manipulations will do, for example:

#%%
text = 'Awesome, I am doing the #100DaysOfCode challenge'

#%% [markdown]
# Does text start with 'Awesome'?

#%%
text.startswith('Awesome')

#%% [markdown]
# Does text end with 'challenge'?

#%%
text.endswith('challenge')

#%% [markdown]
# Does text contain '100daysofcode' (case insensitive)
# 

#%%
'100daysofcode' in text.lower()

#%% [markdown]
# I am bold and want to do 200 days (note strings are inmutable, so save to a new string)

#%%
text.replace('100', '200')

#%% [markdown]
# ### Regex == Meta language
# 
# But what if you need to do some more tricky things, say matching any #(int)DaysOfCode? Here you want to use a regex pattern. Regular expressions are a (meta) language on their own and I highly encourage you to read through [this HOWTO](https://docs.python.org/3.7/howto/regex.html#regex-howto) to become familiar with their syntax.
#%% [markdown]
# ### `search` vs `match` 
# 
# The main methods you want to know about are `search` and `match`, former matches a substring, latter matches the string from beginning to end. I always embed my regex in `r''` to avoid having to escape special characters like \d (digit), \w (char), \s (space), \S (non-space), etc (I think \\\d and \\\s clutters up the regex)

#%%
text = 'Awesome, I am doing the #100DaysOfCode challenge'


#%%
re.search(r'I am', text)


#%%
re.match(r'I am', text)


#%%
re.match(r'Awesome.*challenge', text)

#%% [markdown]
# ### Capturing strings
# 
# A common task is to retrieve a match, you can use _capturing () parenthesis_ for that:

#%%
hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'

m = re.match(r'.*(#\d+DaysOfCode).*', hundred)
m.groups()[0]


#%%
m = re.search(r'(#\d+DaysOfCode)', two_hundred)
m.groups()[0]

#%% [markdown]
# ### `findall` is your friend
# 
# What if you want to match multiple instances of a pattern? `re` has the convenient `findall` method I use a lot. For example in [our 100 Days Of Code](https://github.com/pybites/100DaysOfCode/blob/master/LOG.md) we used the `re` module for the following days - how would I extract the days from this string?

#%%
text = '''
$ python module_index.py |grep ^re
re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095'''

re.findall(r'\d+', text)

#%% [markdown]
# How cool is that?! Just because we can, look at how you can find the most common word combining `findall` with `Counter`:

#%%
text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum"""


#%%
text.split()[:5]

#%% [markdown]
# Of course you can do the same with `words.split()` but if you have more requirements you might fit it in the same regex, for example let's only count words that start with a capital letter.
# 
# I am using two _character classes_ here (= pattern inside `[]`), the first to match a capital letter, the second to match 0 or more common word characters. 
# 
# Note I am escaping the single quote (') inside the second character class, because the regex pattern is wrapped inside single quotes as well: 

#%%
from collections import Counter

cnt = Counter(re.findall(r'[A-Z][A-Za-z0-9\']*', text))
cnt.most_common(5)

#%% [markdown]
# ### Compiling regexes
#%% [markdown]
# If you want to run the same regex multiple times, say in a for loop it is best practice to define the regex one time using `re.compile`, here is an example:

#%%
movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')
movies

#%% [markdown]
# Let's find movie titles that have exactly 2 words, just for exercise sake. Before peaking to the solution how would _you_ define such a regex?
#%% [markdown]
# OK here is one way to do it, I am using `re.VERBOSE` which ignores spaces and comments so I can explain what each part of the regex does (really nice!):

#%%
pat = re.compile(r'''
                  ^             # start of string
                  \d+           # one or more digits
                  \.            # a literal dot
                  \s+           # one or more spaces
                  (?:           # non-capturing parenthesis, so I don't want store this match in groups()
                  [A-Za-z']+\s  # character class (note inclusion of ' for "Schindler's"), followed by a space
                  )             # closing of non-capturing parenthesis
                  {2}           # exactly 2 of the previously grouped subpattern
                  \(            # literal opening parenthesis
                  \d{4}         # exactly 4 digits (year)
                  \)            # literal closing parenthesis
                  $''', re.VERBOSE)       # end of string
                 

#%% [markdown]
# As we've seen before if the regex matches it returns an `_sre.SRE_Match` object, otherwise it returns `None`

#%%
for movie in movies:
    print(movie, pat.match(movie))

#%% [markdown]
# ### Advanced string replacing
#%% [markdown]
# As shown before `str.replace` probably covers a lot of your needs, for more advanced usage there is `re.sub`: 

#%%
text = '''Awesome, I am doing #100DaysOfCode, #200DaysOfDjango and of course #365DaysOfPyBites'''

# I want all challenges to be 100 days, I need a break!
text.replace('200', '100').replace('365', '100')

#%% [markdown]
# `re.sub` makes this easy:

#%%
re.sub(r'\d+', '100', text)

#%% [markdown]
# Or what if I want to change all the #nDaysOf... to #nDaysOfPython? You can use `re.sub` for this. Note how I use the capturing parenthesis to port over the matching part of the string to the replacement (2nd argument) where I use `\1` to reference it:

#%%
re.sub(r'(#\d+DaysOf)\w+', r'\1Python', text)

#%% [markdown]
# And that's a wrap. I only showed you some of the common `re` features I use day-to-day, but there is much more. I hope you got a taste for writing regexes in Python.
#%% [markdown]
# ## Second day: solidify what you've learned
# 
# A. We recommend reading [10 Tips to Get More out of Your Regexes](https://pybit.es/mastering-regex.html) + watching the Al Sweigart's PyCon talk: _Yes, It's Time to Learn Regular Expressions_, linked at the end. 
# 
# If you still have time check out [the mentioned HOWTO](https://docs.python.org/3.7/howto/regex.html#regex-howto) and the [docs](https://docs.python.org/3.7/library/re.html).
# 
# B. Write some regexes interactively using an online tool like [regex101](https://regex101.com/#python).
# 
#%% [markdown]
# ## Third day: put your new skill to the test!
# 
# A. Take [Bite 2. Regex Fun](https://codechalleng.es/bites/2/) which should be within reach after studying the materials. It let's you write 3 regexes. Like to work on your desktop? Maybe you can do [blog challenge 42 - Mastering Regular Expressions](https://codechalleng.es/challenges/42/) which is similar but let's you solve 6 regex problems!
# 
# B. More fun: `wget` or `request.get` your favorite site and use regex on the output to parse out data (fun trivia: a similar exercise is where [our code challenges started](https://pybit.es/js_time_scraper_ch.html)).
# 
# Good luck and remember: 
# 
# > Keep calm and code in Python
#%% [markdown]
# ### Time to share what you've accomplished!
# 
# Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfCode**. 
# 
# Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.
# 
# *See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofcode-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofcode-with-python-course/pulls).*

