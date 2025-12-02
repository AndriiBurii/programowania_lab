def odwroc_string(tekst):
    return tekst[::-1]

tekst_uzytkownika = input("Podaj tekst do odwrócenia: ")
odwrocony = odwroc_string(tekst_uzytkownika)
print(f"Oryginalny tekst: {tekst_uzytkownika}")
print(f"Odwrócony tekst: {odwrocony}")