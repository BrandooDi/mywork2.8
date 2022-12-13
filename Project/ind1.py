#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_plat():
    """
    Запросить данные о платежах.
    """
    raspol = input("Расчётный счёт платильщика: ")
    raspl = input("Расчётный счет получателя: ")
    sum = input("Перечисляемая сумма в руб: ")

    # Создать словарь.
    return {
        "raspol": raspol,
        "raspl": raspl,
        "sum": sum,
    }


def display_plats(staff):
    """
    Отобразить список платежей.
    """
    # Проверить, что список платежей не пуст.
    if staff:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 35, "-" * 45)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^35} | {:^45} |".format(
                "No",
                "Расчётный счёт платильщика",
                "Расчётный счет получателя",
                "Перечисляемая сумма в руб",
            )
        )
        print(line)

        # Вывести данные о всех платежах.
        for idx, plat in enumerate(staff, 1):
            print(
                "| {:>4} | {:<30} | {:<35} | {:>45} |".format(
                    idx,
                    plat.get("raspol", ""),
                    plat.get("raspl", ""),
                    plat.get("sum", 0),
                )
            )

        print(line)

    else:
        print("Список платежей пуст")


def select_plats(staff, sum):
    """
    Выбрать сумму с данным типом.
    """
    # Сформировать список  платежей.
    result = [plat for plat in staff if sum == plat.get("sum", 0)]

    # Возвратить список выбранных платежей.
    return result


def main():
    """
    Главная функция программы.
    """
    # Список платежей.
    plats = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == "exit":
            break

        elif command == "add":
            # Запросить данные о платеже.
            plat = get_plat()

            # Добавить словарь в список.
            plats.append(plat)
            # Отсортировать список в случае необходимости.
            if len(plats) > 1:
                plats.sort(key=lambda item: item.get("raspol", ""))

        elif command == "list":
            # Отобразить все платежи.
            display_plats(plats)

        elif command.startswith("select "):
            # Разбить команду на части для выделения пункта назначения.
            part = command.split(" ", maxsplit=1)
            com = part[1]

            # Выбрать платежи заданного типа
            selected = select_plats(plats, com)
            # Отобразить выбранные платежи
            display_plats(selected)

        elif command == "help":
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить самолет;")
            print("list - вывести список самолетов;")
            print("select <тип> - запросить самолеты заданного типа;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
