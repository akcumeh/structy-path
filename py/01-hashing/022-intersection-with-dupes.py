def intersection_plus(a: list, b: list) -> list:
    # idea 1:
    # dict for each, compare occurrences, use the min value to append as required

    group_a = {}
    group_b = {}

    for item in a:
        if item in group_a:
            group_a[item] += 1
        else:
            group_a[item] = 1

    for item in b:
        if item in group_b:
            group_b[item] += 1
        else:
            group_b[item] = 1

    intersection = []

    for item in group_a:
        if item in group_b:
            intersection.extend([item]*min(group_a[item], group_b[item]))

    return intersection


# test cases
print(intersection_plus(
  ["a", "b", "c", "b"], 
  ["x", "y", "b", "b"]
)) # -> ["b", "b"]
print(intersection_plus(
  ["q", "b", "m", "s", "s", "s"], 
  ["s", "m", "s"]
)) # -> ["m", "s", "s"]
print(intersection_plus(
  ["p", "r", "r", "r"], 
  ["r"]
)) # -> ["r"]
print(intersection_plus(
  ["r"], 
  ["p", "r", "r", "r"]
)) # -> ["r"]
print(intersection_plus(
  ["t", "v", "u"], 
  ["g", "e", "d", "f"]
)) # -> [ ]
print(intersection_plus(
  ["a", "a", "a", "a", "a", "a",], 
  ["a", "a", "a", "a"]
)) # -> ["a", "a", "a", "a"]