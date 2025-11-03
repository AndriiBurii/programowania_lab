a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print(f"Dodawanie: {a} + {b} = {a + b}")
print(f"Odejmowanie: {a} - {b} = {a - b}")
print(f"Mnożenie: {a} × {b} = {a * b}")

if b != 0:
    print(f"Dzielenie: {a} ÷ {b} = {a / b}")
else:
    print(f"Dzielenie: {a} ÷ {b} = Nie można dzielić przez zero!")

print(f"Potęgowanie: {a} ^ {b} = {a ** b}")

