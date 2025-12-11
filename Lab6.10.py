import math

krotka = (2, 4, 8, 16, 32, 5, 10, 20, 25, 50)

print("Krotka zawiera następujące elementy:")
for i, element in enumerate(krotka, 1):
    print(f"a{i} = {element}")

print()
print(f"Liczba elementów w krotce (n): {len(krotka)}")
print()

iloczyn = math.prod(krotka)
n = len(krotka)

srednia_geometryczna = math.pow(iloczyn, 1/n)

print("Obliczenia:")
print(f"Iloczyn wszystkich elementów: {iloczyn}")
print(f"Pierwiastek stopnia {n} z iloczynu: {srednia_geometryczna:.4f}")
print()

print(f"WYNIK: Średnia geometryczna = {srednia_geometryczna:.4f}")
print()

