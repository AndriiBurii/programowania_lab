gol = int(input("Liczba zdobytych bramek: "))
bonus = 0

if gol >10:
    bonus = 10
elif gol > 5:
    bonus = 5

total_score = (gol*10)+bonus

print(f"Ogólna liczba zdobytych punktów: {total_score}")