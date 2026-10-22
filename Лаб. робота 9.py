input_string = "1.5 2.5 3.5"

# Розрізання рядку по пробілах на окремі слова
words = input_string.split()

# Перетворення списку слів на список чисел
numbers = list(map(float, words))

# Перетворення списку на кортеж
result = tuple(numbers)

print(result)