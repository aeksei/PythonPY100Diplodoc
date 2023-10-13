def is_palindrome_number(num: int) -> bool:
    if num < 0:
        raise ValueError("Число должно быть неотрицательным")

    return True if str(num) == str(num)[::-1] else False


if __name__ == "__main__":
    print(is_palindrome_number(1234))
    print(is_palindrome_number(1234321))
