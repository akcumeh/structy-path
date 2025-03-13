def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if (number%i == 0):
            return False
        
    return True


import math


def is_prime_2(number):
    if number < 2:
        return False
    for i in range(2, math.floor(math.sqrt(number)+1)):
        if (number%i == 0):
            return False
        
    return True


testCases = [
    2, # true
    3, # true
    4, # false
    5, # true
    6, # false
    7, # true
    8, # false
    25, # false
    31, # true
    2017, # true
    2048, # false
    1, # false
    713,  # false
]

for test in testCases:
    # print(is_prime(test), "-", test)
    print(is_prime_2(test), "-", test)


# is_prime runtime: 0.328s
# is_prime_2 runtime: 0.138s