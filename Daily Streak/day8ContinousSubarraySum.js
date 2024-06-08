      // // Note:-  Concept is not clear enough do it again later.........
// 523. Continuous Subarray Sum
// Medium
// Topics
// Companies
// Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

// A good subarray is a subarray where:

// its length is at least two, and
// the sum of the elements of the subarray is a multiple of k.
// Note that:

// A subarray is a contiguous part of the array.
// An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

// Example 1:

// Input: nums = [23,2,4,6,7], k = 6
// Output: true
// Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
// Example 2:

// Input: nums = [23,2,6,4,7], k = 6
// Output: true
// Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
// 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
// Example 3:

// Input: nums = [23,2,6,4,7], k = 13
// Output: false
 

// Constraints:

// 1 <= nums.length <= 105
// 0 <= nums[i] <= 109
// 0 <= sum(nums[i]) <= 231 - 1
// 1 <= k <= 231 - 1 

function hasGoodSubarray(nums, k) {
    // Edge case for k == 0
    if (k === 0) {
      for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] === 0 && nums[i + 1] === 0) {
          return true;
        }
      }
      return false;
    }
  
    // Dictionary to store the first occurrence of each modulo value
    const modMap = new Map();
    modMap.set(0, -1);  // Initialize with 0 to handle cases where the subarray starts from index 0
    let cumulativeSum = 0;
  
    for (let i = 0; i < nums.length; i++) {
      cumulativeSum += nums[i];
      let modValue = ((cumulativeSum % k) + k) % k; // Handle negative mod value
  
      if (modMap.has(modValue)) {
        if (i - modMap.get(modValue) > 1) {
          return true;
        }
      } else {
        modMap.set(modValue, i);
      }
    }
  
    return false;
  }
  
  // Example usage:
  console.log(hasGoodSubarray([23, 2, 4, 6, 7], 6));  // Output: True
  console.log(hasGoodSubarray([23, 2, 6, 4, 7], 6));  // Output: True
  console.log(hasGoodSubarray([23, 2, 6, 4, 7], 13)); // Output: False
  


// not a good approach 
function hasGoodSubarray(nums, k) {
    // Edge case for k == 0
    if (k === 0) {
      for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] === 0 && nums[i + 1] === 0) {
          return true;
        }
      }
      return false;
    }
  
    const modValues = [];
    const indices = [];
    let cumulativeSum = 0;
  
    modValues.push(0);
    indices.push(-1); // Initialize with 0 to handle cases where the subarray starts from index 0
  
    for (let i = 0; i < nums.length; i++) {
      cumulativeSum += nums[i];
      let modValue = ((cumulativeSum % k) + k) % k; // Handle negative mod value
  
      for (let j = 0; j < modValues.length; j++) {
        if (modValues[j] === modValue && i - indices[j] > 1) {
          return true;
        }
      }
  
      modValues.push(modValue);
      indices.push(i);
    }
  
    return false;
  }
  
  // Example usage:
  console.log(hasGoodSubarray([23, 2, 4, 6, 7], 6));  // Output: True
  console.log(hasGoodSubarray([23, 2, 6, 4, 7], 6));  // Output: True
  console.log(hasGoodSubarray([23, 2, 6, 4, 7], 13)); // Output: False