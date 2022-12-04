#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    """
    Вычисление полной площади или площади боковой поверхности цилиндра
    """
    way = int(
        input(
            "Какую площадь вы хотите вычислить?\n"
            "Боковой поверхности(1)\n"
            "Полную площадь(2)\n"
            "> "
        )
    )

    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    s = 2 * math.pi * r * h

    if way == 1:
        print(f"Боковая площадь s = {s}")

    elif way == 2:
        s += circle(r) * 2
        print(f"Полная площадь s = {s}")

    else:
        print("Ошибка")


def circle(r):
    """
    Вычисление площади основания
    """
    return math.pi * pow(r, 2)


if __name__ == "__main__":
    cylinder()
