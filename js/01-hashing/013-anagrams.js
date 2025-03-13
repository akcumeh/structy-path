const counter = (word) => {
    let letterCount = {};
    for (let i = 0; i < word.length; i++) {
        if (!(word[i] in letterCount)) {
            letterCount[word[i]] = 1;
        } else {
            letterCount[word[i]]++;
        };
    };

    return letterCount;
};

function anagrams(str1, str2) {
    const counter1 = counter(str1);
    const counter2 = counter(str2);
    
    if (Object.keys(counter1).length !== Object.keys(counter2).length) {
        return false;
    }
    
    for (let letter in counter1) {
        if (counter1[letter] !== counter2[letter]) {
            return false;
        }
    }
    
    return true;
};

export default anagrams;

console.log(anagrams('restful', 'fluster')); // true
console.log(anagrams('cats', 'tocs')); // false
console.log(anagrams('monkeyswrite', 'newyorktimes')); // true
console.log(anagrams('paper', 'reapa')); // false
console.log(anagrams('elbow', 'below')); // true
console.log(anagrams('tax', 'taxi')); // false
console.log(anagrams('taxi', 'tax')); // false
console.log(anagrams('night', 'thing')); // true
console.log(anagrams('abbc', 'aabc')); // false
console.log(anagrams('po', 'popp')); // false
console.log(anagrams('pp', 'oo')); // false