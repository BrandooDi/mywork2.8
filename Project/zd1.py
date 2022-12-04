#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    """
    Проверка числа на знак
    """
    number = int(input("Введите число: "))
    if number > 0:
        positive()
    else:
        negative()


def positive():
    """
    Вывод, что число положительное
    """
    print("Положительное")


def negative():
    """
    Вывод, что число отрицательное
    """
    print("Отрицательное")


if __name__ == "__main__":
    test()
