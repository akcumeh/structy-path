function maxValue(numList){
    let max = numList[0];
    for (let i = 1; i < numList.length; i++){
        if (numList[i] > max){
            max = numList[i];
        };
    }
    return max;
}

let testCases = [
    [4, 7, 2, 8, 10, 9], // 10
    [10,5, 40, 40.3], // 40.3
    [-5, -2, -1, -11], // -1
    [42], // 42
    [1000, 8], // 1000
    [1000, 8, 9000], // 9000
    [2, 5, 1, 1, 4], // 5
];

for (let i = 0; i < testCases.length; i++) {
    console.log(maxValue(testCases[i]));
}