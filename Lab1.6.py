drogę = int(input("Wpisz drogę pokonaną przez samochód:"))
spalanie = float(input("Wpisz średnie spalanie:"))
zużycie = (spalanie/100)*drogę
cena_palywa =  6.5
cena_przejazdu = zużycie*cena_palywa
print("Zużycie paliwa:", zużycie, "litrów")
print("Cena przejazdu:", cena_przejazdu)
