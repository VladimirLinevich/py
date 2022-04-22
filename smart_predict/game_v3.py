"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def smart_predict(number: int = 1) -> int:
    """Функция угадывает число, учитывая, что на каждой итерации нам известно:
    больше либо меньше загаданное число, чем наше преполагаемое
    В каждой итерации уменьшаем диапазон гадания, в зависимости от того,
    меньше загаданное число, либо больше.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0  # счетчик попыток
    upper_bound = 100  # верхняя граница диапазона "гадания"
    lower_bound = 0  # нижняя граница диапазона "гадания"
    while True:
        count += 1
        predict_number = np.random.randint(lower_bound, upper_bound+1)
        if number == predict_number:
            break
        elif number < predict_number:
            upper_bound = predict_number-1
        elif number > predict_number:
            lower_bound = predict_number+1
    return count


def score_game(predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        predict_func ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали числа

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(smart_predict)
