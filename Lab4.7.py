moja_krotka = (10, 2, 6, 6, 9, 13, 0, 1)

print("Oryginalna krotka:")
print(moja_krotka)
print()

lista_pomocnicza = list(moja_krotka)
print("Krotka przekonwertowana na listę:")
print(lista_pomocnicza)
print()

lista_pomocnicza.sort()
print("Posortowana lista:")
print(lista_pomocnicza)
print()

posortowana_krotka = tuple(lista_pomocnicza)
print("Posortowana krotka:")
print(posortowana_krotka)
print()