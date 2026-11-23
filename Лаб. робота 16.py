import matplotlib.pyplot as plt

# Створення списку значень x від 0 до 12
x = [i * 0.1 for i in range(0, 121)]

# Обчислення y = x^(1/2) + x^(1/3) + 1.1
y = [val ** (1/2) + val ** (1/3) + 1.1 for val in x]

# Будування графіку
plt.plot(x, y, linestyle='-', color='blue')

# Межі осі X за умовою [-0.5; 12]
plt.xlim(-0.5, 12)

# Додавання сітки та підписи осей для зручності
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції y = √x + ∛x + 1,1")

# Зберігання
plt.savefig("grafik.png")
plt.show()
