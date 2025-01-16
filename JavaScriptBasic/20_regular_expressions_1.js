/*
Task:
    Complete the function in the editor below by returning a RegExp object, re,
    that matches any string s that begins and ends with the same vowel.
    Recall that the English vowels are a, e, i, o, and u.

Constraints:
    The length of string s is >= 3.
    String  consists of lowercase letters only (i.e., [a-z]).

Output Format:
    The function must return a RegExp object that matches any string beginning with and ending in the same vowel.
*/

function regexVar() {
    return new RegExp('^[aioueAIOUE].*\1$');
}
