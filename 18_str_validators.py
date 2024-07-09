
def any_isalnum(string: str) -> bool:
    return any(i.isalnum() for i in string)


def any_isalpha(string: str) -> bool:
    return any(i.isalpha() for i in string)


def any_isdigit(string: str) -> bool:
    return any(i.isdigit() for i in string)


def any_islower(string: str) -> bool:
    return any(i.islower() for i in string)


def any_isupper(string: str) -> bool:
    return any(i.isupper() for i in string)


if __name__ == '__main__':
    s = input()

    print(any_isalnum(s))
    print(any_isalpha(s))
    print(any_isdigit(s))
    print(any_islower(s))
    print(any_isupper(s))