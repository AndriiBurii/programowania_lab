litera = input("Wprowadź literę: ")


if len(litera) != 1:
    print("Błąd! Wprowadź tylko jedną literę.")
elif not litera.isalpha():
    print("Błąd! To nie jest litera.")
else:
    if litera.isupper():
        print("To jest wielka litera.")
    elif litera.islower():
        print("To jest mała litera.")