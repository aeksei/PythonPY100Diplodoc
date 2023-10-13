if __name__ == "__main__":
    number = 123456789

    list_digits = [int(digit) for digit in str(number)]
    print(list_digits)

    print(sum(list_digits))

    print(sum([even_digit for even_digit in list_digits if even_digit % 2 == 0]))

    print(len(list_digits))

    print(min(list_digits))

    print(list_digits[::2])

    print(list_digits[0] - list_digits[-1])
