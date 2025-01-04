/*
Task:
    Complete the getGrade(score) function in the editor.
    It has one parameter: an integer, score, denoting the number of points Julia earned on an exam.
    It must return the letter corresponding to her grade according to the following rules:
        If 25 < score <= 30, then grade = A.
        If 20 < score <= 25, then grade = B.
        If 15 < score <= 20, then grade = C.
        If 10 < score <= 15, then grade = D.
        If 5 < score <= 10, then grade = C.
        If 0 <= score <= 5, then grade = F.

Input Format:
    Stub code in the editor reads a single integer denoting score from stdin and passes it to the function.

Output Format:
    The function must return the value of grade (i.e., the letter grade) that Julia earned on the exam.
 */

function getGrade(score) {
    if ((25 < score) && (score <= 30)) {
        return "A";
    }
    else if ((20 < score) && (score <= 25)) {
        return "B";
    }
    else if ((15 < score) && (score <= 20)) {
        return "C";
    }
    else if ((10 < score) && (score <= 15)) {
        return "D";
    }
    else if ((5 < score) && (score <= 10)) {
        return "E";
    }
    else {
        return "F";
    }
}
