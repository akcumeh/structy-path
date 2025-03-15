function allUnique(l) {
    let all = {};

    for (item in l) {
        if (all[l[item]]) {
            return false;
        } else {
            all[l[item]] = 1;
        }
    };

    return true;
};

// test cases
console.log(allUnique(["q", "r", "s", "a"])) // -> True
console.log(allUnique(["q", "r", "s", "a", "r", "z"])) // -> False
console.log(allUnique(["red", "blue", "yellow", "green", "orange"])) // -> True
console.log(allUnique(["cat", "cat", "dog"])) // -> False
console.log(allUnique(["a", "u", "t", "u", "m", "n"])) // -> False
console.log(allUnique("spring".split())) // -> True