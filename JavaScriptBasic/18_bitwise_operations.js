/*
Task:
    We define S to be a sequence of distinct sequential integers from 1 to n.
    We want to know the maximum bitwise AND value of any two integers, a and b (where a < b),
    in sequence S that is also less than a given integer, k.

Input Format:
    The first line contains an integer, q, denoting the number of function calls.
    Each of the q subsequent lines defines a dataset for a function call
    in the form of two space-separated integers describing the respective values of n and k.

Output Format:

    Return the maximum possible value of a & b < k for any a < b in sequence k.
 */

function getMaxLessThanK(n, k) {
    let maxValue = 0;

    for (let i = 1; i <= n; i++) {
        for (let j = i + 1; j <= n; j++) {
            let curr = i & j;
            if (curr > maxValue && curr < k) {
                maxValue = curr;
            }
        }
    }
    return maxValue
}