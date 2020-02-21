# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers = [1, 3, 2, 56, 7, -1]
# записываем числа в файл
with open("task5.file.txt", 'w', encoding='utf-8') as f:
    print(*numbers, sep=" ", file=f)

# подсчитываем сумму чисел в файле
with open("task5.file.txt", encoding='utf-8') as f:
    numbers_sum = sum(map(int, f.readline().strip().split()))
    print(f"Сумма чисел равна {numbers_sum}")

