"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Угадываем число за количество попыток не более 7

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 #счетчик
    left_number = 1 #левая граница
    right_number = 101 #правая граница
    predict_number = np.random.randint(1, 101) # предполагаемое число

    while True: #цикл для сравнения  загаданного и предполагаемого числа
        count += 1
        if number < predict_number:
            right_number = predict_number
            predict_number = int(np.mean(np.arange(left_number - 1, right_number)))
        elif number > predict_number:
            left_number = predict_number
            predict_number = int(np.mean(np.arange(left_number, right_number + 1)))
        else:
            break  # выход из цикла если угадали
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число {number} в среднем за: {score} попыток")
    
    return score

# RUN
if __name__ == "__main__":
    score_game(random_predict)