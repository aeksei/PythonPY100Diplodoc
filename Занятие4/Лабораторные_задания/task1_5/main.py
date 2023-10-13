if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_even = [num for num in list_ if num % 2 == 0]
    list_odd = [num for num in list_ if num % 2 == 1]

    len_even = len(list_even)
    len_odd = len(list_odd)

    if len_odd > len_even:
        print("Нечетные")
    elif len_odd < len_even:
        print("Четные")
    else:
        print("Одинаково")
