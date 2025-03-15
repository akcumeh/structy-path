def exclusive_items(a: list, b: list) -> list:
    # starting to use stricter function definitions & parameters

    set_of_all = {}
    bougie_list = []

    for list_ in [a, b]:
        for i in list_:
            if i in set_of_all:
                set_of_all[i] += 1
            else:
                set_of_all[i] = 1

    for key, value in set_of_all.items():
        if value == 1:
            bougie_list.append(key)

    return bougie_list


# test cases
print(exclusive_items([4,2,1,6], [3,6,9,2,10])) # -> [4,1,3,9,10]
print(exclusive_items([2,4,6], [4,2])) # -> [6]
print(exclusive_items([4,2,1], [1,2,4,6])) # -> [6]
print(exclusive_items([0,1,2], [10,11])) # -> [0,1,2,10,11]
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
print(exclusive_items(a, b)) # -> [ ]