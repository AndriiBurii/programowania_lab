def potega(a, n):

    if n == 0:
        return 1
    else:
        return a * potega(a, n - 1)


liczba = float(input("Podaj liczbę (a): "))
wykladnik = int(input("Podaj wykładnik potęgi (n): "))

wynik = potega(liczba, wykladnik)
print(f"{liczba}^{wykladnik} = {wynik}")

