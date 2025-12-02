def wspolne_wartosci(sekwencja1, sekwencja2):
    zbior1 = set(sekwencja1)
    zbior2 = set(sekwencja2)

    wspolne = zbior1 & zbior2

    return list(wspolne)


lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

wynik = wspolne_wartosci(lista1, lista2)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Wspólne wartości: {wynik}")

napis1 = "python"
napis2 = "programming"

wynik2 = wspolne_wartosci(napis1, napis2)
print(f"\nNapis 1: {napis1}")
print(f"Napis 2: {napis2}")
print(f"Wspólne litery: {wynik2}")

krotka1 = (10, 20, 30, 40)
krotka2 = (30, 40, 50, 60)

wynik3 = wspolne_wartosci(krotka1, krotka2)
print(f"\nKrotka 1: {krotka1}")
print(f"Krotka 2: {krotka2}")
print(f"Wspólne wartości: {wynik3}")