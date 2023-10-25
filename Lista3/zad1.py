from math import e, log
from randgen import uni
def killCats(halflife, p, step, cats):
    startingcats = cats
    time = 0
    tau = halflife / log(2)
    p_decay = e ** (-step / tau)

    while (cats > startingcats * p):
        for i in range(cats):
            if uni() > p_decay: cats -= 1
        time += step
    return time

print(killCats(5730, 0.65, 0.05, 1000))
# halflife - czas połowicznego rozkładu w latach
# p - prawdopodobieństwo przeżycia kota
# step - czas kroku
# cats - ilość kotów