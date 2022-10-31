"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time

some_list = []
some_dict = {}


def measuring_time(func):       # декоратор для замера времени
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения : {end_time - start_time}')
        return result

    return wrapper


@measuring_time
def put_in_list(lst, n):    # Итоговая сложность: O(n)
    for i in range(n):      # O(n)
        lst.append(i)       # O(1)
    return lst       # O(1)


@measuring_time
def put_in_dict(dct, n):    # Итоговая сложность: O(n)
    for i in range(n):      # O(n)
        dct[i] = i**2
    return dct      # O(1)


put_in_list(some_list, 1000000)       # Время выполнения : 0.09374380111694336
put_in_dict(some_dict, 1000000)          # Время выполнения : 0.334186315536499
# print(some_list)          # Проверка на факт того, что эмелент добавился
# print(some_dict)

'''
Из замеров времени и сложностей операции делаю вывод, что добавление элементов в списки происходит быстрее, чем в словари.
Разница почти в 4 раза.
'''

@measuring_time
def show_elem_list(lst, idx):       # O(1)
    return lst[idx]     # O(1)


@measuring_time
def show_index_list(lst, element):      # O(n)
    for i in range(len(lst)):   # O(n)
        if lst[i] == element:   # O(1)
            return i        # O(1)
    return False            # O(1)


@measuring_time
def show_elem_dict(dct, key):       # O(1)
    return dct[key]     # O(1)

# print(show_elem_dict(some_dict, 50000))     # Время выполнения : 0.0
# print(show_elem_list(some_list, 50000))     # Время выполнения : 0.0
# print(show_index_list(some_list, 50000))    # Время выполнения : 0.031248092651367188

'''
Из замеров времени и сложностей операции делаю вывод, что извлечение элементов из списков и словарей происходит одинаково быстро.
Но если в списке нужно извлечь индекс, по которому находится нужный нам элемент, то такая операция уже проходит дольше.
'''


@measuring_time
def remove_el_list(lst, el):        # O(n)
    for i in range(len(lst)):       # O(n)
        if lst[i] == el:        # O(1)
            if i != len(lst) - 1:       # O(1)
                return lst[:i] + lst[i + 1:]        # O(1)
            else:
                return lst[:i]      # O(1)


@measuring_time
def remove_el_dict(dct, key):       # O(1)
    del dct[key]        # O(1)
    return dct          # O(1)


# remove_el_dict(some_dict, 999999)   # Время выполнения : 0.0
# remove_el_list(some_list, 999999)  # Время выполнения : 0.15018534660339355


'''
Что касается удаление из словаря и удаление из списка, то очевидно, что удаление из словаря из словаря сильно быстрее.
Ключи в словаре своего рода индексы и программа знает где искать ключ и что удалять. В списке программа ищет что удалить, так как индекс неизвестен.
'''


