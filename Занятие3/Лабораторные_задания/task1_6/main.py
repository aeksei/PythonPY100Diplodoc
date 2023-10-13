def alive(salary, spend, months=10, increase=0.03):
    need_money = 0
    for _ in range(months):
        need_money += spend - salary
        spend *= 1 + increase

    return need_money


if __name__ == "__main__":
    print(alive(5000, 6000))
