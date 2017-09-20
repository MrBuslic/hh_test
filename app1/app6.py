'''Число 125874 и результат умножения его на 2 — 251748
можно получить друг из друга перестановкой цифр. 
Найдите наименьшее положительное натуральное x такое,
что числа 5*x, 6*x можно получить друг из друга перестановкой
цифр.'''
def app6():
    i = 0
    while True:
        i += 1
        s = {fig: str(i).count(fig) for fig in sorted(set(str(i)))}
        s5 = {fig: str(i).count(fig) for fig in sorted(set(str(5 * i)))}
        s6 = {fig: str(i).count(fig) for fig in sorted(set(str(6 * i)))}
        if s == s5 and s == s6:
            return i
        elif i % 1000 == 0:
            print(i)

print('anser = {}'.format(app6()))  # ответ: 142857