def max_value(num_list):
    max_val = num_list[0]
    for num in num_list:
        if num > max_val:
            max_val = num
    return max_val


test_cases = [
    [4, 7, 2, 8, 10, 9], # 10
    [10,5, 40, 40.3], # 40.3
    [-5, -2, -1, -11], # -1
    [42], # 42
    [1000, 8], # 1000
    [1000, 8, 9000], # 9000
    [2, 5, 1, 1, 4], # 5
]

for i in test_cases:
    print(max_value(i))