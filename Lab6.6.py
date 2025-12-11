import time

print("Program będzie odliczał sekundy do końca")
print()

try:
    czas = int(input("Podaj liczbę sekund do odliczenia: "))

    if czas <= 0:
        print("Liczba sekund musi być większa od 0!")
    else:
        print(f"\nOdliczanie {czas} sekund...")
        print()

        for i in range(czas, 0, -1):
            print(f"Pozostało: {i} sekund")
            time.sleep(1)

        print()
        print("KONIEC! Czas upłynął!")

except ValueError:
    print("Błąd! Proszę podać liczbę całkowitą.")