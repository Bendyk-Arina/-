import pandas as pd

# Зчитування списку рядків із файлу (прибираючи зайві пробіли та переноси рядків)
with open("Вкусность.txt", "r", encoding="utf-8") as file:
    items = [line.strip() for line in file if line.strip()]

# Видалення дублікатів, зберігаючи початковий порядок елементів
unique_items = list(dict.fromkeys(items))

# Створюємо масив Series
series = pd.Series(unique_items)

print("Отриманий масив Series:")
print(series)

# Зберігаємо Series у файл result.txt
with open("result.txt", "w", encoding="utf-8") as out_file:
    out_file.write(series.to_string(index=False))
