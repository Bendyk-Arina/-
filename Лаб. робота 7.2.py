n = int(input("Введіть кількість рядків N: "))
# Створення порожнього списку
modified_strings = []

print(f"Введіть {n} рядків (з парною кількістю літер):")
for i in range(n):
    line = input(f"Рядок {i+1}: ") # Показує порядковий номер цього рядка
    length = len(line) # Вимірювання кількості символів у рядку
    
    # Перевірка чи довжина рядка парна
    if length % 2 == 0 and length > 0:
        # Знаходження середини рядка
        mid = length // 2
        
        # Ділимо рядок на частини
        left_part = line[:mid-1] 
        middle_part = line[mid-1:mid+1].upper()  # Дві центральні літери робимо великими
        right_part = line[mid+1:]
        
        # Збираємо рядок назад
        new_line = left_part + middle_part + right_part
        modified_strings.append(new_line)
    else: 
        print("Помилка: Довжина рядка повинна бути парною, рядок пропущено.")

print("\nРезультат обробки рядків:")
for line in modified_strings: #Перебір кожного рядка у списку
    print(line)