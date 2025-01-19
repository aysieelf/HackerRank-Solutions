/*
Task:
    Complete the function in the editor below by returning a RegExp object, re,
    that matches any string s satisfying both of the following conditions:
        - String s starts with the prefix Mr., Mrs., Ms., Dr., or Er.
        - The remainder of strings s (i.e., the rest of the string after the prefix)
        consists of one or more upper and/or lowercase English alphabetic letters (i.e., [a-zA-Z]).

 */

function regexVar() {
    return new RegExp('^(Mr|Mrs|Ms|Dr|Er)\\.[a-zA-Z]+$')
}