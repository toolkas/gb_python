# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.

my_list = [1, 3, 5, 2, 5, 9, 2, 10, 1]
my_list_2 = [num for index, num in enumerate(my_list) if index != 0 and num > my_list[index - 1]]

print(my_list_2)
