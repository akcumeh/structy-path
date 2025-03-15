def intersection(a, b):
    common = [];
    all_el = {};

    for item in [a, b]:
        for i in range(len(item)):
            if item[i] in all_el.keys():
                all_el[item[i]]+=1
            else:
                all_el[item[i]] = 1
    
    for key in all_el:
        if key > 1:
            common.append(key)

    print(common)
    return common


# testcases
intersection([4,2,1,6], [3,6,9,2,10]) # [2,6]
intersection([2,4,6], [4,2]) # [2,4]
intersection([4,2,1], [1,2,4,6]) # [1,2,4]
intersection([0,1,2], [10,11]) # []
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
intersection(a, b) # -> [0,1,2,3,..., 49999]
