import datetime
import sys
import logging


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def num_filtr(fl):
    numbers = range(0, 101)
    if fl == "True":
        msg = "Парні елементи -> "
    elif fl == "False":
        msg = "Непарні елементи -> "

    for num in numbers:
        if (fl == "True") & (num % 2 == 0):
            msg += str(num) + ", "
        elif (fl == "False") & (num % 2 != 0):
            msg += str(num) + ", "
    return msg


def array():
    x = [1, 2, 3, 4, 5, 6, 7]
    print("Масив: ", x)
    print("Введіть номер елемента масиву, який хочете вивести: ")
    index = int(input())
    try:
        print(f"X[{index}] = {x[index]}")
    except IndexError:
        logging.error("Такого елементу в масиві немає")
    else:
        logging.info("Ви ввели коректні дані")