# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый элемент
# рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
# новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = []

while True:
    line = input("Введите целое число или 'стоп', чтобы закончить: ").strip()
    if line == 'stop':
        break

    number = int(line)

    index = 0
    while index < len(rating):
        current = rating[index]
        if current < number:
            break
        index += 1

    print(f"rating.insert({index}, {number})")
    rating.insert(index, number)

    print(f"Результат: {' '.join(map(str, rating))}")
