function pairSum(nums, target) {
    let seenNums = {};
    let pair;
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        let complement = target - num;
        if (complement in seenNums) {
            pair = [seenNums[complement], i];
            return pair;
        };
        seenNums[num] = i;
    };
};

const longNums = [];
for (let i = 1; i<=30000; i++) {
    longNums.push(i);
};
let testCases = [
    [[3, 2, 5, 4, 1], 8],
    [[4, 7, 9, 2, 5, 1], 5],
    [[4, 7, 9, 2, 5, 1], 3],
    [[1, 6, 7, 2], 13],
    [[9, 9], 18],
    [[4, 5, 6], 11],
    [[6, 4, 2, 8], 12],
    [longNums, 59999]
];

for (test of testCases) {
    console.log(pairSum(test[0], test[1]));
};