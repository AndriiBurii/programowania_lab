ocena = int(input("Podaj ocena: "))

if ocena > 80:
    print("Zalichenie w terminie 0")
elif ocena <= 80 and ocena >= 50:
    print("Można poprawić ocenę")
elif ocena < 50:
    print("Muszą poprawić ocena")

