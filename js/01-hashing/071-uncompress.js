function uncompress(word) {
    let uncompressed = "";
    let i = 0, j = 0;

    while (j < word.length) {
        if ("abcdefghijklmnopqrstuvwxyz".includes(word[j])) {
            uncompressed += word[j].repeat(parseInt(word.substring(i, j)));
            i = j + 1;
        }
        j += 1;
    }
    console.log(uncompressed);
    return uncompressed;
}

// Test cases
uncompress("2c3a1t") //'ccaaat'
uncompress("4s2b") //'ssssbb'
uncompress("2p1o5p") //'ppoppppp'
uncompress("3n12e2z") //'nnneeeeeeeeeeeezz'
uncompress("127y") //'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
uncompress("10a") //'aaaaaaaaaa'