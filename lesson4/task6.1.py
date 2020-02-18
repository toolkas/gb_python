# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from sys import argv
from itertools import count

if len(argv) == 1:
    print("Передайте программе число, с которого начать генерацию")
    exit(0)

start = int(argv[1])
for x in count(start):
    print(x)
