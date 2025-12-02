def oblicz_bmi(waga, wzrost):

    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        zakres = "niedowaga"
    elif 18.5 <= bmi <= 24.9:
        zakres = "pożądana masa ciała"
    elif 25 <= bmi <= 29.9:
        zakres = "nadwaga"
    elif 30 <= bmi <= 34.9:
        zakres = "otyłość I stopnia"
    elif 35 <= bmi <= 39.9:
        zakres = "otyłość II stopnia"
    else:
        zakres = "otyłość III stopnia"

    print(f"Twoje BMI wynosi: {bmi:.2f}")
    print(f"Jesteś w zakresie: {zakres}")

    return bmi

waga_uzytkownika = float(input("Podaj swoją wagę (kg): "))
wzrost_uzytkownika = float(input("Podaj swój wzrost (m): "))

oblicz_bmi(waga_uzytkownika, wzrost_uzytkownika)

