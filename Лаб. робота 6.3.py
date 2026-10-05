import math

a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

results = []
x = a

while x <= b + 1e-9:
    if abs(x - 6) != 0:
        f_x = 3 - math.log(abs(x - 6)) + math.cos(x)
        # Зберігаємо округлене значення для гарного виведення
        results.append(round(f_x, 4))
    else:
        results.append("Не визначено")
    x += h

print("\n3. Виведення списку у рядок:")
print(results)

print("\nВиведення списку у стовпчик:")
for val in results:
    print(val) 