def pairs(elements: list):
    mega_list = []
    for i in range(len(elements)):
        j=i+1
        while j < len(elements):
            mega_list.append([elements[i], elements[j]])
            j+=1
    
    return mega_list


# Test cases
print(pairs(["a", "b", "c"])) # ->
# [
#    ["a", "b"],
#    ["a", "c"],
#    ["b", "c"]
# ]
print(pairs(["a", "b", "c", "d"])) # ->
# [
#    ["a", "b"],
#    ["a", "c"],
#    ["a", "d"],
#    ["b", "c"],
#    ["b", "d"],
#    ["c", "d"]
# ]
print(pairs(["cherry", "cranberry", "banana", "blueberry", "lime", "papaya"])) # ->
# [ 
#   [ "cherry", "cranberry" ], 
#   [ "cherry", "banana" ], 
#   [ "cherry", "blueberry" ], 
#   [ "cherry", "lime" ], 
#   [ "cherry", "papaya" ], 
#   [ "cranberry", "banana" ], 
#   [ "cranberry", "blueberry" ], 
#   [ "cranberry", "lime" ], 
#   [ "cranberry", "papaya" ], 
#   [ "banana", "blueberry" ], 
#   [ "banana", "lime" ], 
#   [ "banana", "papaya" ], 
#   [ "blueberry", "lime" ], 
#   [ "blueberry", "papaya" ], 
#   [ "lime", "papaya" ] 
# ] 
