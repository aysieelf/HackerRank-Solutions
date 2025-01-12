/*
Task:
    Complete the function in the editor.
    It has one parameter: an array, nums.
    It must iterate through the array performing one of the following actions on each element:
        If the element is even, multiply the element by 2.
        If the element is odd, multiply the element by 3.
    The function must then return the modified array.

Input Format:
    The first line contains an integer, n, denoting the size of nums.
    The second line contains n space-separated integers describing the respective elements of nums.

Output Format:
    Return the modified array where every even element is doubled and every odd element is tripled.
 */

function modifyArray(nums) {
    nums = nums.map((n) => n % 2 === 0 ? n * 2 : n);
    nums = nums.map((n) => n % 2 === 1 ? n * 3 : n);
    return nums;
}