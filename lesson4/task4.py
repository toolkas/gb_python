# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.


my_list = [1, 2, 1, 4, 6, 3, 3, 6, 3, 8, 9, 11, 1]

my_list_2 = [x for x in my_list if my_list.count(x) == 1]
print(my_list_2)
