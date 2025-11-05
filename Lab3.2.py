liczby_pierwsze = []
liczba = 2

while len(liczby_pierwsze) < 10:
    jest_pierwsza = True

    dzielnik = 2
    while dzielnik < liczba:
        if liczba % dzielnik == 0:
            jest_pierwsza = False
            break
        dzielnik += 1

    if jest_pierwsza:
        liczby_pierwsze.append(liczba)

    liczba += 1

print(','.join(map(str, liczby_pierwsze)))