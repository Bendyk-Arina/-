class BOOK:
    # Конструктор класу
    def __init__(self, title, author, publisher, year, pages):
        self.title = title          # Назва
        self.author = author        # Автор
        self.publisher = publisher  # Видавництво
        self.year = year            # Рік видання
        self.pages = pages          # Кількість сторінок

    # Метод для зміни року видання
    def change_year(self, new_year):
        self.year = new_year

    # Метод для зміни кількості сторінок
    def change_pages(self, new_pages):
        self.pages = new_pages

    # Допоміжний метод для зручного виведення інформації про книгу
    def __str__(self):
        return f"«{self.title}» — {self.author} ({self.publisher}, {self.year}, {self.pages} стор.)"


books = [
    BOOK("Кобзар", "Тарас Шевченко", "А-БА-БА-ГА-ЛА-МА-ГА", 2018, 704),
    BOOK("Тіні забутих предків", "Михайло Коцюбинський", "Віват", 2020, 224)
]

# Перевірка роботи методів зміни властивостей
books[0].change_year(2021)
books[0].change_pages(720)

# Додавання нової книги у список
new_book = BOOK("Місто", "Валер'ян Підмогильний", "Основи", 2019, 304)
books.append(new_book)

print("Список після додавання нової книги:")
for book in books:
    print(book)

# Вилучення нової книги зі списку
books.remove(new_book)

print("\nСписок після вилучення нової книги:")
for book in books:
    print(book)
