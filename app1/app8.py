'''Рассмотрим спираль, в которой, начиная с 1 в центре, последовательно
расставим числа по часовой стрелке, пока не получится спираль 5 на 5 
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
Можно проверить, что сумма всех чисел на диагоналях равна 101.
Чему будет равна сумма чисел на диагоналях, для спирали
размером 1091 на 1091?'''
def a1(n_size):
    s = 1
    for i in range(3, n_size + 1, 2):
        for j in range(4):
            s += i ** 2 - j * (i - 1)
    return s

print(a1(1091)) # ответ: 866327641