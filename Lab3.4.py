x = int(input("Podaj liczbę przyjaciół: "))
n = int(input("Podaj liczbę zamówionych potraw: "))

suma_cen = 0

for i in range(1, n + 1):
    cena = float(input(f"Podaj cenę potrawy {i}: "))
    suma_cen += cena


srednia_cena = suma_cen / n
liczba_gosci = x + 1
rachunek_na_osobe = suma_cen / liczba_gosci

print(f"\nŁączna suma: {suma_cen} zł")
print(f"Średnia cena potrawy: {srednia_cena:.2f} zł")
print(f"Liczba gości: {liczba_gosci}")
print(f"Rachunek na osobę: {rachunek_na_osobe:.2f} zł")