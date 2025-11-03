import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

print(f"Równanie: {a}x² + {b}x + {c} = 0")

if a == 0:
    if b == 0:
        if c == 0:
            print("Nieskończenie wiele rozwiązań")
        else:
            print("Brak rozwiązań")
    else:
        x = -c / b
        print(f"Równanie liniowe: x = {x}")
else:
    D = b ** 2 - 4 * a * c
    print(f"D = {D}")

    if D < 0:
        print("Brak rozwiązań rzeczywistych")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Jedno rozwiązanie: x = {x}")
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print(f"Dwa rozwiązania:")
        print(f"x₁ = {x1}")
        print(f"x₂ = {x2}")