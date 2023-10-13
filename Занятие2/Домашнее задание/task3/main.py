a = int(input('Введите число '))
b = int(input('Введите число '))
c = int(input('Введите число '))

result1 = a < 45 and b >= 45 and c >= 45
result2 = a >= 45 and b < 45 and c >= 45
result3 = a >= 45 and b >= 45 and c < 45

if result1 or result2 or result3:
    print("Одно из чисел меньше 45")
else:
    print("Все числа больше 45 или все числа меньше 45")
