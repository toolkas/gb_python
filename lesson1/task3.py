# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число: "))

nn = 10 * n + n
nnn = 100 * n + 10 * n + n

s = nnn + nn + n
print(f"{nnn} + {nn} + {n} = {s}")