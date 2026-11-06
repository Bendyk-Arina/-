import string

# Параметр encoding="utf-8" для коректного читання українських літер
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()  # Зчитання текст із файлу в одну змінну

# Очищення тексту від розділових знаків. 
punctuation = ",.!?:;«»\"\'()—-\n"
for znak in punctuation:
    text = text.replace(znak, " ") # Заміна всіх знаків на пробіли.

# Приведення до маленьких літер та розбиваємо на слова
words = text.lower().split()

# Знаходження оригінальних слів і видалення повторів слів
unique_words = set(words)

# Підрахунок кількості оригінальних слів
count = len(unique_words)

print(f"Кількість оригінальних слів у тексті: {count}")

# Сортування всіх унікальних слів за алфавітом
sorted_words = sorted(unique_words)

# Записування результату у файл output.txt
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(f"Всього оригінальних слів: {count}\n\n")
    file.write("Список слів за алфавітом:\n")
    for word in sorted_words:
        file.write(word + "\n")  # Кожне слово з нового рядка

print("Оригінальні слова збережено у файл output.txt.")