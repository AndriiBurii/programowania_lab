import keyword

slowa_do_sprawdzenia = ['for', 'print', 'break', 'done', 'bad']

for slowo in slowa_do_sprawdzenia:
    if keyword.iskeyword(slowo):
        print(f"'{slowo}' - TAK, to słowo kluczowe")
    else:
        print(f"'{slowo}' - NIE, to nie jest słowo kluczowe")