def wyswietl_parametry(*args):
    print("Przekazane parametry:")
    for i, wartosc in enumerate(args, 1):
        print(f"Parametr {i}: {wartosc}\n")


wyswietl_parametry(5)

wyswietl_parametry(10, 20, 30)

wyswietl_parametry("Python", 3.14, True, 42)