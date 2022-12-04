#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiplier():
    """
    Перемножение чисел, пока не будет введен 0
    """
    print("Введите числа:\n")
    res = 1
    while True:
        n = float(input())
        if n == 0:
            break
        else:
            res *= n
    print(f"Произведение: {res}")


if __name__ == "__main__":
    multiplier()
