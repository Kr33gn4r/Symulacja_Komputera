import numpy as np
import matplotlib.pyplot as plt
from randgen import expo
# dla ułatwienia symulacji przymuje że w danej jednostce czasu jest jedno wystąpienie
# zatem co średnio 10 minut (lambd) pojawia się klient
# co średnio 8 minut (mi) obsłużony jest klient
# potem tylko wyniki należy przemnożyć przez stałą aby czasy były dobre
# czyli zamiana jednostki czasu z jakiegoś arbitralnego t (np 1 minuta) na np 8 minut

def simulation(n, lambd, mi): #lambd - czas klienta, mi - czas obsługi
    klient, obsluga = n * [0], n * [0]

    # każdy blok informuje o czasie obsługi klienta * expo(1) * jednostka czasu mi
    for i in range(n): obsluga[i] = expo(1) * mi

    # zakładam iż pierwszy klient przychodzi w czasie 0
    # każdy blok informuje o czasie przyjścia klienta i w porównaniu
    # do klienta i-1 * expo(jedno wystąpienie) * jednostka czasu lambd
    # proces taki jest procesem poissona ponieważ czas pomiędzy klientami
    # klient[i] - klient[i-1] jest w przybliżeniu równy Poiss(lambd(i - (i-1)) =
    # Poiss(lambd * 1) = Poiss(lambd)
    for i in range(1, n): klient[i] = klient[i - 1] + expo(1) * lambd

    # potrzebuje znać czas rozpoczęcia obsługi i zakończenia jej dla każdego klienta
    obsluga_poczatek, obsluga_koniec = n * [0], n * [0]
    # pierwszy klient przychodzi w czasie 0 oraz będzie obsłużony w czasie obsluga[0]
    obsluga_koniec[0] = obsluga[0]
    # sprawdzamy nakładanie się obsługi z przyjściem klienta
    for i in range(1, n):
        # jeżeli czas obsługi klienta i-1 jest mniejszy niż czas przyjścia klienta i
        # to czas przyjścia klienta i jest od razu też początkiem jego obsługi
        if (obsluga_koniec[i - 1] < klient[i]): obsluga_poczatek[i] = klient[i]
        # jeżeli natomiast tak nie jest, to początek obsługi klienta i jest równy
        # końcowi obsługi klienta i-1
        else: obsluga_poczatek[i] = obsluga_koniec[i - 1]
        # koniec obsługi klienta i jest równy czasu początku obsługi + czasu obsługi
        obsluga_koniec[i] = obsluga_poczatek[i] + obsluga[i]

    return klient, obsluga, obsluga_poczatek, obsluga_koniec

def plotsim(n, lambd, mi):
    a, b, c, d = simulation(n, lambd, mi)
    e = n * [0]
    a, c, d, e = np.array(a), np.array(c), np.array(d), np.array(e)
    for i in range(1, n):
        e[i-1] = c[i] - d[i-1]

    plt.style.use('ggplot')
    plt.title(f"Wykres kolejki M/M/1 dla średniego czasu przyjścia {lambd} minut,\nśredniego czasu obsługi {mi} minut oraz {n} klientów")
    plt.xlabel("Czas w minutach")
    plt.ylabel("Numer klienta")
    plt.barh(y=np.arange(n), width=c-a, left=a, color='crimson', label='oczekiwanie klienta')
    plt.barh(y=np.arange(n), width=d-c, left=c, color='lime', label='obsługiwanie klienta')
    plt.barh(y=np.arange(n), width=e, left=d, color='midnightblue', label='brak klienta')
    plt.legend()
    ax = plt.gca()
    ax.set_xlim([0, d[n-1]])
    ax.set_ylim([0, n])

    plt.show()

plotsim(300, 10, 8)
