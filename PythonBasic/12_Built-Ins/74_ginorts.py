"""
Task:
    You are given a string S. S contains alphanumeric characters only.
    Your task is to sort the string S in the following manner:
        - all sorted lowercase letters are ahead of uppercase letters,
        - all sorted uppercase letters are ahead of digits,
        - all sorted odd digits are ahead of sorted even digits.
"""
s = input()

lowercase = []
uppercase = []
odd_digits = []
even_digits = []
for char in s:
    if char.isalpha():
        if char.islower():
            lowercase.append(char)
        else:
            uppercase.append(char)
    else:
        if int(char) % 2 == 1:
            odd_digits.append(char)
        else:
            even_digits.append(char)

lowercase = sorted(lowercase)
uppercase = sorted(uppercase)
odd_digits = sorted(odd_digits)
even_digits = sorted(even_digits)

print(f"{''.join(lowercase)}{''.join(uppercase)}{''.join(odd_digits)}{''.join(even_digits)}")
