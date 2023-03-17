import math


def get_normal_keys(keys, normal_keys):
    for i in keys:
        normal_keys.append(i[0])


def properties_for_normal(arr_of_dicts, normal_keys):
    sum = 0
    sum_of_frequency = 0
    for i in range(len(arr_of_dicts)):
        sum += arr_of_dicts[i][normal_keys[i]] * int(normal_keys[i])
        sum_of_frequency += arr_of_dicts[i][normal_keys[i]]

    res = sum / sum_of_frequency
    print("--- Характеристики дискретного ряда распределения ---")
    print("Средняя: ", res)
    div_of_avg = []
    for i in range(len(arr_of_dicts)):
        div_of_avg.append(normal_keys[i] - res)
    print("Отклонение от средней: ", div_of_avg)
    sum = 0
    for i in range(len(arr_of_dicts)):
        sum += div_of_avg[i] ** 2 * arr_of_dicts[i][normal_keys[i]]
    sigma = math.sqrt(sum / sum_of_frequency)
    print("Дисперсия: ", sum / sum_of_frequency)
    print("Среднее квадратическое отклонение: ", sigma)

    frequency = []
    for el, i in enumerate(normal_keys):
        frequency.append(arr_of_dicts[el][i])

    for i in range(len(arr_of_dicts)):
        if max(frequency) == arr_of_dicts[i][normal_keys[i]]:
            age = normal_keys[i]
            break

    M0 = age
    print("Мода:", M0)

    sum = 0
    if (len(arr_of_dicts) % 2 == 0):
        Me = (int(normal_keys[int(len(normal_keys) / 2)]) + int(normal_keys[int(len(normal_keys) / 2) + 1])) / 2
    elif(len(arr_of_dicts) % 2 == 1):
        Me = normal_keys[math.ceil(len(normal_keys) / 2)]
    print("Медиана: ", Me)

    scope = int(normal_keys[-1]) - int(normal_keys[0])
    print("Размах:", scope)
    print("Коэффициент вариации:", sigma / res * 100)