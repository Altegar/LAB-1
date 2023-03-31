# Сушинський Ігор
# Лабораторна робота №1
# Знайомство із середовищем. Налагодження програми. Структура програми. Базові обчислення. Модуль math
# Варіант 18

from math import sqrt, sin, cos, tan, log

a = int(input("Введіть початок проміжку: a = "))
b = int(input("Введіть кінець проміжку: b = "))
h = int(input("Введіть крок проміжку: h = "))

lst1 = []
for x in range(a, b + 1, h):
    y = 2 * (x ** 2 - 3) - (sin(x ** 2) / 1 + cos(x)) + (cos(abs(x)) ** 2) - log(abs(x) + 2) - 1 + sin(x) ** 2
    lst1.append(round(y, 3))

print(f"1) y = {lst1}")

print("======================")

a = int(input("Введіть початок проміжку: a = "))
b = int(input("Введіть кінець проміжку: b = "))
h = int(input("Введіть крок проміжку: h = "))

lst2 = []
for x in range(a, b + 1, h):
    y = 7 - 4 * x - x ** 2 + x ** 3 + log(3 + 2 * abs(x)) + 1 / tan((4 + abs(x)) / 8) + sqrt(1 - sin(x) ** 2)
    lst2.append(round(y, 3))

print(f"2) y = {lst2}")
