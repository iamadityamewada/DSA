// 

function longestSubarray(nums, limit) {
    let minDeque = [];
    let maxDeque = [];
    let left = 0;
    let maxLen = 0;

    for (let right = 0; right < nums.length; right++) {
        // Update minDeque
        while (minDeque.length && nums[minDeque[minDeque.length - 1]] > nums[right]) {
            minDeque.pop();
        }
        minDeque.push(right);

        // Update maxDeque
        while (maxDeque.length && nums[maxDeque[maxDeque.length - 1]] < nums[right]) {
            maxDeque.pop();
        }
        maxDeque.push(right);

        // Shrink window from the left if the condition is violated
        while (nums[maxDeque[0]] - nums[minDeque[0]] > limit) {
            left++;
            // Remove elements that are out of the window
            if (minDeque[0] < left) {
                minDeque.shift();
            }
            if (maxDeque[0] < left) {
                maxDeque.shift();
            }
        }

        // Calculate the max length of the subarray
        maxLen = Math.max(maxLen, right - left + 1);
    }

    return maxLen;
}
