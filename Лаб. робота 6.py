import math

a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

print("\n1. Табулювання циклом із параметром:")
# Обчислюємо кількість кроків
n = int((b - a) / h) + 1

for i in range(n):
    x = a + i * h
    if x > b:
        break
    
    # Перевірка ОДЗ: область визначення логарифма
    if abs(x - 6) == 0:
        print(f"x = {x:.4f} -> Функція не визначена (ln(0))")
    else:
        f_x = 3 - math.log(abs(x - 6)) + math.cos(x)
        print(f"x = {x:.4f} -> f(x) = {f_x:.4f}") 