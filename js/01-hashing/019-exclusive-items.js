function exclusiveItems(a, b) {
    let setOfAll = {};
    let bougieList = [];

    for (item of [a, b]) {
        for (let i = 0; i < item.length; i++) {
            if (setOfAll[item[i]]) {
                setOfAll[item[i]]++;
            } else {
                setOfAll[item[i]] = 1;
            };
        };
    };

    for (item in setOfAll) {
        if (setOfAll[item] == 1) {
            bougieList.push(parseInt(item));
        }
    };

    return bougieList;
};

// test cases
console.log(exclusiveItems([4, 2, 1, 6], [3, 6, 9, 2, 10])) // -> [4, 1, 3, 9, 10]
console.log(exclusiveItems([2, 4, 6], [4, 2])) // -> [6]
console.log(exclusiveItems([4, 2, 1], [1, 2, 4, 6])) // -> [6]
console.log(exclusiveItems([0, 1, 2], [10, 11])) // -> [0, 1, 2, 10, 11]
console.log(exclusiveItems([1, 1, 3, 4], [1, 2, 3, 4])) // -> [2]