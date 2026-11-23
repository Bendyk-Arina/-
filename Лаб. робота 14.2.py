import os
import time
import requests

# Створення папки для збереження картинок
folder_name = "programming_images"
os.makedirs(folder_name, exist_ok=True)

url = "https://depositphotos.com/ua/photos/%D0%BC%D0%BE%D0%B2%D0%B8-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F.html"

print("Починаємо завантаження 5 зображень...\n")

# Цикл, який повториться 5 разів
for i in range(1, 6):
    response = requests.get(url)  # Запит до сайту

    # Шлях та ім'я файлу
    file_path = f"{folder_name}/image_{i}.png"
        
        # Відкриваємо файл для запису байтів ('wb') і зберігаємо туди картинку
    with open(file_path, "wb") as file:
            file.write(response.content)
            
print("Усі фото збережено у папку:", folder_name)
