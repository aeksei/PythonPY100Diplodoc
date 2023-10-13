def task(num: int) -> bool:
    list_digits = [int(digit) for digit in str(num)]
    return False if len(set(list_digits)) == len(list_digits) else True


if __name__ == "__main__":
    print(task(123))
    print(task(1111111))
