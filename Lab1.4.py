cena = 39.99
rabat = 0.2
wartosc_koncowa = cena * (1-rabat)
cena_PLN = "{:.2f}".format(wartosc_koncowa)
print("Ostateczna cena produktu, po rabacie wynosi:", cena_PLN, "PLN")