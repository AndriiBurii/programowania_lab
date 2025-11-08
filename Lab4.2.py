imiona = ["Anna", "Krzysztof", "Ewa", "Bartosz"]
print("Lista początkowa:", imiona)
print()

print("a. Sortowanie alfabetyczne:")
imiona.sort()
print("   Po sortowaniu:", imiona)
print()

print("b. Dodawanie dwóch osób i usuwanie ostatniej:")
imiona.append("Zofia")
imiona.append("Marek")
print("   Po dodaniu Zofia i Marek:", imiona)
ostatnia_osoba = imiona.pop()
print(f"   Pobrano pop(): {ostatnia_osoba}")
print("   Lista po pop():", imiona)
print()

print("c. Dodanie osoby na pozycji 3:")
imiona.insert(3, "Tomasz")
print("   Po insert(3, 'Tomasz'):", imiona)
print()

print("d. Odwrócenie kolejności i zdublowanie:")
imiona.reverse()
print("   Po reverse():", imiona)
imiona = imiona * 2
print("   Po zdublowaniu (imiona * 2):", imiona)