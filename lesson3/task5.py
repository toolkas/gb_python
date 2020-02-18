# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
# нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале
# нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


result = 0
running = True

while running:
    line = input("Введите числа, разделенные пробелами: ")
    values = line.split()

    if "$" not in values:
        for val in values:
            result += float(val)
        print(f"Сумма чисел: {result}")
    elif values.count("$") == 1:
        for val in values:
            if val == "$":
                print(f"Сумма чисел: {result}")
                running = False
            else:
                result += float(val)
    else:
        stop_word_count = values.count("$")

        accumulator = 0
        for val in values:
            if val == "$":
                stop_word_count -= 1
                if stop_word_count == 0:
                    break
            if val != "$":
                result += float(val)
        result += accumulator
        print(f"Сумма чисел: {result}")
        running = False
