import math


def pole_trojkata(a, b, c):
    try:
        if a <= 0 or b <= 0 or c <= 0:
            print("Błąd: Boki muszą być dodatnie!")
            return None

        if a + b <= c or a + c <= b or b + c <= a:
            print("Błąd: Z tych boków nie można zbudować trójkąta!")
            return None

        s = (a + b + c) / 2

        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

        print(f"Pole trójkąta: {pole:.2f}")
        return pole

    except:
        print("Błąd: Coś poszło nie tak!")
        return None



try:
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))

    pole_trojkata(a, b, c)

except:
    print("Błąd: Podaj liczby!")
