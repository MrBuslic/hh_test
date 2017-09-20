#Рассмотрим все возможные числа a^b для 1<a<6 и 1<b<6: 
#2^2=4, 2^3=8, 2^4=16, 2^5=32 3^2=9, 3^3=27, 3^4=81, 3^5=243 4^2=16,
#4^3=64, 4^4=256, 4^5=1024, 5^2=25, 5^3=125, 5^4=625, 5^5=3125 
#Если убрать повторения, то получим 15 различных чисел. 
#Сколько различных чисел a^b для 2<a<100 и 2<b<101?
#Сколько различных чисел a^b для 2<a<149 и 2<b<116?
def app1(a_st, a_end, b_st, b_end):
    mass = []
    for i, a in enumerate(range(a_st + 1, a_end)):
        for b in range(b_st + 1, b_end):
            t = a**b
            if t not in mass:
                mass.append(t)
        print('{}: a = {}, len(mass) = {}'.format(i, a, len(mass)))
    return len(mass)

a_st = 2
a_end = 149
b_st = 2
b_end = 116
print('app1({ast}, {aend}, {bst}, {bend}) = {r}'.format(
    ast = a_st, bst = b_st, aend = a_end, bend = b_end, r = app1(a_st, a_end, b_st, b_end)))    # ответ 15671