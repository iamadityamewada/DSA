// Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
// palindrome
//  that can be built with those letters.

// Letters are case sensitive, for example, "Aa" is not considered a palindrome.

function longestPalindrome(s) {
    // Create an object to count the frequency of each character
    let charCount = {};
    
    // Iterate over each character in the string
    for (let char of s) {
        // Update the count of the character in the charCount object
        charCount[char] = (charCount[char] || 0) + 1;
    }
    console.log(charCount);
    let length = 0;
    let oddFound = false;
    
    // Iterate over the values in the charCount object
    for (let count of Object.values(charCount)) {
        if (count % 2 === 0) {
            // If the count is even, add it entirely to the length
            length += count;
        } else {
            // If the count is odd, add the largest even part of it to the length
            length += count - 1;
            // Mark that we found an odd count
            oddFound = true;
        }
    }
    
    // If there was any character with an odd count, we can place one in the middle
    if (oddFound) {
        length += 1;
    }
    
    // Return the calculated length of the longest palindrome
    return length;
}

// Example usage
let s = "abccccdd";
console.log(longestPalindrome(s)); // Output should be 7


 