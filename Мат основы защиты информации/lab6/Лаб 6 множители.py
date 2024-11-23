import random
from math import gcd

def pollard(n, B=20):
    a = random.randint(2, n-1)
    for j in range(2, B+1):
        a = pow(a, j, n)
    d = gcd(a-1, n)
    if 1 < d < n:
        return d
    else:
        return None

n = 21
factor = pollard(n, B=20)
if factor:
    print(f" {n} = {factor} * {int(n/factor)}")
else:
    print(f"Множители числа {n} не найдены")