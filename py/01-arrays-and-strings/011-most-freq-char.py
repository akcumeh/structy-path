# Write a function, most_frequent_char that takes in a string as an argument.
# 
# The function should return the most frequent character of the string.
# If there are ties, return the character that appears earlier in the string.

def most_frequent_char(string):
    count = {}
    maxChar = ''
    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    maxCount = 0
    for letter in count:
        if count[letter] > maxCount:
            maxCount = count[letter]
            maxChar = letter
    
    print(maxChar)
    return maxChar


# Test cases
most_frequent_char('bookeeper') # -> 'e'
most_frequent_char('david') # -> 'd'
most_frequent_char('abby') # -> 'b'
most_frequent_char('mississippi') # -> 'i'
most_frequent_char('potato') # -> 'o'
most_frequent_char('eleventennine') # -> 'e'
most_frequent_char('riverbed') # -> 'r'
