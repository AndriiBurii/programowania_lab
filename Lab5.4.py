def srednia_z_listy(lista):
    if len(lista) == 0:
        return "Lista jest pusta."
    suma = sum(lista)
    srednia = suma / len(lista)
    return srednia

ile_liczb = int(input("Ile liczb chcesz wprowadzić? "))
lista = []

for i in range(ile_liczb):
    liczba = float(input(f"Liczba {i}: "))
    lista.append(liczba)
print(f"Lista:{lista}")
print(f"Srednia: {srednia_z_listy(lista)}")