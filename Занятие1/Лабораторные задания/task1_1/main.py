DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input("Год рождения: "))
current_year = int(input("Текущий год: "))

days = (current_year - start_year) * DAYS_OF_YEAR
print(days)
