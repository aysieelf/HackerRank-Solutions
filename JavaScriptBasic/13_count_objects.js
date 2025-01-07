/*
Task:
    Complete the function in the editor.
    It has one parameter: an array, a, of objects.
    Each object in the array has two integer properties denoted by x and y.
    The function must return a count of all such objects o in array a that satisfy o.x == o.y.

Input Format:
    The first line contains an integer denoting n.
    Each of the n subsequent lines contains two space-separated integers describing the values of x and y.

Output Format:
    Return a count of the total number of objects o such that o.x == o.y.
    Locked stub code in the editor prints the returned value to STDOUT.
 */

function getCount(objects) {
    let count = 0;
    for (const o of objects) {
        if (o.x === o.y) {
            count++;
        }
    }
    return count;
}

function getCount(objects) {
    return objects.filter(o => o.x === o.y).length;
}