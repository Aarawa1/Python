import random

# Generowanie listy 300 losowych liczb z przedziału 100-1000
numbers = []
for _ in range(300):
  numbers.append(random.randint(100, 1000))

even_sum = 0  # Suma liczb parzystych
odd_sum = 0   # Suma liczb nieparzystych

for number in numbers:
    if number % 2 == 0:  # Sprawdzenie, czy liczba jest parzysta
        even_sum += number
    else:  # Jeśli liczba nie jest parzysta, to jest nieparzysta
        odd_sum += number

print("Suma liczb parzystych:", even_sum)
print("Suma liczb nieparzystych:", odd_sum)