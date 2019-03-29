# Create a program that takes in some text and returns a list of all of the characters
# used in the text that are not vowels, sorted in alphabetical order


jabberwocky = """
Beware the Jabberwock, my son! 
      The jaws that bite, the claws that catch! 
Beware the Jubjub bird, and shun 
      The frumious Bandersnatch!
"""

vowels = frozenset({"aeiou"})
poemCharacters = set(jabberwocky)
print(sorted(poemCharacters - vowels))
