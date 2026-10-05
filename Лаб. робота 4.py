import math

def calculate_f(x):
    try:
        # Обчислюємо косинус x
        cos_x = math.cos(x)
        
        # Виводимо значення косинуса на екран, щоб бачити неціле число (наприклад, 0.99)
        print(f"--> Проміжне значення cos({x}) = {cos_x}")
        
        # Область визначення логарифма: аргумент має бути строго більшим за 0
        if cos_x <= 0:
            return "Помилка: cos(x) має бути більшим за 0 для обчислення логарифма."
            
        # Обчислюємо чисельник: 3 * tg(x)
        numerator = 3 * math.tan(x)
        
        # Обчислюємо знаменник: ln(cos(x)) + 4
        denominator = math.log(cos_x) + 4
        
        # Перевірка на ділення на нуль
        if denominator == 0:
            return "Помилка: ділення на нуль (знаменник дорівнює нулю)."
            
        # Обчислюємо другу частину: модуль (x - x^2)
        second_part = abs(x - x**2)
        
        # Підсумкове значення функції[
        result = (numerator / denominator) + second_part
        return result
        
    except Exception as e:
        return f"Сталася непередбачена помилка: {e}"

# Приклад використання:
try:
    # Запитуємо у користувача значення x
    x_input = float(input("Введіть значення x: "))
    
    # Викликаємо функцію та виводимо результат
    res = calculate_f(x_input)
    print(f"Результат f({x_input}) = {res}")
    
except ValueError:
    print("Помилка: Будь ласка, введіть коректне число.")