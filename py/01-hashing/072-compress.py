def compress(word):
    # brute force attempt 2
    compressed = ""
    letters = ""
    counts = []

    for i in range(len(word)):
        if i==0:
            letters+=word[i]
            counts.append(1)
        elif word[i] == word[i-1]:
            counts[len(letters)-1] += 1
        elif word[i] != word[i-1]:
            letters += word[i]
            counts.append(1)

    for j in range(len(counts)):
        if counts[j] > 1:
            compressed+=str(counts[j])+letters[j]
        else:
            compressed+=letters[j]

    print(compressed)
    return compressed

# Test cases
compress('ccaaatsss') # -> '2c3at3s'
compress('ssssbbz') # -> '4s2bz'
compress('ppoppppp') # -> '2po5p'
compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); 
# -> '127y'
print('\n')

def compress2(word):
    # with approach & walkthrough videos
    compressed2=""
    i=0
    j=0
    
    while j < len(word):
        if word[i] == word[j]:
            j+=1
        else:
            count = j-i
            if count > 1:
                compressed2+=str(j-i)+word[i]
            else:
                compressed2+=word[i]
            i=j
        if j == len(word)-1:
            if count > 1:
                compressed2+=str(j-i)+word[i]
            else:
                compressed2+=word[i]

    print(compressed2)
    return compressed2

compress2('ccaaatsss') # -> '2c3at3s'
compress2('ssssbbz') # -> '4s2bz'
compress2('ppoppppp') # -> '2po5p'
compress2('nnneeeeeeeeeeeezz') # -> '3n12e2z'
compress2('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); 
# -> '127y'