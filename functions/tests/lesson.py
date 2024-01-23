

def add_one(num: int) -> int:
    return num + 1


def division(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y


def is_palindrom(string: str) -> bool:
    if string[::-1] == string:
        return True
    return False

