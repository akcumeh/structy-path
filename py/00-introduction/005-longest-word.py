def longest_word(sentence):
    max_word = ""    
    words = sentence.split(" ")

    for word in words:
        if len(word) >= len(max_word):
            max_word = word
    
    print(max_word)
    return max_word

longest_word("what a wonderful world") # -> "wonderful"
longest_word("have a nice day") # -> "nice"
longest_word("the quick brown fox jumped over the lazy dog") # -> "jumped"
longest_word("who did eat the ham") # -> "ham"
longest_word("potato") # -> "potato"
