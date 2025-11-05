imie = input("Podaj imię: ")
print("Witaj", imie)

wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
inicjaly = imie[0] + "." + nazwisko[0] + "."
print("Inicjały:", inicjaly)

lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
lancuch3 = lancuch1 + lancuch2
print("Połączony łańcuch:", lancuch3)

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polowa1 = lancuch1[:len(lancuch1)//2]
polowa2 = lancuch2[:len(lancuch2)//2]
lancuch3 = polowa1 + polowa2
print("Pierwsza połowa każdego łańcucha:", lancuch3)