# Сушинський Ігор
# Лабораторна робота №1
# Знайомство із середовищем. Налагодження програми. Структура програми. Базові обчислення. Модуль math
# Варіант 18

from math import sin, cos, log10


def calculate_expression(x):
    result = 2 * (x ** 2 - 3) - (sin(x ** 2) / 1 + cos(x)) + (cos(abs(x)) ** 2) - log10(x + 2) - 1 + sin(x) ** 2
    return result


y = float(input("Введіть, будь ласка, значення для x = "))

print(f"y = {calculate_expression(y)}")
