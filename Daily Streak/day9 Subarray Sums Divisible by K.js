// note   concept not clear redo this
// Subarray Sums Divisible by K


// 974. Subarray Sums Divisible by K
// Solved
// Medium
// Topics
// Companies
// Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

// A subarray is a contiguous part of an array.

 

// Example 1:

// Input: nums = [4,5,0,-2,-3,1], k = 5
// Output: 7
// Explanation: There are 7 subarrays with a sum divisible by k = 5:
// [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
// Example 2:

// Input: nums = [5], k = 9
// Output: 0
 

// Constraints:

// 1 <= nums.length <= 3 * 104
// -104 <= nums[i] <= 104
// 2 <= k <= 104




/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraysDivByK = function(nums, k) {
    let remainderCount = {0: 1};
   let prefixSum = 0;
   let result = 0;

   for (let num of nums) {
       prefixSum += num;
       let remainder = prefixSum % k;
       if (remainder < 0) {
           remainder += k;
       }
       
       if (remainder in remainderCount) {
           result += remainderCount[remainder];
           remainderCount[remainder] += 1;
       } else {
           remainderCount[remainder] = 1;
       }
   }

   return result;
}




// optimal approach
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraysDivByK = function(nums, k) {
    let res = 0
    let map = {}
    for (let i=0; i<k; i++) {
        map[i] = 0
    }
    map[0] = 1

    let prefixRem = 0
    for (let num of nums) {
        prefixRem = (prefixRem + num%k + k) % k
        res += map[prefixRem]
        map[prefixRem]++
    }

    return res
};