function readLine() {
    return inputString[currentLine++];
}
/*
 * Create the function factorial here
 */
function factorial(n) {
    let result = n;
    for (let i = n-1; i > 0; i--) {
        result = result * i;
    }
    return result
}