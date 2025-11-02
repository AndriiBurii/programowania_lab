with open('notowania_gieldowe.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    print("Zawartość pliku:")
    for line in lines:
        print(line.strip())