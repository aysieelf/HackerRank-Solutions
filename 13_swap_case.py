def swap_case(s):
    output = ''
    for i in s:
        if i.isalpha():
            output = output + i.swapcase()
        else:
            output = output + i
    return output

