# 4. Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические
# операции.

n = int(input("Введите целое положительное число: "))

if n <= 0:
    print("Вы ввели некорректное число!")
else:
    max_digit = 0
    current = n
    while current != 0:
        digit = current % 10
        if digit > max_digit:
            max_digit = digit
        current = current // 10

    print(f"Максимальная цифра числа {n} равна {max_digit}")