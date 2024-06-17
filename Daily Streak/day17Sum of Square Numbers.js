// 633. Sum of Square Numbers
// Medium
// Topics
// Companies
// Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

// Example 1:

// Input: c = 5
// Output: true
// Explanation: 1 * 1 + 2 * 2 = 5
// Example 2:

// Input: c = 3
// Output: false
 

// Constraints:

// 0 <= c <= 231 - 1

//mine solution


// Do it again 

/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function(c) {
    let a = 0;
  let b = Math.floor(Math.sqrt(c));
  
  while (a <= b) {
      let sum = a * a + b * b;
      if (sum === c) {
          return true;
      } else if (sum < c) {
          a++;
      } else {
          b--;
      }
  }
  return false;

};


javascript
/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function(c) {
    let i = 0;
    let j = Math.ceil(Math.sqrt(c));
    while(i<=j){
        let sum = i*i + j*j;
        if(sum < c){
            i++;
        }else if (sum > c){
            j--;
        }else{
            return true;
        }
    