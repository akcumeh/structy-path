def uncompress(str):
    uncompressed = ""
    i=0
    j=0

    while j < len(str):
        if str[j] in "abcdefghijklmnopqrstuvwxyz":
            uncompressed += str[j] * int(str[i:j])
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