# structy-path
Learning data structures & algorithms on Structy.net

## Table of Contents
| Section | Problem | Solution | 
|---------|---------|----------|
| [01 - Arrays & Strings](#01---arrays--strings) | [010-anagrams](#010---anagrams) | [py](./py/01-arrays-and-strings/010-anagrams.py) / [js](./js/01-arrays-and-strings/010-anagrams.js) |
|  | [011-most-freq-char](#011---most-frequent-char) | [py](./py/01-arrays-and-strings/011-most-freq-char.py) / [js](./js/01-arrays-and-strings/011-most-freq-char.js) | 
|  | [012-pair-sum](#012---pair-sum) | [py](./py/01-arrays-and-strings/012-pair-sum.py) / [js](./js/01-arrays-and-strings/012-pair-sum.js) | 
|  | [013-pair-product](#013---pair-product) | [py](./py/01-arrays-and-strings/013-pair-product.py) / [js](./js/01-arrays-and-strings/013-pair-product.js) | 
|  | [014-uncompress](#014---uncompress) | [py](./py/01-arrays-and-strings/014-uncompress.py) / [js](./js/01-arrays-and-strings/014-uncompress.js) | 
|  | [015-compress](#015---compress) | [py](./py/01-arrays-and-strings/015-compress.py) / [js](./js/01-arrays-and-strings/015-compress.js) | 
| [02 - Beginner Recursion]() | [024-sum-numbers-recursive](#024---sum-numbers-recursive) | [py](./py/02-beginner-recursion/024-sum-numbers-recursive.py) / [js](./js/02-beginner-recursion/024-sum-numbers-recursive.js) | 
|  | [025-factorial](#025---factorial) | [py](./py/02-beginner-recursion/025-factorial.py) / [js](./js/02-beginner-recursion/025-factorial.js) | 

## 01 - Arrays & Strings

### [010 - anagrams](https://structy.net/problems/anagrams)
#### Problem
Write a function, anagrams, that takes in two strings as arguments.
The function should return a boolean indicating whether or not the strings are anagrams.
Anagrams are strings that contain the same characters, but in any order.

#### Solutions
[Solution - py](./py/01-arrays-and-strings/010-anagrams.py)
![All Testcases Passed - py](./assets/010-anagrams.py.png)

[Solution - js](./js/01-arrays-and-strings/010-anagrams.js)
![All Testcases Passed - js](./assets/010-anagrams.js.png)

### [011 - most frequent char](https://structy.net/problems/most-frequent-char)
#### Problem
Write a function, most_frequent_char that takes in a string as an argument.
The function should return the most frequent character of the string.
If there are ties, return the character that appears earlier in the string.

#### Solutions
[Solution - py](./py/01-arrays-and-strings/011-most-freq-char.py)
![All Testcases Passed - py](./assets/011-most-freq-char.py.png)

[Solution - js](./js/01-arrays-and-strings/011-most-freq-char.js)
![All Testcases Passed - js](./assets/011-most-freq-char.js.png)

### [012 - pair sum](https://structy.net/problems/pair-sum)
#### Problem
Write a function, pair_sum, that takes in a list and a target sum as args.

The function should return a tuple containing a pair of indices whose elements sum to the given target.
The indices returned must be unique.
Be sure to return the indices, not the elements themselves.
There is guaranteed to be one such pair that sums to the target.

#### Solutions
[Solution - py](./py/01-arrays-and-strings/012-pair-sum.py)
![All Testcases Passed](./assets/012-pair-sum.py.png)

[Solution - js](./js/01-arrays-and-strings/012-pair-sum.js)
![All Testcases Passed](./assets/012-pair-sum.js.png)

### [013 - pair product](https://structy.net/problems/pair-product)
#### Problem
Write a function, pair_product, that takes in a list and a target product as arguments.

The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.
Be sure to return the indices, not the elements themselves.
There is guaranteed to be one such pair whose product is the target.

#### Solutions
[Solution - py](./py/01-arrays-and-strings/013-pair-product.py)
![All Testcases Passed](./assets/013-pair-product.py.png)

### [014 - uncompress](https://structy.net/problems/uncompress)
#### Problem
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

```
<number><char>

for example, '2c' or '3a'.
```

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

#### Solutions
[Solution - py](./py/01-arrays-and-strings/014-uncompress.py)
![All Testcases Passed](./assets/014-uncompress.py.png)

### [015 - compress](https://structy.net/problems/compress)
#### Problem
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

```
'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
```

You can assume that the input only contains alphabetic characters.

#### Solutions(es?)
[Solution - py](./py/01-arrays-and-strings/015-compress.py)
![All Testcases Passed](./assets/015-compress.py.png)


#### Break in Transmission...
Me when I switch to py for 3 seconds:
![context switcher](./py/assets/context-switcher.png)


## 02 - Beginner Recursion
### [024 - sum numbers recursive](https://structy.net/problems/sum-numbers-recursive)
#### Problem
Problem

#### Solutions
[Solution - py]()

[Solution - js]()

### [025 - factorial](https://structy.net/problems/factorial)
#### Problem
Problem

#### Solutions
[Solution - py]()

[Solution - js]()