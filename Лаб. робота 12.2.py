with open("input1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

cleaned_lines = []

for line in lines:
    words = line.split()   # split() ділить рядок на слова, прибираючи всі зайві пробіли
    clean_line = " ".join(words)   # " ".join(words) з'єднує слова через один пробіл
    cleaned_lines.append(clean_line)

with open("output1.txt", "w", encoding="utf-8") as out_file:  # Записуємо результат у новий текстовий файл
    out_file.write("\n".join(cleaned_lines))

print("Зайві пробіли видалено.")