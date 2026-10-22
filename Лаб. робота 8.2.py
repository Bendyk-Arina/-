import numpy as np

# 1. Введення розміру матриці
N = int(input("Введіть розмір матриці N: "))

# 2. Заповнення матриці випадковими числами від 1 до 12
matrix = np.random.randint(1, 13, size=(N, N))

print("\nПочаткова матриця:\n", matrix)

# 3. Обчислення добутку елементів головної діагоналі
product = np.prod(np.diag(matrix))
print(f"\nДобуток елементів головної діагоналі: {product}")

# 4. Заміна повторів на 0 (ваш варіант із циклом)
seen = set()

for i in range(N):      # Цикл по рядках
    for j in range(N):  # Цикл по стовпцях
        if matrix[i, j] in seen:
            matrix[i, j] = 0  # Якщо елемент вже був, замінюємо на 0
        else:
            seen.add(matrix[i, j])  # Якщо вперше, додаємо

print("\nМатриця після видалення повторів:\n", matrix)