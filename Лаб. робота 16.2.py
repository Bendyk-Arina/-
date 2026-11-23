import matplotlib.pyplot as plt

# Читання тексту із файлу та переведення літер в нижній регістр
with open("book.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = []
counts = []

for char in alphabet:
    letters.append(char)
    counts.append(text.count(char))

# Побудова гістограми
plt.bar(letters, counts, color="skyblue", edgecolor="black")

plt.title("Частота англійських літер у тексті")
plt.xlabel("Літери")
plt.ylabel("Кількість повторень")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
