'''Наименьшее число m, такое, что m! делится без
остатка на 10 — это m=5 (5! = 120). Аналогично,
наименьшее число m, такое, что m! делится без остатка
на 25 — это m=10. В общем случае, значение функции
s(n) равно наименьшему числу m, такому что m! без
остатка делится на n. Определим функцию S(M, N) = ∑s(n)
для всех n ∈ [M, N]. К примеру,
S(6, 10) = 3 + 7 + 4 + 6 + 5 = 25.
Найдите S(7100000, 7200000).'''
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

def IntFact(N):
    '''ф-ция разложения на простые множители'''
    d = {}
    i = 0
    while i < N:
        if N % sieve_mass[i] == 0:
            N /= sieve_mass[i]
            if sieve_mass[i] in d.keys():
                d[sieve_mass[i]] += 1
            else:
                d[sieve_mass[i]] = 1
            i -= 1
        i += 1
    return d


def s(n):
    d = IntFact(n)          # словарь разложенных прост множ
    d_keys_inv = list(d.keys())[::-1]

    m = d_keys_inv[0]       # ответ
    for dd in d_keys_inv:
        while 1:
            res_del_dd = 0      # получаймый рез
            pow_dd = 1          # степень dd
            while m / (dd ** pow_dd) >= 1:
                res_del_dd += int(m / (dd ** pow_dd))
                pow_dd += 1
            if res_del_dd < d[dd]:
                m += 1
            else:
                break
    return m

def S(M, N):
    result = 0
    r_mass = []
    for i in range(M, N + 1):
        t = s(i)
        r_mass.append(t)
        result += t
        if i % 10000 == 0:
            print('s({}) = {}'.format(i,t))
    return result, r_mass

t = S(7100000, 7200000)
print(t[0])