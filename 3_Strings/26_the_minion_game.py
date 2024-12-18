"""
Task:
    Kevin and Stuart want to play the 'The Minion Game'.

    Game Rules:
        Both players are given the same string, S.
        Both players have to make substrings using the letters of the string S.
        Stuart has to make words starting with consonants.
        Kevin has to make words starting with vowels.
        The game ends when both players have made all possible substrings.

    Scoring:
        A player gets +1 point for each occurrence of the substring in the string S.

    For Example:
        String  = BANANA
        Kevin's vowel beginning word = ANA
        Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

    Your task is to determine the winner of the game and their score.


    minion_game has the following parameters:
        string string: the string to analyze
    Prints:
        string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

Input Format
        A single line of input containing the string .
        Note: The string  will contain only uppercase letters.

What I learned today:
    String vs List - 'AOEIU' in string is faster than ['A', 'O', 'E', 'I', 'U']
    Algorithm optimization from O(n²) → O(n) → O(n/2) by:
        Eliminating substring operations
        Using mathematical formula for counting
        "Mirror" string processing from both ends
"""
def minion_game(string):
    kevin = stuart = 0
    vowels = 'AOEIU'
    len_string = len(string)
    middle = (len_string + 1) // 2

    if string[0] in vowels:
        kevin += len_string
    else:
        stuart += len_string

    for i in range(1, middle):
        if string[i] in vowels:
            kevin += (len_string - i)
        else:
            stuart += (len_string - i)

        if string[-i] in vowels:
            kevin += i
        else:
            stuart += i

    if len_string % 2 == 0:
        if string[len_string // 2] in vowels:
            kevin += len_string / 2
        else:
            stuart += len_string / 2


    if kevin > stuart:
        print("Kevin", int(kevin))
    elif kevin < stuart:
        print("Stuart", int(stuart))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

