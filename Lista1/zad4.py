import numpy as np
import matplotlib.pyplot as plt
import math
from zad1 import getrandom
from scipy.stats import ttest_ind
#standard tarczy FITA 80cm (długość pomiędzy pierścieniami wynosi 4cm)

def first_bowman():
    angle = getrandom(360)
    wind = getrandom(1001)
    score = max(10 - int(wind/40), 0)
    return score

def second_bowman():
    x = getrandom(901, -900)
    y = getrandom(901, -900)
    distance = math.sqrt(x**2 + y**2)
    score = max(10 - int(distance/40), 0)
    return score

def bow_competition(amount):
    first_score_list = []
    second_score_list = []
    winning_list = []
    for i in range(amount):
        first_score = 0
        second_score = 0
        for j in range(10):
            first_score += first_bowman()
            second_score += second_bowman()
        first_score_list.append(first_score)
        second_score_list.append(second_score)
        if first_score == second_score: winning_list.append(0)
        else: winning_list.append((first_score-second_score) / abs(first_score - second_score))
    return np.array(first_score_list), np.array(second_score_list), np.array(winning_list)

wyniki1, wyniki2, wygrane = bow_competition(20)
unique, counts = np.unique(wygrane, return_counts=True)

print("H0: Gracze średnio uzyskują równe wyniki")
print("HA: Gracze średnio uzyskują różne wyniki")
stat, p = ttest_ind(wyniki1, wyniki2)
print(stat, p)
if p < 0.05: print("Różnice nie są wystarczająco znaczące dla poziomu istotności 95%, zatem przyjmujemy H0")
else: print("Różnice są wystarczające dla poziomu istotności 95% aby odrzucić H0, przyjmując tym HA")

plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = (12, 5)
f, (ax1, ax2) = plt.subplots(1, 2, sharey=False)

ax1.hist(wyniki1, label="Pierwszy łucznik", color="tab:orange", histtype='bar')
ax1.hist(wyniki2, label="Drugi łucznik", color="tab:blue", histtype='bar')
ax1.legend()
ax1.set_title("Częstość występowania ilości punktów")

bintuple = []
for i in unique:
    if i == -1: bintuple.append("Przegrane")
    elif i == 0: bintuple.append("Remisy")
    else: bintuple.append("Wygrane")

bars = ax2.bar(unique, counts)
ax2.set_xticks(unique, tuple(bintuple))
ax2.bar_label(bars)
ax2.set_title("Wyniki gry dla pierwszego gracza")

plt.show()