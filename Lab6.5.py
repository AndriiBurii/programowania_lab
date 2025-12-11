import random

print("Losowanie 6 liczb spośród liczb od 1 do 49")
print()

liczby = list(range(1, 50))

wylosowane = random.sample(liczby, 6)

wylosowane.sort()

print("Wylosowane liczby:")
for i, liczba in enumerate(wylosowane, 1):
    print(f"Kula {i}: {liczba}")

print()
print(f"Twoje szczęśliwe liczby: {wylosowane}")