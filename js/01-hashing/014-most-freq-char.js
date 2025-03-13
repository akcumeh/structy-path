function mostFreqChar(word){
    let count = {};
    let maxChar = '';
    let maxCount = 0;
    for (letter in word) {
        if (count[word[letter]]) {
            count[word[letter]]++;
        } else {
            count[word[letter]] = 1;
        };
    };

    for (letter in count) {
        if (count[letter] > maxCount) {
            maxCount = count[letter];
            maxChar = letter;
        };
    };

    return maxChar;
};


let testCases = [
    'bookkeeper', // 'e'
    'david', // 'd'
    'abby', // 'b'
    'mississippi', // 'i'
    'potato', // 'o'
    'eleventennine', // 'e'
];

for (let test of testCases) {
    console.log(mostFreqChar(test));
};

// runtime: 0.147s