import temperatura

celsius1 = 21
fahrenheit1 = temperatura.c_to_f(celsius1)
print(f"{celsius1} ^C = {fahrenheit1:.2f} ^F")

fahrenheit2 = 89
celsius2 = temperatura.f_to_c(fahrenheit2)
print(f"{fahrenheit2} ^F = {celsius2:.2f} ^C")

celsius3 = 35
kelvin = temperatura.c_to_k(celsius3)
print(f"{celsius3} ^C = {kelvin:.2f} K")