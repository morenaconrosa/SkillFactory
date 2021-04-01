import numpy as np

number = np.random.randint(1, 101)  # загадали число, в заданном диапазоне

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

def game_predict(number):
    '''Оптимизируем игру, используя бинарный поиск, чтобы узнать как быстро игра угадывает число'''

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

    print(f"Ваш алгоритм угадывает число в среднем за {count} попыток)")

    return (count)


game_predict(number)
