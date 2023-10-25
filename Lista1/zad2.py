import numpy as np
import matplotlib.pyplot as plt
from zad1 import getrandom
from scipy.stats import chisquare
#0 = Kamień, 1 = Papier, 2 = Nożyce

def RPShand(amount, player):
    for i in range(amount):
        player.append(getrandom(3))

def RPSgame(amount):
    gracz1 = []
    gracz2 = []
    gracz1wynik = []
    RPShand(amount, gracz1)
    RPShand(amount, gracz2)
    for i in range(amount):
        if gracz1[i]==0 and gracz2[i]==1 or gracz1[i]==1 and gracz2[i]==2 or gracz1[i]==2 and gracz2[i]==0: gracz1wynik.append(-1)
        elif gracz1[i]==gracz2[i]: gracz1wynik.append(0)
        else: gracz1wynik.append(1)
    return gracz1wynik

wyniki = RPSgame(100)
wyniki = np.array(wyniki)
unique, counts = np.unique(wyniki, return_counts=True)

print("H0: Każda opcja w KPN ma taką samą szansę wygrania")
print("HA: Jedna z opcji w KPN ma większą szansę na wygranie")
stat, p = chisquare(counts)
print(stat, p)
if p > 0.05: print("Różnice nie są wystarczająco znaczące dla poziomu istotności 95%, zatem przyjmujemy H0")
else: print("Różnice są wystarczające dla poziomu istotności 95% aby odrzucić H0, przyjmując tym HA")

plt.style.use('ggplot')
f, ax = plt.subplots()
bars = ax.bar(unique, counts)
ax.set_xticks(unique, ("Przegrane", "Remisy", "Wygrane"))
ax.bar_label(bars)
ax.set_title("Wyniki gry dla pierwszego gracza")
plt.show()
