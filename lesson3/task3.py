# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(x, y, z):
    values = sorted([x, y, z])
    return values[1] + values[2]


print(my_func(3, 1, 3))