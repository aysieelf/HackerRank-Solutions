/*
Task:
    First, print each vowel in s on a new line. The
    English vowels are a, e, i, o, and u, and each vowel must be printed in the same order as it appeared in s.
    Second, print each consonant (i.e., non-vowel) in  on a new line in the same order as it appeared in s.

Input Format:
    There is one line of input with the string s.

Output Format:
    First, print each vowel in  on a new line (in the same order as they appeared in ).
    Second, print each consonant (i.e., non-vowel) in  on a new line (in the same order as they appeared in ).
 */

function vowelsAndConsonants(s) {
    const vowels = new Set("aeiou");

    for (const char of s) {
        if (vowels.has(char)) {
            console.log(char);
        }
    }

    for (const char of s) {
        if (!vowels.has(char)) {
            console.log(char);
        }
    }
}