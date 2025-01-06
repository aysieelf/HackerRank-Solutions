/*
Task:
    Complete the isPositive function below. It has one integer parameter, a.
    If the value of a is positive, it must return the string YES.
    Otherwise, it must throw an Error according to the following rules:
        If a is 0, throw an Error with message = Zero Error.
        If a is negative, throw an Error with message = Negative Error.

Input Format:
    Locked stub code in the editor reads the following input from stdin
    and passes each value of a to the function as an argument:
        The first line is an integer, n, denoting the number of times the function will be called with some a.
        Each line i of the n subsequent lines contains an integer denoting some a.

Output Format:
    If the value of a is positive, the function must return the string YES.
    Otherwise, it must throw an Error according to the following rules.
 */
function isPositive(a) {
    if (a > 0) {
        return "YES";
    }
    else if (a === 0) {
        throw new Error("Zero Error");
    }
    else {
        throw new Error("Negative Error");
    }
}