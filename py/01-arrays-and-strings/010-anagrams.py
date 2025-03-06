# Problem Statement

# Write a function, anagrams, that takes in two strings as arguments.
# The function should return a boolean indicating whether or not the strings
# are anagrams.
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    isAnagram = (counter(s1) == counter(s2))
    print(isAnagram)
    return isAnagram


def counter(string):
    count = {}
    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count


# Test cases
anagrams('restful', 'fluster') # -> True
anagrams('cats', 'tocs') # -> False
anagrams('monkeyswrite', 'newyorktimes') # -> True
anagrams('paper', 'reapa') # -> False
anagrams('elbow', 'below') # -> True
anagrams('tax', 'taxi') # -> False
anagrams('taxi', 'tax') # -> False
anagrams('night', 'thing') # -> True
anagrams('abbc', 'aabc') # -> False
anagrams('po', 'popp') # -> false
anagrams('pp', 'oo') # -> false
