def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))

wynik = fibonacci(n)
print(f"Wyraz {n} ciągu Fibonacciego: {wynik}")

print(f"\nPierwszych {n+1} wyrazów ciągu Fibonacciego:")
for i in range(n + 1):
    print(f"F({i}) = {fibonacci(i)}")
