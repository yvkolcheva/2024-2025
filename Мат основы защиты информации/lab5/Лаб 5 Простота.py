import math
import random

def Ferma(n, k):
    for i in range(k):
        a = random.randint(1, n - 1)
        if (a**(n - 1) % n != 1):
            return 'Число составное'
    return 'Число простое'

print(Ferma(7, 10))


def jacobi(a, n):
    if not(n > a > 0 and n%2 == 1):
        return 0
    s = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
        k = n % 8
        if k == 3 or k == 5:
            s = -s
        a, n = n, a
        if a % 4 == n % 4 == 3:
            s = -s
        a %= n
    if n == 1:
        return s
    else:
        return 0

print('Символ Якоби ',jacobi(7, 33))


def S_Sh(n,k):
    for i in range(k):
        a = random.randint(2, n - 3)
        r = a**((n - 1)/2) % n
        if r != 1 and r != n - 1:
            return 'Число составное'
        s = jacobi(n, a)
        if r == s % n:
            return 'Число составное'
    return 'Число простое'

print(S_Sh(15, 10))

def miller_rabin(n, k):
    if n == 2:
        return 'Число простое'
    if n % 2 == 0:
        return 'Число составное'
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return 'Число составное'
    return 'Число простое'

print(miller_rabin(7, 10))