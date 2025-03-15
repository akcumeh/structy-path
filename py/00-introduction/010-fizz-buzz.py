def fizz_buzz(number):
    fizz_buzz_list = []

    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_list.append("fizzbuzz")
        elif i % 3 == 0:
            fizz_buzz_list.append("fizz")
        elif i % 5 == 0:
            fizz_buzz_list.append("buzz")
        else:
            fizz_buzz_list.append(i)
            
    print(fizz_buzz_list)
    return fizz_buzz_list


# test cases
fizz_buzz(11) # -> [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11]
fizz_buzz(2) # -> [1,2]
fizz_buzz(16) # -> [
#   1,
#   2,
#   "fizz",
#   4,
#   "buzz",
#   "fizz",
#   7,
#   8,
#   "fizz",
#   "buzz",
#   11,
#   "fizz",
#   13,
#   14,
#   "fizzbuzz",
#   16
# ]
fizz_buzz(32) # -> [
#   1,      2,          "fizz",     4, 
#   "buzz", "fizz",     7,          8, 
#   "fizz", "buzz",     11,         "fizz", 
#   13,     14,         "fizzbuzz", 16, 
#   17,     "fizz",     19,         "buzz", 
#   "fizz", 22,         23,         "fizz", 
#   "buzz", 26,         "fizz",     28, 
#   29,     "fizzbuzz", 31,         32 
# ] 
