# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def divide_number(x, y):
    return x / y


first = float(input("Введите числитель: ").strip())
second = float(input("Введите знаменатель: ").strip())

try:
    result = first / second
    print(f"{first} / {second} = {result}")
except ZeroDivisionError:
    print("Введены некорректные данные: нельзя делить на ноль!")