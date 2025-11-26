def powitanie(imie = "Uzytkowniku", jezyk="polski"):
    if jezyk == "polski":
        print(f"Cześć, {imie}.")
    elif jezyk == "angielski":
        print(f"Hello, {imie}.")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}.")
    else:
        print(f"Witam, {imie}.")

imie = input("Podaj imie: ")
jezyk = input("Podaj jezyk: ")
powitanie()
powitanie("andrii")