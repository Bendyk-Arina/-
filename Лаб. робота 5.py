import math
# Введення значення аргументу x
x = float(input("Введіть значення x: "))

# Обчислення функції залежності від умови
if x >= 3:
    result = math.sin(x)
elif 0 <= x < 3:
    result = math.cos(x)
else:  # x < 0
    result = math.tan(x)
print(f"f({x}) = {result}") 