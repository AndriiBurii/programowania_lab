
paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Pozostałe paliwo: {paliwo} litrów")
    czas += 1
    paliwo -= paliwo_zuzyte_na_s
    print(f"Czas lotu: {czas} s" )
print("Koniec lotu.")