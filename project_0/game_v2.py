"""Игра угадай число
компьютер сам загадывает и сам отгадывает число, количество
попыток не должно превышать 20.  
"""

import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число из диапазона, с корректировкой
    диапазона после каждой итерации.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    range_min = 1
    range_max = 101
    
    while True:
        count += 1
        predict_number = np.random.randint(range_min, range_max)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
        elif number > predict_number:
            range_min = predict_number + 1
        else:
            range_max = predict_number
    return(count)


def middle_predict(number:int=1) -> int:
    """Методично в качестве угадываемого числа берем середину
    диапазона (целую часть), с каждой попыткой уменьшая диапазон 
    в геометрической прогрессии. 
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    range_min = 1
    range_max = 101
    
    while True:
        count += 1
        predict_number = int((range_min+range_max) * 0.5)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
        elif number > predict_number:
            range_min = predict_number + 1
        else:
            range_max = predict_number
    return(count)


def score_game(func_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        func_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(func_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Алгоритм {func_predict.__name__} угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)
score_game(middle_predict)