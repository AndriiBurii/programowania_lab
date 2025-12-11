import random

szczesliva_liczba = random.randint(1, 100)
print(f"Twoja szczęśliwa liczba: {szczesliva_liczba}")
print()

roczniki = [2000, 2001, 2002, 2003, 2004, 2005]

print("Roczniki urodzenia osób w grupie:")
for i, rok in enumerate(roczniki, 1):
    print(f"Osoba {i}: {rok}")

print()

szczesliwy_rocznik = random.choice(roczniki)
print(f"Szczęśliwy rocznik: {szczesliwy_rocznik}")