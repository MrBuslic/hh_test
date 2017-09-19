'''Определим функцию P(n,k) следующим образом: P(n,k) = 1,
если n может быть представлено в виде суммы k простых чисел
(простые числа в записи могут повторяться, 1 не является
простым числом) и P(n,k) = 0 в обратном случае.
К примеру, P(10,2) = 1, т.к. 10 может быть представлено
в виде суммы 3 + 7 или 5 + 5, а P(11,2) = 0, так как никакие
два простых числа не могут дать в сумме 11.
Определим функцию S(n) как сумму значений функции P(i,k)
для всех i и k, таких что 1≤i≤n, 1≤k≤n. Таким образом,
S(2) = P(1,1) + P(2,1) + P(1,2) + P(2,2) = 1,
S(10) = 20, S(1000) = 248838.

Найдите S(14185).'''

def sieve(n):
    '''
    нахождение простых чисел до n
    '''
    S = []
    for i in range(n):
        S.append(1)
    S[0] = 0
    k = 2
    while k * k <= n:
        if S[k - 1] == 1:
            i = k * k
            while i <= n:
                S[i - 1] = 0
                i += k
        k += 1
    p = []
    for i, s in enumerate(S):
        if s:
            p.append(i+1)
    return p

mass = sieve(14185)

def P(n,k):
    '''P(n,k) = 1, если n может быть представлено
в виде суммы k простых чисел'''
    if n <= 0 or k <= 0:
        return (0, ())
    if n < 2 * k:
        return (0, ())
    elif n == 2 * k:
        return (1, [2 for i in range(k)])
    K = [2 for _ in range(k)]
    K_i = [0 for _ in range(k)]
        
    while 1: #K[-1] <= n:
        if sum(K) == n:
            return 1, K
        elif sum(K) > n:
            K_i[i] = 0
            K[i] = mass[K_i[i]]
            try:
                while mass[K_i[i + 1] + 1] > n:
                    i += 1
                K_i[i + 1] += 1
                K[i + 1] = mass[K_i[i + 1]]
                continue
            except:
                return (0, ())
        for i in range(k):
            if mass[K_i[i] + 1] <= n:
                K_i[i] += 1
                K[i] = mass[K_i[i]]
                break
            K_i[i] = 0
            K[i] = mass[K_i[i]]
        else:
            return (0, ())
    return (0, ())

def S(n):
    '''S(n) сумму значений функции P(i,k)
для всех i и k, таких что 1≤i≤n, 1≤k≤n'''
    r = 0
    for i in range(n + 1):
        for j in range(n + 1):
            t = P2(i,j)[0]
            #print('P({},{}) = {}'.format(i, j, t))
            r += t
        if i % 100 == 0:
            print('S({}) = {}'.format(i, r))
    return r

def P2(n, k):
    '''Возможно более быстрое. Использую "Проблема Гольдбаха".
   При рекурсивном вызыве не правильно показывает разложение'''
    if n <= 0 or k <= 0:
        return (0, ())
    if n < 2 * k:
        return (0, ())
    elif n == 2 * k:
        return (1, [2 for i in range(k)])
    if n < 10:
        return P(n, k)
    if n % 2:   # нечетное
        if k > 3:
            while k > 3:
                n -= 2
                k -= 1
                if n <= 1:
                    return (0, ())
            return P2(n, k)
        elif k < 3:
            return P(n, k)
        else:
            return (1, ())
    else:       # четное
        if k < 4:
            return P(n, k)
        else:
            return P2(n - 3, k - 1)


print(S(14185))
