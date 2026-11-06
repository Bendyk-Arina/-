import csv

# Підпрограма для збереження словника у CSV-файл
def save_students_to_csv(filename, students_dict):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        # Записуємо кожен рядок у форматі: Прізвище, Рік народження
        for last_name, birth_year in students_dict.items():
            writer.writerow([last_name, birth_year])
    print(f"Дані збережено у файл {filename}")

# Підпрограма для зчитування даних з CSV-файлу в словник
def load_students_from_csv(filename):
    students_dict = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Перевірка на порожній рядок
                    last_name, birth_year = row
                    students_dict[last_name] = int(birth_year)
        print(f"Дані зчитано з файлу {filename}")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    
    return students_dict

file_name = "students.csv"
    
students = {
        "Пікассо": 1881,
        "Далі": 1904,
        "Малевич": 1879,
        "ван Гог": 1853,
}
# Збереження та зчитування даних у словник 
save_students_to_csv(file_name, students)
loaded_students = load_students_from_csv(file_name)
    
print(loaded_students)