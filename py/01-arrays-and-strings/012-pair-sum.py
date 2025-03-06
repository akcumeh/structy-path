# Write a function, pair_sum, that takes in a list and a target sum as args.

# The function should return a tuple containing a pair of indices whose
# elements sum to the given target.
# The indices returned must be unique.
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair that sums to the target.


def pair_sum(nums, target):
    seen_nums = {}
    pair = ()
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in seen_nums:
            pair = (seen_nums[complement], i)
            print(pair)
            return pair
        
        seen_nums[num] = i


# Test cases
pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
pair_sum([1, 6, 7, 2], 13) # -> (1, 2)
pair_sum([9, 9], 18) # -> (0, 1)
pair_sum([6, 4, 2, 8 ], 12) # -> (1, 3)
