# Сушинський Ігор
# Лабораторна робота №1
# Знайомство із середовищем. Налагодження програми. Структура програми. Базові обчислення. Модуль math
# Варіант 18

from math import sin, cos, log10


def math_expression(x):
    return 2 * (x ** 2 - 3) - (sin(x ** 2) / 1 + cos(x)) + (cos(abs(x)) ** 2) - log10(x + 2) - 1 + sin(x) ** 2


y = float(input("Введіть, будь ласка, значення для x = "))

print(f"1) y = {math_expression(y)}")

a = int(input("Введіть початок проміжку: a = "))
b = int(input("Введіть кінець проміжку: b = "))
h = int(input("Введіть крок проміжку: h = "))

lst = []
for x in range(a, b + 1, h):
    y = 2 * (x ** 2 - 3) - (sin(x ** 2) / 1 + cos(x)) + (cos(abs(x)) ** 2) - log10(abs(x) + 2) - 1 + sin(x) ** 2
    lst.append(round(y, 3))

print(f"2) y = {lst}")
