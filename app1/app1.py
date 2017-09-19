#Рассмотрим все возможные числа a^b для 1<a<6 и 1<b<6: 
#2^2=4, 2^3=8, 2^4=16, 2^5=32 3^2=9, 3^3=27, 3^4=81, 3^5=243 4^2=16,
#4^3=64, 4^4=256, 4^5=1024, 5^2=25, 5^3=125, 5^4=625, 5^5=3125 
#Если убрать повторения, то получим 15 различных чисел. 
#Сколько различных чисел a^b для 2<a<100 и 2<b<101?
mass = []
for i, a in enumerate(range(3, 100)):
    for b in range(3, 101):
        t = a**b
        if t not in mass:
            mass.append(t)
    print('{}: a = {}, len(mass) = {}'.format(i, a, len(mass)))