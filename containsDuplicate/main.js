class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seenSet = new Set(); // Set to store unique numbers we encounter in the array
        for(const num of nums){ // Iterate through each number in the array
            if (seenSet.has(num)){  // If the number already exists in the Set, it's a duplicate
                return true;    // Found a duplicate, return true
            }
            seenSet.add(num); // If didn't find a duplicate it adds to set
        }
        return false;   // when the Itteration is over there are no duplicate it returns false
    }
}
const solution = new Solution();    // create an object from the Solution class
console.log(solution.hasDuplicate([1, 2, 3, 3]));