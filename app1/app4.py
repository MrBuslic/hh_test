'''В некоторых числах можно найти последовательности цифр,
которые в сумме дают 10. К примеру, в числе 3523014 целых
четыре таких последовательности:
[352]3014
3[523]014
3[5230]14
35[23014]
Можно найти и такие замечательные числа, каждая цифра которых
входит в по крайней мере одну такую последовательность.
Например, 3523014 является замечательным числом, а 28546 — нет
(в нём нет последовательности цифр, дающей в сумме 10 и при
этом включающей 5). 
Найдите количество этих замечательных чисел в интервале
[1, 9700000] (обе границы — включительно).'''

def find_10(num):
    s = str(num)
    m = [int(i) for i in s]
    fl_fig = [0 for i in range(len(m))]
    fl = 0
    for i in range(len(m)):
        for j in range(i + 1, len(m) + 1):
            if sum(m[i: j]) == 10:
                for k in range(i, j):
                    fl_fig[k] += 1
                if not 0 in fl_fig:
                    fl = 1
    return(fl, fl_fig)

def is_find_10(num):
    s = str(num)
    m = [int(i) for i in s]
    fl_fig = [0 for i in range(len(m))]
    for i in range(len(m)):
        for j in range(i + 1, len(m) + 1):
            if sum(m[i: j]) == 10:
                for k in range(i, j):
                    fl_fig[k] += 1
                if not 0 in fl_fig:
                    return 1
    return 0

r = 0
for i in range(1, 9700000 + 1):
    r += is_find_10(i)
    if i % 10000 == 0:
        print('f({}) = {}'.format(i, r))
print('finish!')
print('f({}) = {}'.format(i, r))