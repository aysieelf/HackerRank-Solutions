/*
Task:
    Complete the getLetter(s) function in the editor. It has one parameter: a string, s,
    consisting of lowercase English alphabetic letters (i.e., a through z).
    It must return A, B, C, or D depending on the following criteria:
        If the first character in string s is in the set {a, e, i, o, u}, then return A.
        If the first character in string s is in the set {b, c, d, f, g}, then return B.
        If the first character in string s is in the set {h, j, k, l, m}, then return C.
        If the first character in string s is in the set {n, p, q, r, s, t, v, w, x, y, z}, then return D.

Function Description:
    Complete the getLetter function in the editor below.
        getLetter has the following parameters:
            string s: a string
        Returns:
            string: a single letter determined as described above

Input Format:
    Stub code in the editor reads a single string denoting s from stdin.
 */
function getLetter(s) {
    let letter;
    switch (s[0]) {
        case "a":
        case "e":
        case "i":
        case "o":
        case "u":
            letter = "A";
            break;
        case "b":
        case "c":
        case "d":
        case "f":
        case "g":
            letter = "B";
            break;
        case "h":
        case "j":
        case "k":
        case "l":
        case "m":
            letter = "C";
            break;
        case "n":
        case "p":
        case "q":
        case "r":
        case "s":
        case "t":
        case "v":
        case "w":
        case "x":
        case "y":
        case "z":
            letter = "D";
            break;
    }
    return letter;
}