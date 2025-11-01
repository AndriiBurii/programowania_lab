x = int(input("Podaj x:"))
y = int(input("Podaj y:"))
z = int(input("Podaj z:"))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print(f"Liczby uporządkowane: {x},{y},{z}")