function greet(s) {
    s = "hey "+s
    return s;
};


let testCases = [
    "alvin",
    "jason",
    "how now brown cow",
];

for (let i=0; i<testCases.length; i++) {
    console.log(greet(testCases[i]));
};