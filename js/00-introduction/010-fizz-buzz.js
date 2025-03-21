function fizzBuzz(number) {
    let fizzBuzzList = [];

    for (let i = 1; i <= number; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            fizzBuzzList.push("fizzbuzz");
        } else if (i % 3 === 0) {
            fizzBuzzList.push("fizz");
        } else if (i % 5 === 0) {
            fizzBuzzList.push("buzz");
        } else {
            fizzBuzzList.push(i);
        }
    };
    
    return fizzBuzzList;
};

// test cases
fizzBuzz(11) // -> [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11]
fizzBuzz(2) // -> [1, 2]
fizzBuzz(16) // -> [
//   1,
//   2,
//   "fizz",
//   4,
//   "buzz",
//   "fizz",
//   7,
//   8,
//   "fizz",
//   "buzz",
//   11,
//   "fizz",
//   13,
//   14,
//   "fizzbuzz",
//   16
//]
fizzBuzz(32) // -> [
//   1, 2, "fizz", 4, 
//   "buzz", "fizz", 7, 8, 
//   "fizz", "buzz", 11, "fizz", 
//   13, 14, "fizzbuzz", 16, 
//   17, "fizz", 19, "buzz", 
//   "fizz", 22, 23, "fizz", 
//   "buzz", 26, "fizz", 28, 
//   29, "fizzbuzz", 31, 32 
//] 
