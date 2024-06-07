// 648. Replace Words
// Medium
// Topics
// Companies
// In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

// Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

// Return the sentence after the replacement.

 

// Example 1:

// Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
// Output: "the cat was rat by the bat"
// Example 2:

// Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
// Output: "a a b c"
 

// Constraints:

// 1 <= dictionary.length <= 1000
// 1 <= dictionary[i].length <= 100
// dictionary[i] consists of only lower-case letters.
// 1 <= sentence.length <= 106
// sentence consists of only lower-case letters and spaces.
// The number of words in sentence is in the range [1, 1000]
// The length of each word in sentence is in the range [1, 1000]
// Every two consecutive words in sentence will be separated by exactly one space.
// sentence does not have leading or trailing spaces.

/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
function replaceWords(dictionary, sentence) {
    let dicSet = new Set(dictionary);
    words = sentence.split(" ");
    function findShortestRoot(word){
        for(let i =0;i<word.length;i++){
            const prefix = word.substring(0,i);
            if(dicSet.has(prefix)){
                return prefix;
            }
               
            }
             return word;   
    }
    let newWords = words.map((word)=> findShortestRoot(word));
    return newWords.join(" ");
}



// Example Usage
const dictionary = ["cat", "bat", "rat"];
const sentence = "the cattle was rattled by the battery";
console.log(replaceWords(dictionary, sentence));  // Output: "the cat was rat by the bat"


// another approach
var Trie = function() {
    this.trie = new Map();
};

/** 
 * @param {string} word
 * @return {void}
 */

Trie.prototype.insert = function(word) {
    let pointer = this.trie;

    for (let i = 0; i < word.length; i++) {
        const char = word[i];

        if (pointer.has(char)) {
            pointer = pointer.get(char);
        } else {
            pointer.set(char, new Map());
            pointer = pointer.get(char);
        }
    }

    pointer.set('isEnd', true);
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let pointer = this.trie;
    let word = '';

    for (let i = 0; i < prefix.length; i++) {
        const char = prefix[i];

        if (pointer.has(char)) {
            word += char;
            pointer = pointer.get(char);
            if (pointer.get('isEnd')) return word;
        } else {
            return prefix;
        }
    }

    return word;
};

/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */

var replaceWords = function(dictionary, sentence) {
    sentence = sentence.split(' ');
    const trie = new Trie();

    for (const word of dictionary) {
        trie.insert(word);
    }

    for (let i = 0; i < sentence.length; i++) {
        sentence[i] = trie.startsWith(sentence[i]);
    } 
}    
