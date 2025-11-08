stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżant",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

print("Krotka stopni wojskowych:")
print(stopnie)
print()

ilosc_stopni = len(stopnie)

Major_index = stopnie.index("Major")

Pulkownik_wystepowanie = "Pułkownik" in stopnie

print("Wyniki:")
print(f"ilosc_stopni: {ilosc_stopni}")
print(f"Major_index: {Major_index}")
print(f"Pulkownik_wystepowanie: {Pulkownik_wystepowanie}")