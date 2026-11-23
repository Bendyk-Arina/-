import requests
from bs4 import BeautifulSoup

url = "https://www.alice-in-wonderland.net/resources/chapters-script/alices-adventures-in-wonderland/chapter-1/"

# Завантаження вмісту сторінки
response = requests.get(url)
response.encoding = "utf-8"

# Передаємо HTML-код у BeautifulSoup для очищення від тегів
soup = BeautifulSoup(response.text, "html.parser")

# Витягування абзаців з текстом (без меню та кнопок)
paragraphs = [
    p.get_text().strip()
    for p in soup.find_all("p")
    if len(p.get_text().strip()) > 50
]
fragment = "\n\n".join(paragraphs)  # Об'єднування всіх елементів списку в один рядок (між абзацами два переноси рядка).

# Збереження результату у файл
with open("text.txt", "w", encoding="utf-8") as file:
  file.write(fragment)

print("Фрагмент книги збережено у файл text.txt")
