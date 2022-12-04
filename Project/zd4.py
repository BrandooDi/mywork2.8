#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    """
    Получение и возвращение строки
    """
    s = input("Введите строку: ")
    return s


def test_input(s):
    """
    Проверка на возможность преобразования в число
    """
    if type(s) == int or s.isnumeric():
        return True
    else:
        return False


def str_to_int(s):
    """
    Преобразование в целочисленный тип
    """
    n = int(s)
    return n


def print_int(s):
    """
    Вывод на экран
    """
    print(s)


if __name__ == "__main__":
    a = get_input()
    if test_input(a) is True:
        print_int(str_to_int(a))
    else:
        print("Введенную строку невозможно преобразовать в число")
