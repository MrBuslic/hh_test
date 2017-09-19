'''
Дано равенство, в котором цифры заменены на буквы:
syx + rvsv = ryrs 
Найдите сколько у него решений, если различным буквам соответствуют
различные цифры (ведущих нулей в числе не бывает).
Внимание: не указано система исчисления
'''

sys_base = 10
r = 0
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
                        r += 1
print(r)
