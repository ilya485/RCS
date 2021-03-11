# Лабораторна робота №1 на тему "Обчислення показників надійності за даними випробувань"
# Виконав студент групи ІО-71 Кизима І.Л, варіант №7

T = [577, 566, 251, 868, 2525, 26, 1040, 580, 57,
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
I_fail = 342

print("Середній наробіток: ", sum(T)/len(T))

T = sorted(T)
#print(T)
T_avg = sum(T) / len(T)
h = (T[-1] - T[0]) / 10
#print(h)

intervals = [[a for a in T if (i * h <= a <= (i + 1) * h)] for i in range(10)]
#for i in range(len(intervals)):
#    print(i * h, " - ", h * (i + 1), intervals[i])

f = [len(i) / (len(T) * h) for i in intervals]
#print("\nf list", f)

P = []
s = 1
for i in range(10):
    P.append(s)
    s -= f[i] * h
#print("P ", P)

P1 = max([p for p in P if p < gamma])
P2 = min([p for p in P if p > gamma])
index = P.index(P1)
d = (P1 - gamma) / (P1 - P2)
T_gamma = (h * index) - (h * d)
print("γ-відсотковий наробіток на відмову Tγ: ", T_gamma)

a = int(T_infail // h)
Chance = 1 - sum([f[i] * h for i in range(a)]) - f[a] * (T_infail % h)
print("Ймовірність безвідмовної роботи: ", Chance)

a = int(I_fail // h)
Intensivnost = f[int(I_fail // h)] / (1 - sum([f[i] * h for i in range(a)]) - f[a] * (I_fail % h))
print("Інтенсивність відмов: ", Intensivnost)
