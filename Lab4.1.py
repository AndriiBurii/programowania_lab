Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print("Lista początkowa:", Moja_lista)

Moja_lista.append(100)
print(f"append(100): {Moja_lista}")

Moja_lista.insert(2, 999)
print(f"insert(2, 999): {Moja_lista}")

Moja_lista.extend([11, 12, 13])
print(f"extend([11,12,13]): {Moja_lista}")

Moja_lista.remove(3)
print(f"remove(3): {Moja_lista}")

popped = Moja_lista.pop()
print(f"pop() - usunięto {popped}: {Moja_lista}")

popped = Moja_lista.pop(3)
print(f"pop(3) - usunięto {popped}: {Moja_lista}")

print(f"Moja_lista[0]: {Moja_lista[0]}")
print(f"Moja_lista[-1]: {Moja_lista[-1]}")
print(f"Moja_lista[0:3]: {Moja_lista[0:3]}")
print(f"Moja_lista[2:7]: {Moja_lista[2:7]}")
print(f"Moja_lista[::2]: {Moja_lista[::2]}")
print(f"Moja_lista[::-1]: {Moja_lista[::-1]}")

Moja_lista.sort()
print(f"sort(): {Moja_lista}")

Moja_lista.sort(reverse=True)
print(f"sort(reverse=True): {Moja_lista}")

Moja_lista.reverse()
print(f"reverse(): {Moja_lista}")

print(f"len(Moja_lista): {len(Moja_lista)}")
print(f"max(Moja_lista): {max(Moja_lista)}")
print(f"min(Moja_lista): {min(Moja_lista)}")
print(f"sum(Moja_lista): {sum(Moja_lista)}")
print(f"sorted(Moja_lista): {sorted(Moja_lista)}")

print(f"lista + [200, 300]: {Moja_lista + [200, 300]}")
print(f"[1, 2] * 3: {[1, 2] * 3}")

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

print("Lista końcowa:", Moja_lista)