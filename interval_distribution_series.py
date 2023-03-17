import math


def dicts_of_age(data, data_unique, arr_of_dicts):
    for i in data_unique:
        arr_of_dicts.append({i: data.count(i)})


def get_keys(arr_of_dicts, keys):
    for i in arr_of_dicts:
        keys.append(list(i.keys()))


def getting_the_result_interval(data, keys, arr_of_dicts, new_arr_of_dicts, h, names_intervals):
    total = 0
    j = 0
    number_first = number = data[0]
    for i in keys:
        total += arr_of_dicts[j][i[0]]

        if arr_of_dicts[-1] == arr_of_dicts[j]:
            new_arr_of_dicts.append({str(number) + ' - ' + str(keys[-1][0]): total})
            names_intervals.append(str(number) + ' - ' + str(keys[-1][0]))
            total = 0
        j += 1
        if j % h == 0 and j != 0:
            new_arr_of_dicts.append({str(number_first + j - h) + ' - ' + str(number_first + j): total})
            names_intervals.append(str(number_first + j - h) + ' - ' + str(number_first + j))
            number = number_first + j
            total = 0


def properties(minimal, m, h, last_el, arr_of_dicts, names_intervals, new_arr_of_dicts):
    avg = []
    for i in range(m):
        if i == m - 1:
            avg.append((minimal + last_el) / 2)
        else:
            avg.append((minimal + (minimal + h)) / 2)
            minimal = minimal + h
    sum = 0
    sum_of_frequency = 0
    for i in range(m):
        sum += avg[i]*arr_of_dicts[i][names_intervals[i]]
        sum_of_frequency += arr_of_dicts[i][names_intervals[i]]
    res = sum / sum_of_frequency
    print("--- Характеристики интервального ряда распределения ---")
    print("Средняя: ", res)
    div_of_avg = []
    for i in range(m):
        div_of_avg.append(avg[i] - res)
    print("Отклонение от средней: ", div_of_avg)
    sum = 0
    for i in range(m):
        sum += div_of_avg[i] ** 2 * arr_of_dicts[i][names_intervals[i]]
    sigma = math.sqrt(sum / sum_of_frequency)
    print("Дисперсия: ", sum / sum_of_frequency)
    print("Среднее квадратическое отклонение: ", sigma)

    frequency = []
    for el, i in enumerate(names_intervals):
        frequency.append(new_arr_of_dicts[el][i])

    for i in range(m):
        if (max(frequency) == new_arr_of_dicts[0][names_intervals[0]]):
            left_frequency = 0
            left_interval = int(names_intervals[0].split()[0])
            right_frequency = new_arr_of_dicts[i + 1][names_intervals[i + 1]]
            div_intervals = int(names_intervals[i].split()[2]) - left_interval
        elif (max(frequency) == new_arr_of_dicts[-1][names_intervals[-1]]):
            right_frequency = 0
            left_frequency = new_arr_of_dicts[i - 1][names_intervals[i - 1]]
            left_interval = int(names_intervals[i].split()[0])
            div_intervals = int(names_intervals[i].split()[2]) - left_interval
        elif (max(frequency) == new_arr_of_dicts[i][names_intervals[i]]):
            left_frequency = new_arr_of_dicts[i - 1][names_intervals[i - 1]]
            right_frequency = new_arr_of_dicts[i + 1][names_intervals[i + 1]]
            left_interval = int(names_intervals[i].split()[0])
            div_intervals = int(names_intervals[i].split()[2]) - left_interval

    M0 = left_interval + div_intervals *((max(frequency) - left_frequency) / (2 * max(frequency) - left_frequency - right_frequency))
    print("Мода:", M0)

    sum = 0
    for i in range(m):
        sum += arr_of_dicts[i][names_intervals[i]]
        if sum >= sum_of_frequency / 2:
            if (new_arr_of_dicts[i][names_intervals[i]] == new_arr_of_dicts[0][names_intervals[0]]):
                this_frequency = new_arr_of_dicts[i][names_intervals[i]]
                left_interval = int(names_intervals[0].split()[0])
                div_intervals = int(names_intervals[i].split()[2]) - left_interval
                sum -= arr_of_dicts[i][names_intervals[i]]
            elif (new_arr_of_dicts[i][names_intervals[i]] == new_arr_of_dicts[-1][names_intervals[-1]]):
                this_frequency = new_arr_of_dicts[i][names_intervals[i]]
                left_interval = int(names_intervals[i].split()[0])
                div_intervals = int(names_intervals[i].split()[2]) - left_interval
                sum -= arr_of_dicts[i][names_intervals[i]]
            else:
                this_frequency = new_arr_of_dicts[i][names_intervals[i]]
                left_interval = int(names_intervals[i].split()[0])
                div_intervals = int(names_intervals[i].split()[2]) - left_interval
                sum -= arr_of_dicts[i][names_intervals[i]]
            break
    Me = left_interval + div_intervals * ((sum_of_frequency / 2 - sum) / this_frequency)
    print("Медиана: ", Me)

    scope = int(names_intervals[-1].split()[2]) - int(names_intervals[0].split()[0])
    print("Размах:", scope)
    print("Коэффициент вариации:", sigma / res * 100)


