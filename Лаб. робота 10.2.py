import os
import shutil

# Ствоення папки RESULTS
os.makedirs("RESULTS", exist_ok=True)

# Зчитування вмісту папки та впорядковування його по порядку.
files = sorted(os.listdir("Python_docs"))
print("Вміст каталогу:", files)

# Копіювання 2 перших файлів
for file in files[:2]:
    source = os.path.join("Python_docs", file)
    if os.path.isfile(source):
        shutil.copy(source, "RESULTS")
        print(f"Скопійовано: {file}")