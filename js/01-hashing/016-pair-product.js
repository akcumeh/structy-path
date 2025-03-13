function pairProduct(nums, target) {
    let seenNums = {};
    let pair;
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        let complement = target / num;
        if (complement in seenNums) {
            pair = [seenNums[complement], i];
            return pair;
        };
        seenNums[num] = i;
    };
};

let testCases = [
    [[3, 2, 5, 4, 1], 8],
    [[3, 2, 5, 4, 1], 10],
    [[4, 7, 9, 2, 5, 1], 5],
    [[4, 7, 9, 2, 5, 1], 35],
    [[3, 2, 5, 4, 1], 10],
    [[4, 6, 8, 2], 16],
];

for (test of testCases) {
    console.log(pairProduct(test[0], test[1]));
};