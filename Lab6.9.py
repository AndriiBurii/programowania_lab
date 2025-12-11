import math
import keyword

print("1. MODUŁ MATH")
funkcje_math = [nazwa for nazwa in dir(math) if not nazwa.startswith('_')]
print(f"Liczba funkcji/stałych w module math: {len(funkcje_math)}")
print()
for i, nazwa in enumerate(funkcje_math, 1):
    print(f"{i:2d}. {nazwa}")
print()

funkcje_tuple = [nazwa for nazwa in dir(tuple) if not nazwa.startswith('_')]
print(f"Liczba metod w typie tuple: {len(funkcje_tuple)}")
print()
for i, nazwa in enumerate(funkcje_tuple, 1):
    print(f"{i:2d}. {nazwa}")
print()

funkcje_keyword = [nazwa for nazwa in dir(keyword) if not nazwa.startswith('_')]
print(f"Liczba funkcji/zmiennych w module keyword: {len(funkcje_keyword)}")
print()
for i, nazwa in enumerate(funkcje_keyword, 1):
    print(f"{i:2d}. {nazwa}")

