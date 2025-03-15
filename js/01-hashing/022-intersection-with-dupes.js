function intersectionPlus(a, b) {
    let hash_a = {};
    let hash_b = {};
    let result = [];
    for (let i = 0; i < a.length; i++) {
        if (!hash_a[i]) {
            hash_a[i] = 1;
        } else {
            hash_a[i]++;
        };
    };

    for (let i = 0; i < b.length; i++) {
        if (!hash_b[i]) {
            hash_b[i] = 1;
        } else {
            hash_b[i]++;
        };
    };

    for (key in hash_a) {
        if (hash_b[hash_a[key]]) {
            let i=0;
            while (i<=Math.min(hash_a[key], hash_b[key])) {
                result.push(hash_b[key]);
                i++;
            };
        };
    };

    return result;
};

// test cases
console.log(intersectionPlus(
    ["a", "b", "c", "b"],
    ["x", "y", "b", "b"]
)) // -> ["b", "b"]
console.log(intersectionPlus(
    ["q", "b", "m", "s", "s", "s"],
    ["s", "m", "s"]
)) // -> ["m", "s", "s"]
console.log(intersectionPlus(
    ["p", "r", "r", "r"],
    ["r"]
)) // -> ["r"]
console.log(intersectionPlus(
    ["r"],
    ["p", "r", "r", "r"]
)) // -> ["r"]
console.log(intersectionPlus(
    ["t", "v", "u"],
    ["g", "e", "d", "f"]
)) // -> []
console.log(intersectionPlus(
    ["a", "a", "a", "a", "a", "a",],
    ["a", "a", "a", "a"]
)) // -> ["a", "a", "a", "a"]