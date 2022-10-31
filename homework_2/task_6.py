"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint, seed
#seed(1)
x = randint(1, 100)


def guess_number(num, amount=10):
    if amount == 0:
        print(f'Очень жаль. Вы не угадали. загаданное число = {num}. Попробуйте еще раз.')
        return
    attempt = int(input('Введите число от 1 до 100 '))
    if attempt < num:
        print(f'Загаданное число больше вашего. Осталось {amount - 1} попыток.')
        guess_number(num, amount - 1)
    elif attempt > num:
        print(f'Загаданное число меньше вашего. Осталось {amount - 1} попыток.')
        guess_number(num, amount - 1)
    elif attempt == num:
        print('Поздравляю. Вы угадали!')
        return

guess_number(x)