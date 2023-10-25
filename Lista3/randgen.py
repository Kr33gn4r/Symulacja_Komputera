from math import log
from datetime import datetime as dt
seed = int(dt.today().timestamp())

def uni(a=0, b=1):
    global seed
    seed = (48271 * seed) % (2 ** 31 - 1)
    value = seed / (2 ** 31 - 1)
    return (-a + b) * value + a

def expo(lambd):
    u = uni()
    x = -log(1-u)/lambd  #odwrócona dystrybuanta
    return x


