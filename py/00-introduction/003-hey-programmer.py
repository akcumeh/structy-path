def greet(s):
    s="hey "+s

    return s


test_cases = [
    "alvin",
    "jason",
    "how now brown cow",
]
for i in test_cases:
    print(greet(i))