

def separation(arr_of_dicts, first_group, first_group_keys, normal_keys):
    for i in range(19):
        if normal_keys[i] and arr_of_dicts[i]:
            first_group_keys.append(normal_keys[i])
            first_group.append(arr_of_dicts[i])
        else:
            break


def middle_number(first_group, first_group_keys):
    sum = 0
    sum_of_frequency = 0
    for i in range(len(first_group)):
        sum += first_group[i][first_group_keys[i]] * int(first_group_keys[i])
        sum_of_frequency += first_group[i][first_group_keys[i]]

    res = sum / sum_of_frequency
    print("Средняя:", res)
    return res


def deviation_and_dispersion_of_group(middle_res, first_group, first_group_keys):
    div_of_avg = []
    dispersion_of_group = 0
    for i in range(len(first_group)):
        div_of_avg.append(first_group_keys[i] - middle_res)

    print("Отклонения:", div_of_avg)
    sum_of_frequency = 0
    for k in range(len(first_group)):
        sum_of_frequency += first_group[k][first_group_keys[k]]
    sum = 0
    for j in range(len(div_of_avg)):
        sum += div_of_avg[j] ** 2 * first_group[j][first_group_keys[j]]

    print("Дисперсия:", sum / sum_of_frequency)


def properties_for_first_group(arr_of_dicts, normal_keys):
    middle_res = 0
    first_group = []
    first_group_keys = []


    separation(arr_of_dicts, first_group, first_group_keys, normal_keys)
    middle_res = middle_number(first_group, first_group_keys)
    deviation_and_dispersion_of_group(middle_res, first_group, first_group_keys)





