ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

for ulica in ulice:
    for blok in range(1,6):
        for lokal in range(1,11):
            print(f"{ulica} {blok}/{lokal}")