function longestWord(sentence) {
    let max_word = "";
    let words = sentence.split(" ");

    for (word of words) {
        if (word.length >= max_word.length) {
            max_word = word;
        };
    };

    return max_word;
}

console.log(longestWord("what a wonderful world"));
console.log(longestWord("have a nice day"));
console.log(longestWord("the quick brown fox jumped over the lazy dog"));
console.log(longestWord("who did eat the ham"));
console.log(longestWord("potato"));