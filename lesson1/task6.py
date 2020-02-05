# 6. Спортсмен занимается ежедневными пробежками. В первый день его
# результат составил a километров. Каждый день спортсмен увеличивал
# результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно
# натуральное число — номер дня.
#
# Например: a = 2, b = 3.
#
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = float(input("Результат в первый день? "))
b = float(input("Целевой результат? "))

current = a
day = 1
while True:
    print(f"{day}-й день: {current:.2f}")

    if current >= b:
        break

    day += 1
    current *= 1.1

print()
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.")
