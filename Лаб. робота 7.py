s = input("Введіть рядок")

# розділяємо рядок на слова за пробілами
words = s.split()

if words:

    # рахуємо кількість слів
    word_count = len(words)

    # знаходимо найдовше слово
    longest_word = max(words, key=len)



print("Кількість слів у рядку:", word_count)
print("Найдовше слово:", longest_word) 