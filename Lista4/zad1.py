from math import sqrt, floor, log2
from random import uniform, sample
from scipy.special import comb

N = 1000 # ilość elementów
B = 300  # maksymalna waga
sigma = 0.16
mi = 3

f_inverse = lambda: sigma * sqrt(3) * (2 * uniform(0, 1) - 1) + mi

def approx(c):
    return f"2^{log2(c)}"

def my_method(N, B, mi):
    avg_nat = floor(B / mi)
    c = 0
    for i in range(avg_nat + 1):
        c += comb(N, i, exact=True)
    ca = approx(c)
    return c, ca

def montecarlo(n, N, B):
    c = 1
    for i in range(1, N + 1):
        p = 0
        for j in range(n):
            sum = 0
            for k in range(i): sum += f_inverse()
            if sum <= B: p += 1
        c += p/n * comb(N, i, exact=True)
    ca = approx(c)
    return c, ca

def montecarlo2(ni, np, N, B):
    avg = 0
    for i in range(ni):
        c = 1
        w = [0] * N
        for j in range(N): w[j] = f_inverse()
        for j in range(1, N + 1):
            p = 0
            for k in range(np):
                sum = 0
                for l in sample(range(N), j): sum += w[l]
                if sum <= B: p += 1
            c += p/np * comb(N, j, exact=True)
        avg += c
    avg /= ni
    avga = approx(avg)
    return avg, avga

c, ca = my_method(N, B, mi)
#d, da = montecarlo(100, N, B)
d, da = montecarlo2(1, 100, N, B)
print(ca, da, approx(2 ** 1000))
