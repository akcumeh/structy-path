function isPrime(number){
    if (number < 2) return false;
    for (let i=2; i<number; i++) {
        if (number%i == 0) return false;
    };
    return true;
};

function isPrime2(number) {
    if (number < 2) return false;
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i == 0) return false;
    };
    return true;
};

let testCases = [
    2, // true
    3, // true
    4, // false
    5, // true
    6, // false
    7, // true
    8, // false
    25, // false
    31, // true
    2017, // true
    2048, // false
    1, // false
    713,  // false
];

for (i in testCases) {
    console.log(`${isPrime(testCases[i])} - ${testCases[i]}`);
    // console.log(`${isPrime2(testCases[i])} - ${testCases[i]}`);
    console.log("\n");
};