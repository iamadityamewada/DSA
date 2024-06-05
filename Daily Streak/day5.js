// 1002. Find Common Characters
// Easy
// Topics
// Companies
// Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

// Example 1:

// Input: words = ["bella","label","roller"]
// Output: ["e","l","l"]
// Example 2:

// Input: words = ["cool","lock","cook"]
// Output: ["c","o"]
 

// Constraints:

// 1 <= words.length <= 100
// 1 <= words[i].length <= 100
// words[i] consists of lowercase English letters.



/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    function countChars(word) {
        let countChar = {};
        for (let char of word) {
            countChar[char] = (countChar[char] || 0) + 1;
        }
        return countChar;
    }

    // Initialize the counter with the first word
    let commonCounter = countChars(words[0]);

    // Update the counter with the minimum count of each character in each word
    for (let i = 1; i < words.length; i++) {
        const wordCount = countChars(words[i]);
        for (let char in commonCounter) {
            if (wordCount[char]) {
                commonCounter[char] = Math.min(commonCounter[char], wordCount[char]);
            } else {
                delete commonCounter[char];
            }
        }
    }

    // Expand the characters into a list
    let res = [];
    for (let char in commonCounter) {
        for (let i = 0; i < commonCounter[char]; i++) {
            res.push(char);
        }
    }

    return res;
};

// Example usage
let words = ["bella", "label", "roller"];
console.log(commonChars(words));  // Output: ["e", "l", "l"]



// fastest approach 
/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    let arr=[];

    let firstIndex = words[0];

    firstIndex.split('').forEach((item, index) => {
        if (words.every(word => word.includes(item))) {
            arr.push(item);
            words = words.map(word => word.replace(item, ''));
        }
    });

    return arr;
};