drogę = int(input("Wpisz drogę pokonaną przez samochód:"))
spalanie = float(input("Wpisz średnie spalanie:"))
zużycie = float("{:.2f}".format((spalanie/100)*drogę))
cena_palywa =  6.5
cena_przejazdu = float("{:.2f}".format(zużycie*cena_palywa))
print("Zużycie paliwa:", zużycie, "litrów")
print("Cena przejazdu:", cena_przejazdu, "PLN")
