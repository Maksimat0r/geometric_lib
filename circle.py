import math

"""
    Вычисляет площадь круга по заданному радиусу.

    Параметры:
    r: Радиус круга.

    Возвращает: Площадь круга.

    Пример вызова:
    area(5) -> 78.54
"""
def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

