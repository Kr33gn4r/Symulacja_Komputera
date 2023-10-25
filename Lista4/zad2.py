from math import e
from random import uniform

f = lambda x: e ** (-x ** 2 / 2)
a, b = 0, 1
ha, hb = f(a), f(b) #wiem że na tym przedziale funkcja jest stale malejąca
n = 1000000 # ilość punktów wylosowanych

def integral(f, a, b, ha, n):
    P = abs(b - a) * abs(ha - 0)
    c = 0

    for i in range(n):
        x = uniform(a, b)
        y = uniform(0, ha)
        fx = f(x)

        if y <= fx : c += 1
    return P * c / n

print(integral(f, a, b, ha, n))