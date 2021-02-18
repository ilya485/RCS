# Лабораторна робота №1 на тему "Обчислення показників надійності за даними випробувань"
# Виконав студент групи ІО-71 Кизима І.Л, варіант №7

time_table = [577, 566, 251, 868, 2525, 26, 1040, 580, 57,
376, 906, 304, 1407, 134, 62, 230, 531, 653,
2143, 515, 701, 88, 762, 337, 278, 87, 85,
10, 484, 23, 454, 61, 508, 15, 469, 309, 434,
2323, 219, 120, 66, 212, 220, 498, 522, 267,
820, 648, 18, 417, 519, 34, 662, 756, 461,
221, 291, 224, 234, 365, 416, 114, 448, 395,
71, 4, 44, 462, 537, 226, 125, 157, 18, 216,
844, 438, 730, 274, 395, 40, 481, 118, 14,
1297, 102, 249, 34, 758, 611, 159, 1115,
353, 117, 15, 158, 259, 489, 38, 1416, 2344]

gamma = 0.91
T_infail = 2245
T_fail = 342

time_table = sorted(time_table)
h = 0
ten_intervals = []
f_list = []
P_list = []

def get_T(gamma):
    global h, f_list, ten_intervals, P_list
    h = time_table[-1] / 10

    for i in range(10):
        ten_intervals.append([a for a in time_table if (i * h <= a <= (i+1) * h)])

    f_list = [len(interval) / (len(time_table) * h) for interval in ten_intervals]
    area_sum = 1

    for i in range(10):
        P_list.append(area_sum)
        area_sum -= f_list[i] * h

    p_less = max([p for p in P_list if p < gamma])
    p_more = min([p for p in P_list if p > gamma])

    index_more = P_list.index(p_more)

    d = (p_more - gamma) / (p_more - p_less)
    T = index_more + h * d
    return T


def time_unfail(time):
    Sum = 1
    whole_intervals = int(time // h)
    for i in range(whole_intervals):
        Sum -= f_list[i] * h
    Sum -= f_list[whole_intervals] * (time % h)
    return Sum


def lamb(time):
    f = f_list[int(time // h)]
    p = time_unfail(time)
    return f / p

print("Середній наробіток до відмови Tср:", sum(time_table) / len(time_table))
print("γ-відсотковий наробіток на відмову Tγ при γ = ",gamma,":", get_T(gamma))
print("ймовірність безвідмовної роботи на час", T_infail, "годин:", time_unfail(T_infail))
print("інтенсивність відмов на час ", T_fail, " годин:",  lamb(T_fail))
