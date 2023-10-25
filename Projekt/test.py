from kolejki import PlaceFirst

pasazerowie = PlaceFirst(50, 1.3, 2)
for pasazer in pasazerowie:
    print(pasazer.miejsce)