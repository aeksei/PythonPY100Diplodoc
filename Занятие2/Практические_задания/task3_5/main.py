mount = int(input("Введите номер месяца: "))

if mount in range(3, 6):
    print("Весна")
elif mount in [6, 7, 8]:
    print("Лето")
elif mount in (9, 10, 11):
    print("Осень")
elif mount in {12, 1, 2}:
    print("Зима")
else:
    print("Такого месяца не существует :(")
