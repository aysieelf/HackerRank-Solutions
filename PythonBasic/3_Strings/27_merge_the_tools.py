"""
Task:
    Given a string s of length n and an integer k (where k is a factor of n)
    split string into n/k substrings, each of length k.
    For each substring, create a new string that:
        Contains only unique characters (remove duplicates)
        Maintains original order of first appearance
        Characters should be a subsequence of original substring


    merge_the_tools has the following parameters:
        string s: the string to analyze
        int k: the size of substrings to analyze
    prints:
        Print each subsequence on a new line
        No return value is expected
"""
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i: i+k]
        curr_str = ''
        for el in sub:
            if el not in curr_str:
                curr_str += el
        print(curr_str)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)