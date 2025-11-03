
# Wprowadzanie współczynników
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

print(f"Równanie: {a}x + {b} = 0")

# Rozwiązywanie
if a == 0:
    if b == 0:
        print("Nieskończenie wiele rozwiązań")
    else:
        print("Brak rozwiązań")
else:
    x = -b / a
    print(f"x = {x}")