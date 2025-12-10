import f_mat

print("Sposób A")
liczba1 = 10
wynik1 = f_mat.kwadrat(liczba1)
print(f"Kwadrat liczby {liczba1} = {wynik1}")

liczba2 = 3
wynik2 = f_mat.szecian(liczba2)
print(f"Szecian liczby {liczba2} = {wynik2}")

liczba3 = 10
liczba4 = 5
wynik3 = f_mat.dodaj(liczba3, liczba4)
print(f"Suma liczb {liczba3} i {liczba4} = {wynik3}")
print()

from f_mat import kwadrat, szecian, dodaj

print("Sposób B")
wynik4 = f_mat.kwadrat(liczba1)
print(f"Kwadrat liczby {liczba1} = {wynik1}")

wynik5 = f_mat.szecian(liczba2)
print(f"Szecian liczby {liczba2} = {wynik2}")

wynik6 = f_mat.dodaj(liczba3, liczba4)
print(f"Suma liczb {liczba3} i {liczba4} = {wynik3}")