zdanie = input("Podaj zdanie: ")

litery_w_zdaniu = []
for znak in zdanie.lower():
    if znak.isalpha():
        litery_w_zdaniu.append(znak)

litery_w_zdaniu.sort()

print("Litery w zdaniu (alfabetycznie):")
print(litery_w_zdaniu)

unikalne_litery = set(litery_w_zdaniu)
print("Unikalne litery w zdaniu:")
print(sorted(unikalne_litery))

alfabet = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'

brakujace = []
for litera in alfabet:
    if litera not in unikalne_litery:
        brakujace.append(litera)

print("Litery alfabetu, których nie ma w zdaniu:")
print(brakujace)
print(f"Liczba brakujących liter: {len(brakujace)}")