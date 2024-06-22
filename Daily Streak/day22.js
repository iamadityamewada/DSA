// 

function numberOfSubarrays(nums, k) {
    let count = 0;
    let prefixSums = new Map();
    let oddCount = 0;

    prefixSums.set(0, 1); // Initialize with 0 prefix sum count

    for (let num of nums) {
        if (num % 2 !== 0) {
            oddCount++; // Increment the count of odd numbers
        }

        if (prefixSums.has(oddCount - k)) {
            count += prefixSums.get(oddCount - k);
        }

        if (prefixSums.has(oddCount)) {
            prefixSums.set(oddCount, prefixSums.get(oddCount) + 1);
        } else {
            prefixSums.set(oddCount, 1);
        }
    }

    return count;
}

// Example usage
console.log(numberOfSubarrays([1, 1, 2, 1, 1], 3)); // Output: 2
console.log(numberOfSubarrays([2, 4, 6], 1)); // Output: 0
console.log(numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2)); // Output: 16
