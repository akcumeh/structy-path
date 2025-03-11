def uncompress(word):
    uncompressed = ""
    i=0
    j=0

    while j < len(word):
        if word[j] in "abcdefghijklmnopqrstuvwxyz":
            uncompressed += word[j] * int(word[i:j])
            i=j+1
        j+=1

    print(uncompressed)
    return uncompressed


# Test cases
uncompress("2c3a1t") # -> 'ccaaat'
uncompress("4s2b") # -> 'ssssbb'
uncompress("2p1o5p") # -> 'ppoppppp'
uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
uncompress("10a") # -> 'aaaaaaaaaa'