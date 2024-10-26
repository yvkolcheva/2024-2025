
number1 = 15
number2 = 60

#Алгоритм Евклида
num1 = number1
num2 = number2
while num1 != 0 and num2 != 0:
    if num1 >= num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1

nod1 = num1 + num2
print(nod1)


num1 = number1
num2 = number2

#Бинарный алгоритм Евклида
g = 0
while (num1 | num2) & 1 == 0:
    g += 1
    num1 >>= 1
    num2 >>= 1
while num1 & 1 == 0:
    num1 >>= 1
while num2 != 0:
    while num2 & 1 == 0:
        num2 >>= 1
    if num1 > num2:
        num1, num2 = num2, num1
    num2 -= num1
print(num1 << g)

#Расширенный алгоритм Евклида
def ext_evk(a, b):
    if b == 0:
        return a, 1, 0
    else:
        nod, x1, y1 = ext_evk(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return nod, x, y
g,x,y = ext_evk(number1, number2)
print(f"{x} * {number1} + ( {y} ) * {number2} = {g}")

#Расширенный бинарный алгоритм Евклида
def ext_gcd(a, b):
    if a == 0: return 1, 1, b
    if b == 0: return 1, 1, a
    if not a & 1 | b & 1:
        x, y, g = ext_gcd(a >> 1, b >> 1)
        return x, y, g << 1
    elif not a & 1:
        x, y, g = ext_gcd(a >> 1, b)
        return (x - b >> 1, y + (a >> 1), g) if x & 1 else (x >> 1, y, g)
    elif not b & 1:
        x, y, g = ext_gcd(a, b >> 1)
        return (x + (b >> 1), y - a >> 1, g) if y & 1 else (x, y >> 1, g)
    elif b > a:
        x, y, g = ext_gcd(a, b - a)
        return x - y, y, g
    else:
        x, y, g = ext_gcd(a - b, b)
        return x, y - x, g


x, y, g = ext_gcd(number1, number2)
print(f"{x} * {number1} + ( {y} ) * {number2} = {g}")

