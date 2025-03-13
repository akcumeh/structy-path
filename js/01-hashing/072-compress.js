function compress(word) {
    let compressed = new String();
    let i = 0;
    let j = 0;

    while (j < word.length) {
        if (word[i] == word[j]) {
            j++;
        } else {
            if ((j - i) > 1) {
                compressed += (j - i) + word[i];
            } else {
                compressed += word[i];
            };
            i = j;
        };
        if (j == word.length) {
            if ((j - i) > 1) {
                compressed += (j - i) + word[i];
            }
            else {
                compressed += word[i];
            };
        };
    };

    return compressed;
};

// Test Cases
console.log(compress('ccaaatsss')); // '2c3at3s'
console.log(compress('ssssbbz')); // '4s2bz'
console.log(compress('ppoppppp')); // '2po5p'
console.log(compress('nnneeeeeeeeeeeezz')); // '3n12e2z'
console.log(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'));
// '127y'