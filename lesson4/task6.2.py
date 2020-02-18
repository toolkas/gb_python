# 6. Реализовать два небольших скрипта:
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.


from sys import argv
from itertools import cycle

if len(argv) == 1:
    print("Передайте программе список чисел, которые надо повторять")
    exit(0)

for x in cycle(argv[1:]):
    print(x)