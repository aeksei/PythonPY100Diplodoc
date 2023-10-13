def task(n: int, m: int) -> list:
    return [num ** 2 for num in range(n, m+1) if num % 2 == 1]


if __name__ == "__main__":
    number_n = 5
    number_m = 37
    print(task(5, 37))
