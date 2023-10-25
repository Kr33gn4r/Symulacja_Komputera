import numpy as np
from datetime import datetime as dt

seed = int(dt.today().timestamp())

def getrandom(multiplier=1, offset=0):
    global seed
    seed = np.mod(214013 * seed + 2531011, np.power(2, 32))
    value = seed / np.power(2, 32)
    value = int(np.floor(multiplier * value) + offset)
    return value


"""
sprawozdanie:
    zad1:
        tak jak 3 i 4
    zad2:
        funckja, procedura, określona funkcja losująca
        wyciąg z wyników
        histogram teoretyczny i ten z danych otrzymanach, komentarz do tego
        nazwa testu, poziom istotności, p wartość lub obszar krytyczny i stwierdzenie wyniku
        
    zad3.json:
        kod, wyniki, histogram wyników i histogram różnic oczek pierwszego gracza
        
    zad4:
        tak jak dla 3, każdy ma po 10 strzał
"""