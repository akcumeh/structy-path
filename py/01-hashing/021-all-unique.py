def all_unique(l):
    all_items = {}

    for item in l:
        if item in all_items:
            return False
        else:
            all_items[item] = 1

    return True


# test cases
print(all_unique(["q", "r", "s", "a"])) # -> True
print(all_unique(["q", "r", "s", "a", "r", "z"])) # -> False
print(all_unique(["red", "blue", "yellow", "green", "orange"])) # -> True
print(all_unique(["cat", "cat", "dog"])) # -> False
print(all_unique(["a", "u", "t", "u", "m", "n"])) # -> False
print(all_unique("spring".split())) # -> True