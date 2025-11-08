print("ZADANIE A")
imie = input("Podaj imię: ")
print("Witaj", imie)
print()

print("ZADANIE B")
wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)
print()

print("ZADANIE C")
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print("Inicjały:", imie[0] + nazwisko[0])
print()

print("ZADANIE D")
lancuch = input("Podaj łańcuch: ")
print("Pięć razy:", lancuch * 5)
print()

print("ZADANIE E")
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
print("Połączone łańcuchy:", lancuch1 + " " + lancuch2)
print()

print("ZADANIE F")
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")

polowa1 = len(lancuch1) // 2
polowa2 = len(lancuch2) // 2

pierwsza_polowa = lancuch1[:polowa1]

druga_polowa = lancuch2[polowa2:]

lancuch3 = pierwsza_polowa + druga_polowa
print("Wynik:", lancuch3)
