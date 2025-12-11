from datetime import datetime

dzisiaj = datetime.now()
print(f"Dzisiejsza data: {dzisiaj.strftime('%d.%m.%Y')}")
print()

ostatnie_lab = datetime(2025, 12, 10)
print(f"Data ostatnich laboratoriów: {ostatnie_lab.strftime('%d.%m.%Y')}")

roznica_lab = dzisiaj - ostatnie_lab
dni_od_lab = roznica_lab.days
print(f"Dni od ostatnich laboratoriów: {dni_od_lab}")
print()

kolokwium = datetime(2026, 1, 19)
print(f"Data kolokwium: {kolokwium.strftime('%d.%m.%Y')}")

roznica_kolokwium = kolokwium - dzisiaj
dni_do_kolokwium = roznica_kolokwium.days

if dni_do_kolokwium > 0:
    print(f"Dni do kolokwium: {dni_do_kolokwium}")
    print(f"\nCzas do kolokwium w przystępny sposób:")
    print(f"→ Zostało {dni_do_kolokwium} dni")

    miesiace = {
        1: 'stycznia', 2: 'lutego', 3: 'marca', 4: 'kwietnia',
        5: 'maja', 6: 'czerwca', 7: 'lipca', 8: 'sierpnia',
        9: 'września', 10: 'października', 11: 'listopada', 12: 'grudnia'
    }
    miesiac = miesiace[kolokwium.month]
    print(f"→ Kolokwium odbędzie się {kolokwium.day} {miesiac} {kolokwium.year}")

elif dni_do_kolokwium == 0:
    print("DZIŚ jest kolokwium!")
else:
    print(f"Kolokwium było {abs(dni_do_kolokwium)} dni temu")