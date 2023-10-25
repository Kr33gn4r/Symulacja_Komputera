import numpy as np
import matplotlib.pyplot as plt
from zad1 import getrandom

def playDice():
    x = getrandom(6, 1)
    x += getrandom(6, 1)
    return x

def gameDice(amount):
    gracz1 = []
    gracz2 = []
    gracz1przewagi = []
    for i in range(amount):
        gracz1.append(playDice())
        gracz2.append(playDice())
        gracz1przewagi.append(gracz1[i] - gracz2[i])
    gracz1 = np.array(gracz1)
    gracz1przewagi = np.array(gracz1przewagi)
    return gracz1, gracz1przewagi

rzuty, roznice = gameDice(30)
rzuty_unique, rzuty_counts = np.unique(rzuty, return_counts=True)
roznice_unique, roznice_counts = np.unique(roznice, return_counts=True)

plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = (12, 5)
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

bars1 = ax1.bar(rzuty_unique, rzuty_counts)
ax1.bar_label(bars1)
ax1.set_title("Wyniki rzutów dla pierwszego gracza")
ax1.set_xticks(np.arange(2, 13, 1))

bars2 = ax2.bar(roznice_unique, roznice_counts, color="tab:blue")
ax2.bar_label(bars2)
ax2.set_title("Różnice punktowe dla pierwszego gracza")
ax2.set_xticks(np.arange(-10, 11, 1))
plt.show()