// 

var minKBitFlips = function(nums, k) {
    let n = nums.length;
    let flip = 0; // Tracks the number of flips made
    let isFlipped = new Array(n).fill(0); // Tracks if the current index has been flipped
    
    let flips = 0; // Total number of flips performed
    
    for (let i = 0; i < n; i++) {
        // If we move out of a window that was flipped, we need to unmark the flip
        if (i >= k) {
            flip ^= isFlipped[i - k];
        }
        
        // If the current bit needs to be flipped (either it is 0 and we need 1, or it is 1 and we need 0)
        if (nums[i] == flip) {
            // If we can't flip because there aren't enough elements left
            if (i + k > n) return -1;
            
            // Flip the current bit
            flips++;
            flip ^= 1; // Mark the current flip
            isFlipped[i] = 1; // Record the flip at this position
        }
    }
    
    return flips;
};

// Example 1:
console.log(minKBitFlips([0, 1, 0], 1)); // Output: 2

// Example 2:
console.log(minKBitFlips([1, 1, 0], 2)); // Output: -1

// Example 3:
console.log(minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3)); // Output: 3
