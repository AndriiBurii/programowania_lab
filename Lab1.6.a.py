import random

drogę = random.randint(10,1000)
spalanie = float(input("Wpisz średnie spalanie:"))
cena_palywa =  float(input("Wpisz cena palywa:"))
zużycie = (spalanie/100)*drogę
cena_przejazdu = "{:.2f}".format(zużycie*cena_palywa)
print("Drogę pokonana:", drogę)
print("Zużycie paliwa:", zużycie, "litrów")
print("Cena przejazdu:", cena_przejazdu)