with open('notowania_gieldowe.txt', 'a', encoding='utf-8') as file:
    file.write('\nALR, 113')

print("Dane zostały pomyślnie dodane do pliku!")



with open('notowania_gieldowe.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    print("Zaktualizowana zawartość pliku:")
    for line in lines:
        print(line.strip())