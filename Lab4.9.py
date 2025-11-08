lista_zakupow = {
    "chleb": 4.50,
    "mleko": 3.20,
    "jajka": 8.90,
    "masło": 6.50,
    "ser": 12.00,
    "jabłka": 7.80,
    "pomidory": 5.40
}


print("LISTA ZAKUPÓW:")
for artykul, cena in lista_zakupow.items():
    print(f"{artykul:15s} - {cena:6.2f} zł")

suma_wydatkow = sum(lista_zakupow.values())
print(f"SUMA WYDATKÓW: {suma_wydatkow:.2f} zł")
print()
