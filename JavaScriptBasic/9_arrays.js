/*
Function Description:
    Complete the getSecondLargest function in the editor below.
    getSecondLargest has the following parameters:

        int nums[n]: an array of integers
    Returns:
        int: the second largest number in nums

Input Format:
    The first line contains an integer, n, the size of the nums array.
    The second line contains n space-separated numbers that describe the elements in .
 */

function getSecondLargest(nums) {
    const unique = [... new Set(nums)];
    const sorted = unique.sort((a, b) => a - b);
    return sorted[sorted.length - 2];
}