function pairs(elements) {
    let megaList = [];
    for (let i = 0; i < elements.length; i++) {
        let j = i + 1;
        while (j < elements.length) {
            megaList.push([elements[i], elements[j]]);
            j++;
        };
    };

    return megaList;
};

//  Test cases
console.log(pairs(["a", "b", "c"])) //  ->
// [
// ["a", "b"],
// ["a", "c"],
// ["b", "c"]
//  ]
console.log(pairs(["a", "b", "c", "d"])) //  ->
// [
// ["a", "b"],
// ["a", "c"],
// ["a", "d"],
// ["b", "c"],
// ["b", "d"],
// ["c", "d"]
//  ]
console.log(pairs(["cherry", "cranberry", "banana", "blueberry", "lime", "papaya"])) //  ->
// [ 
// ["cherry", "cranberry"], 
// ["cherry", "banana"], 
// ["cherry", "blueberry"], 
// ["cherry", "lime"], 
// ["cherry", "papaya"], 
// ["cranberry", "banana"], 
// ["cranberry", "blueberry"], 
// ["cranberry", "lime"], 
// ["cranberry", "papaya"], 
// ["banana", "blueberry"], 
// ["banana", "lime"], 
// ["banana", "papaya"], 
// ["blueberry", "lime"], 
// ["blueberry", "papaya"], 
// ["lime", "papaya"] 
//  ] 
