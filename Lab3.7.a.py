n = int(input("Podaj liczbę studentów w grupie: "))

suma_punktow = 0
liczba_poprawnych = 0
i = 0

while i < n:
    punkty = int(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))

    if punkty < 0 or punkty > 100:
        print("Błąd! Punkty muszą być w przedziale 0-100. Pomijam...")
        i += 1
        continue

    suma_punktow += punkty
    liczba_poprawnych += 1
    i += 1

if liczba_poprawnych > 0:
    srednia = suma_punktow / liczba_poprawnych
    print(f"\nŚrednia liczba punktów w grupie: {srednia:.2f}")
    print(f"Liczba studentów z poprawnymi punktami: {liczba_poprawnych}")
else:
    print("\nBrak poprawnych wyników!")