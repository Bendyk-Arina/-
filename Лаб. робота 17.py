import pandas as pd

# Зчитуємо таблицю з CSV-файлу у DataFrame
df = pd.read_csv("spisok.csv")

print("Початкова таблиця:")
print(df)

df["Листопад"] = [210, 350, 130]
df["Грудень"] = [280, 410, 175]

print("\nОновлена таблиця:")
print(df)

# index=False прибирає стовпчик з номерами рядків
df.to_csv("spisok_updated.csv", index=False)
