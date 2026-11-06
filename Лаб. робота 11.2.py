import json

def save_books_to_json():
    books_list = []
    print("Введення даних про книги (для завершення залишати назву книги порожньою):")
    
    while True:
        title = input("\nВведіть назву книги: ").strip()
        if not title:
            break
            
        author = input("Введіть автора книги: ").strip()
        
        books_list.append({
            "title": title,
            "author": author
        })
    
    if books_list:
        filename = "books.json"
        # Зберігаємо дані у файл JSON з підтримкою кирилиці (ensure_ascii=False)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(books_list, file, ensure_ascii=False, indent=4)
        
        print(f"\nДані збережено у файл '{filename}'!")
    else:
        print("\nНе уведено жодної книги. Файл не створено.")

if __name__ == "__main__":
    save_books_to_json()
