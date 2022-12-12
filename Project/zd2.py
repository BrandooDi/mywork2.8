#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cylinder(radius, height):
    def circle():
        print(
            "Площадь полной поверхности цилиндра: ",
            2 * 3.14 * radius * height + 2 * 3.14 * radius ** 2,
        )

    message = input(
        "Какую площать вы хотите получить: площадь бокой"
        " поверхности или полную площадь цилиндра?\n"
        "Площадь бокой поверхности команда - неполная\n"
        "Площадь полной поверхности цилинда команда - полная\n"
        ">>>"
    )
    if message.lower() == "неполная":
        print("Площадь боковой повехности: ", 2 * 3.14 * radius * height)
    elif message.lower() == "полная":
        circle()
    else:
        print("Неизвестная команда")


if __name__ == "__main__":
    radius = int(input("Введите радиус цилиндра"))
    height = int(input("Введите высоту цилиндра"))
    cylinder(radius, height)
