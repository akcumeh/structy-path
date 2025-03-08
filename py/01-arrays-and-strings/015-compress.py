def compress(word):
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

def compress2(word):
    compressed2=""
    holder=word[0]

    for i in range(len(word)):
        if word[i-1] == word[i]:
            holder+=word[i]
        else:
            compressed2+=str(len(holder))+holder[-1]
            holder=""
    
    print(compressed2)
    return

compress2('ccaaatsss') # -> '2c3at3s'
compress2('ssssbbz') # -> '4s2bz'
compress2('ppoppppp') # -> '2po5p'
compress2('nnneeeeeeeeeeeezz') # -> '3n12e2z'
compress2('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); 
# -> '127y'