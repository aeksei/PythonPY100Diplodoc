def alive(money_capital, salary, spend, increase=0.05):
    month = 0
    while money_capital >= spend:
        month += 1
        money_capital -= spend
        spend *= 1 + increase
        money_capital += salary

    return month


if __name__ == "__main__":
    print(alive(10000, 5000, 6000))
