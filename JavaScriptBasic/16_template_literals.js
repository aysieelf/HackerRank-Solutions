/*
Task:
    The code in the editor has a tagged template literal that passes
    the area and perimeter of a rectangle to a tag function named sides.
    Recall that the first argument of a tag function is an array of string literals from the template,
    and the subsequent values are the template's respective expression values.

    Complete the function in the editor so that it does the following:
        Finds the initial values of s1 and s2 by plugging the area and perimeter values into the formula:
            S = P +/- sqrt(P**2 - 16*A) / 4
        Creates an array consisting of s1 and s2 and sorts it in ascending order.
        Returns the sorted array.

Input Format:
    The first line contains an integer denoting s1.
    The second line contains an integer denoting s2.

Output Format:

Return an array consisting of s1 and s2, sorted in ascending order.
 */
function sides(literals, ...expressions) {
    const [area, perimeter] = expressions;
    const s1 = (perimeter + Math.sqrt(perimeter**2 - 16*area)) / 4;
    const s2 = (perimeter - Math.sqrt(perimeter**2 - 16*area)) / 4;

    return [s1, s2].sort((a, b) => a - b);

}