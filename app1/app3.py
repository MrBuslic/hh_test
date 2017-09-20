'''
Дано равенство, в котором цифры заменены на буквы:
syx + rvsv = ryrs 
Найдите сколько у него решений, если различным буквам соответствуют
различные цифры (ведущих нулей в числе не бывает).
Внимание: не указано система исчисления
rsrx + sxr = ruyy   # другой вариант
'''

# syx + rvsv = ryrs 
sys_base = 10
result = 0
for x in range(sys_base):
    for y in range(sys_base):
        for v in range(sys_base):
            for r in range(1, sys_base):
                for s in range(1, sys_base):
                    if (s * sys_base** 2 + y * sys_base + x + r
                        * sys_base ** 3 + v * sys_base ** 2
                        + s * sys_base + v == r * sys_base** 3
                        + y * sys_base ** 2 + r * sys_base + s):
                        print('x = {}, y = {}, v = {}, r = {}, s = {}'\
                              ''.format(x, y, v, r, s))
                        result += 1
print(result)

#rsrx + sxr = ruyy
sys_base = 10
result = 0
for u in range(sys_base):
    for y in range(sys_base):
        for x in range(sys_base):
            for r in range(1, sys_base):
                for s in range(1, sys_base):
                    if (r * sys_base ** 3 + s * sys_base ** 2 + r * sys_base + x
                        + s * sys_base ** 2 + x * sys_base + r
                        == r * sys_base** 3 + u * sys_base ** 2 + y * sys_base + y):
                        print('u = {}, y = {}, x = {}, r = {}, s = {}'\
                              ''.format(u, y, x, r, s))
                        result += 1
print(result)
