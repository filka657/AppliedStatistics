import matplotlib.pyplot as plt

def plotting_dist(new_arr_of_dicts, names_intervals):
    frequency = []
    for el, i in enumerate(names_intervals):
        frequency.append(new_arr_of_dicts[el][i])

    plt.bar(names_intervals, frequency)

    plt.show()