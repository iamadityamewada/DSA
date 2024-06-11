// 1122. Relative Sort Array
// Easy
// Topics
// Companies
// Hint
// Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

// Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

// Example 1:

// Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
// Output: [2,2,2,1,4,3,3,9,6,7,19]
// Example 2:

// Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
// Output: [22,28,8,6,17,44]
 

// Constraints:

// 1 <= arr1.length, arr2.length <= 1000
// 0 <= arr1[i], arr2[i] <= 1000
// All the elements of arr2 are distinct.
// Each arr2[i] is in arr1.


var relativeSortArray = function(arr1, arr2) {
  let resArr = [];
  let remainingElems = [];

  // Iterate through arr2 and build resArr with elements from arr1
  arr2.forEach((val) => {
      arr1.forEach((ele, index) => {
          if (ele === val) {
              resArr.push(ele);
          }
      });
  });

  // Remove the elements that are part of arr2 from arr1
  arr2.forEach((val) => {
      arr1 = arr1.filter(ele => ele !== val);
  });

  // Sort the remaining elements in arr1
  remainingElems = arr1.sort((a, b) => a - b);

  // Concatenate the remaining sorted elements to the result array
  resArr = resArr.concat(remainingElems);

  return resArr;
};

// Example usage
const arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19];
const arr2 = [2, 1, 4, 3, 9, 6];
console.log(relativeSortArray(arr1, arr2)); // Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

const arr1_2 = [28, 6, 22, 8, 44, 17];
const arr2_2 = [22, 28, 8, 6];
console.log(relativeSortArray(arr1_2, arr2_2)); // Output: [22, 28, 8, 6, 17, 44]


// Better Appraoch
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
  // initialize result array and cache object
  const result = [];
  const cache = {};
  // cache frequency of elements in array 1
  for (let i = 0; i < arr1.length; i++) {
    cache[arr1[i]] ? cache[arr1[i]]++ : cache[arr1[i]] = 1;
  }
  // iterate over arr2, checking if elements are in cache
  for (let i = 0; i < arr2.length; i++) {
    let currVal = arr2[i];
    if (cache[currVal]) {
      while (cache[currVal] > 0) {
      result.push(currVal);
      cache[currVal]--;
      }
    }
  }
  // iterate over keys in cache object and add to result arr
  for (let key in cache) {
    while (cache[key] > 0) {
      result.push(key);
      cache[key]--;
    }
  }
  // return result
  return result;
};

// another one
