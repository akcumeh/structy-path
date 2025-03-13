# Write a function, pair_product, that takes in a list and a target product as
# arguments.

# The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair whose product is the target.

def pair_product(nums, target):
    seen_nums = {}
    pair = ()
    for i in range(len(nums)):
        num = nums[i]
        complement = target / num
        if complement in seen_nums:
            pair = (seen_nums[complement], i)
            print(pair)
            return pair
        
        seen_nums[num] = i


# Test cases
pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
pair_product([4, 7, 9, 2, 5, 1], 5) # -> (4, 5)
pair_product([4, 7, 9, 2, 5, 1], 35) # -> (1, 4)
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
pair_product([4, 6, 8, 2], 16) # -> (2, 3)
pair_product([ i for i in range(1, 6001) ], 35994000) # -> (5998, 5999) 
