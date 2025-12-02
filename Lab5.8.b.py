def znajdz_maksimum(*args):
    if len(args) == 0:
        return None

    return max(args)

print(f"Maksimum: {znajdz_maksimum(5, 12, 3, 45, 7)}")
print(f"Maksimum: {znajdz_maksimum(100, 25, 67, 89, 34, 12)}")
print(f"Maksimum: {znajdz_maksimum(-5, -12, -3, -1)}")