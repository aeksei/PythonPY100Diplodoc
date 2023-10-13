def get_year_count(start_money, inflation):
    current_money = start_money
    count_years = 0

    while True:
        current_money = current_money * (1 - inflation)
        count_years += 1
        if current_money <= (start_money / 2):
            break

    return count_years


if __name__ == "__main__":
    print(get_year_count(10000, 0.2))
