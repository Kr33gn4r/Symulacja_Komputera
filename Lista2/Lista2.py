from random import randint
bins = [1000, 10, 2000, 1, 5000, 1, 2000, 10, 1000]

def simulate_all_possible_moves(entry):
    winnings = 0
    for i in range(16):
        x = str(bin(i))[2:].zfill(4)
        ready = [int(x[0]), int(x[1]), int(x[2]), int(x[3])]
        winnings += pachinko(entry, ready)
    return winnings / 16


def pachinko(entry, ready = []):
    kolejnosc = []
    kolejnosc.append(entry)
    match entry.upper():
        case 'I':
            entryvalue = 0
        case 'II':
            entryvalue = 1
        case 'III':
            entryvalue = 2
        case 'IV':
            entryvalue = 3
        case 'V':
            entryvalue = 4
        case default:
            print("zły wybór")
            exit(0)

    if ready != []:
        for i in range(4):
            entryvalue += ready[i]
        return bins[entryvalue]
    else:
        for i in range(4):
            left_or_right = randint(0, 1) #0 lewo 1 prawo
            kolejnosc.append(left_or_right)
            entryvalue = entryvalue + 0 if left_or_right == 0 else entryvalue + 1
        return bins[entryvalue], kolejnosc
"""
#1.
wartość, kolejność = pachinko('I')
print(f"Wygrana wynosi: {wartość}\nWrzuciłeś kulkę do dziury: {kolejność[0]}\nRuchy kulki były takie: {kolejność[1:]}")
"""

"""
#2.
print(f"Średnia wygrana po wrzuceniu kulki do dziury III wynosi: {simulate_all_possible_moves('III')}")
"""

"""
#3.
print(f"Średnia wygrana po wrzuceniu kulki do dziury III wynosi: {simulate_all_possible_moves('I')}")
print(f"Średnia wygrana po wrzuceniu kulki do dziury III wynosi: {simulate_all_possible_moves('II')}")
print(f"Średnia wygrana po wrzuceniu kulki do dziury III wynosi: {simulate_all_possible_moves('III')}")
print(f"Średnia wygrana po wrzuceniu kulki do dziury III wynosi: {simulate_all_possible_moves('IV')}")
print(f"Średnia wygrana po wrzuceniu kulki do dziury III wynosi: {simulate_all_possible_moves('V')}")
"""

"""
#4.
bins[4] = 500
print(bins)
print(f"Średnia wygrana po wrzuceniu kulki do dziury I wynosi: {simulate_all_possible_moves('I')}")
print(f"Średnia wygrana po wrzuceniu kulki do dziury II wynosi: {simulate_all_possible_moves('II')}")
print(f"Średnia wygrana po wrzuceniu kulki do dziury III wynosi: {simulate_all_possible_moves('III')}")
print(f"Średnia wygrana po wrzuceniu kulki do dziury IV wynosi: {simulate_all_possible_moves('IV')}")
print(f"Średnia wygrana po wrzuceniu kulki do dziury V wynosi: {simulate_all_possible_moves('V')}")
"""
