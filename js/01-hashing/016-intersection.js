const intersection = (a, b) => {
    let common = new Array();
    let all = {};

    for (item of [a, b]) {
        for (let i = 0; i < item.length; i++) {
            if (all[item[i]]) {
                all[item[i]] += 1;
            } else {
                all[item[i]] = 1;
            };
        };
    };

    for (key in all) {
        if (all[key] > 1) {
            common.push(parseInt(key));
        };
    };

    return common;
};

console.log(intersection([4, 2, 1, 6], [3, 6, 9, 2, 10])) // -> [2,6]
console.log(intersection([2, 4, 6], [4, 2])) // -> [2,4]
console.log(intersection([4, 2, 1], [1, 2, 4, 6])) // -> [1,2,4]
console.log(intersection([0, 1, 2], [10, 11])) // -> []

const a = [];
const b = [];
for (let i = 0; i < 50000; i += 1) {
    a.push(i);
    b.push(i);
};
console.log(intersection(a, b));