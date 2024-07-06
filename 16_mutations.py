def mutate_string(string: str, position: int, character: str):
    """
    Replaces the letter in the position of a string to another letter.
    
    Inputs:
    String: str type; input string we want to change.
    Position: int type;  position of letter that is going to be changed.
    Character: str type; the character with which we replace the old letter.
    """
    
    new_string = string[:position] + character + string[position+1:]
    return new_string
