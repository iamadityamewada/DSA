// Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

// Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

// Example 1:

// Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
// Output: true
// Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
// Example 2:

// Input: hand = [1,2,3,4,5], groupSize = 4
// Output: false
// Explanation: Alice's hand can not be rearranged into groups of 4.


var isNStraightHand = function(hand, W) {
    if (hand.length % W !== 0) {
        return false;
    }
    
    // Count the frequency of each card using a simple object
    let count = {};
    for (let card of hand) {
        count[card] = (count[card] || 0) + 1;
    }
    
    // Get all unique cards and sort them
    let uniqueCards = Object.keys(count).map(Number).sort((a, b) => a - b);
    
    for (let card of uniqueCards) {
        // If the current card count is greater than 0, try to form a group
        if (count[card] > 0) {
            let num = count[card];
            for (let i = 0; i < W; i++) {
                let currentCard = card + i;
                if (count[currentCard] === undefined || count[currentCard] < num) {
                    return false;
                }
                count[currentCard] -= num;
            }
        }
    }
    
    return true;
};

// Example usage:
console.log(isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)); // true
console.log(isNStraightHand([1, 2, 3, 4, 5], 4)); // false



// another approach
/**
 * @param {number[]} hand
 * @param {number} groupSize
 * @return {boolean}
 */
 /*

 [1, 2, 4, 5] k = 2


 */
 var isNStraightHand = function(hand, groupSize) {
    if (hand.length % groupSize !== 0) {
      return false;
    }
  
    const countMap = new Map();
  
    // Count the occurrences of each card
    for (const card of hand) {
      countMap.set(card, (countMap.get(card) || 0) + 1);
    }
  
    // Sort the cards in ascending order
    hand.sort((a, b) => a - b);
  
    for (const card of hand) {
      if (countMap.get(card) === 0) {
        // Skip cards that have been used in previous groups
        continue;
      }
  
      // Check if we can form a group of consecutive cards
      for (let i = 0; i < groupSize; i++) {
        const currCard = card + i;
  
        if (countMap.get(currCard) === undefined || countMap.get(currCard) === 0) {
          // If any card in the group is missing, return false
          return false;
        }
  
        // Reduce the count of the current card in the map
        countMap.set(currCard, countMap.get(currCard) - 1);
      }
    }
  
    return true;
  } 