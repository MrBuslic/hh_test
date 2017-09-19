import math
'''Наименьшее число m, такое, что m! делится без
остатка на 10 — это m=5 (5! = 120). Аналогично,
наименьшее число m, такое, что m! делится без остатка
на 25 — это m=10. В общем случае, значение функции
s(n) равно наименьшему числу m, такому что m! без
остатка делится на n. Определим функцию S(M, N) = ∑s(n)
для всех n ∈ [M, N]. К примеру,
S(6, 10) = 3 + 7 + 4 + 6 + 5 = 25.
Найдите S(7100000, 7200000).'''
def s(n):
    m = 0
    while math.factorial(m) % n != 0:
        m += 1
    return m

def S(M, N):
    result = 0
    r_mass = []
    for i in range(M, N + 1):
        t = s(i)
        r_mass.append(t)
        result += t
    return result, r_mass

def sieve(n):
    '''нахождение простых чисел до n'''
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

sieve_mass = sieve(7200000) # массив простых чисел

def S2(N, M):
    r = 0
    r_mass = []
    for i in range(N, M + 1):
        for j in range(len(sieve_mass) - 1, -1, -1):
            if i % sieve_mass[j] == 0:
                r += sieve_mass[j]
                r_mass.append(sieve_mass[j])
                break
    return r, r_mass

t = S(2,1000)
for i in t[1]:
    print(i)
print('S2(2, 1000)')
t = S2(2, 1000)
for i in t[1]:
    print(i)
