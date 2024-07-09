import textwrap

def wrap(string, max_width):
    # counter = 0
    # output = ''
    # for char in string:
    #     if counter < max_width - 1:
    #         output += char
    #         counter += 1
    #     else:

    #         output += char + "\n"
    #         counter = 0
    # return output
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)