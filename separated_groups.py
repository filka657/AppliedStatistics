

def separation1(arr_of_dicts, first_group, first_group_keys, normal_keys):
    sum = 0
    for i in range(19):
        if normal_keys[i] and arr_of_dicts[i]:
            first_group_keys.append(normal_keys[i])
            first_group.append(arr_of_dicts[i])
            sum += first_group[i][normal_keys[i]]
        else:
            break
    return sum


def separation2(arr_of_dicts, second_group, second_group_keys, normal_keys):
    sum = 0
    for i in range(18):
        if normal_keys[i + 19] and arr_of_dicts[i + 19]:
            second_group_keys.append(normal_keys[i + 19])
            second_group.append(arr_of_dicts[i + 19])
            sum += second_group[i][second_group_keys[i]]
        else:
            break
    return sum


def separation3(arr_of_dicts, third_group, third_group_keys, normal_keys):
    sum = 0
    for i in range(21):
        if normal_keys[i + 37] and arr_of_dicts[i + 37]:
            third_group_keys.append(normal_keys[i + 37])
            third_group.append(arr_of_dicts[i + 37])
            sum += third_group[i][third_group_keys[i]]
        else:
            break
    return sum


def middle_number(group, group_keys):
    sum = 0
    sum_of_frequency = 0
    for i in range(len(group)):
        sum += group[i][group_keys[i]] * int(group_keys[i])
        sum_of_frequency += group[i][group_keys[i]]

    res = sum / sum_of_frequency
    print("Средняя:", res)
    return res


def deviation_and_dispersion_of_group(middle_res, group, group_keys, ):
    div_of_avg = []
    for i in range(len(group)):
        div_of_avg.append(group_keys[i] - middle_res)

    print("Отклонения:", div_of_avg)
    sum_of_frequency = 0
    for k in range(len(group)):
        sum_of_frequency += group[k][group_keys[k]]
    sum = 0
    for j in range(len(div_of_avg)):
        sum += div_of_avg[j] ** 2 * group[j][group_keys[j]]

    print("Дисперсия:", sum / sum_of_frequency)
    return sum / sum_of_frequency


def inward_dispersion(dispersion, sum):
    dis = 0
    sums = 0
    for i in range(3):
        dis += dispersion[i] * sum[i]
        sums += sum[i]

    print("\nВнутригрупповая дисперсия:", dis / sums)
    return dis / sums


def mej_dispersion(sum, res, arr_of_dicts, normal_keys):
    full_res = middle_number(arr_of_dicts, normal_keys)
    mej_dis = 0
    sums = 0
    for i in range(3):
        mej_dis += (res[i] - full_res) ** 2 * sum[i]
        sums += sum[i]
    print("Межгрупповая дисперсия:", mej_dis / sums)
    return mej_dis / sums


def properties_for_first_group(arr_of_dicts, normal_keys):

    sum = []
    res = []
    dispersion = []

    first_group = []
    first_group_keys = []

    second_group = []
    second_group_keys = []

    third_group = []
    third_group_keys = []

    sum.append(separation1(arr_of_dicts, first_group, first_group_keys, normal_keys))
    sum.append(separation2(arr_of_dicts, second_group, second_group_keys, normal_keys))
    sum.append(separation3(arr_of_dicts, third_group, third_group_keys, normal_keys))

    res.append(middle_number(first_group, first_group_keys))
    res.append(middle_number(second_group, second_group_keys))
    res.append(middle_number(third_group, third_group_keys))

    print("\n\n---Первая группа---\n")
    print(first_group)
    dispersion.append(deviation_and_dispersion_of_group(res[0], first_group, first_group_keys))
    print("\n\n---Вторая группа---\n")
    print(second_group)
    dispersion.append(deviation_and_dispersion_of_group(res[1], second_group, second_group_keys))
    print("\n\n---Третья группа---\n")
    print(third_group)
    dispersion.append(deviation_and_dispersion_of_group(res[2], third_group, third_group_keys))

    inward_dis = inward_dispersion(dispersion, sum)
    mej_dis = mej_dispersion(sum, res, arr_of_dicts, normal_keys)

    print("Общая дисперсия:", inward_dis + mej_dis)
