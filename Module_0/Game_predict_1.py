'''Оптимизированная игра, с использованием бинарного поиска, чтобы узнать как быстро игра угадывает число.
   Используем цикл, благодаря которому делим массив пополам и далее определяем в каком промежутке находится искомое число'''

import numpy as np

number = np.random.randint(1,101)  # загадали число


def game_predict(number):

    predict = 50
    count = 0
    min_limit = 1
    max_limit = 101

    while predict != number:
        count += 1  # плюсуем попытку
        predict = min_limit + (max_limit - min_limit) // 2  # определяем экватор массива

        if predict > number:
            max_limit = predict
        else:
            min_limit = predict

    print(f"Ваш алгоритм угадывает число в среднем за {count} попыток")

    return (count)


game_predict(number)
