"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calc_func():
    operator = input('Введите операцию (+, -, *, / или 0 для выхода) ')
    if operator == '0':
        return 'Программа завершена'
    elif operator in '+-*/':
        try:
            number_one = int(input('Введите первое число: '))
            number_two = int(input('Введите второе число: '))

            if operator == '+':
                print(f'Ответ: {number_one + number_two}')
                return calc_func()

            elif operator == '-':
                print(f'Ответ: {number_one - number_two}')
                return calc_func()

            elif operator == '*':
                print(f'Ответ: {number_one * number_two}')
                return calc_func()

            elif operator == '/':
                try:
                    print(f'Ответ: {number_one / number_two}')
                except ZeroDivisionError:
                    print('Делить на 0 нельзя!!!')
                finally:
                    calc_func()

        except:
            print('Вы вместо числа ввели строку (((. Исправьтесь.')
            calc_func()

    else:
        print(f'Вы ввели неверный оператор или оператор, который не поддерживает этот калькулятор')
        calc_func()


calc_func()
