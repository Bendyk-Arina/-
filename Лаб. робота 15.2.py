import tkinter as tk

UA_LOWER = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
UA_UPPER = UA_LOWER.upper()
EN_LOWER = "abcdefghijklmnopqrstuvwxyz"
EN_UPPER = EN_LOWER.upper()

# Алгоритм шифрування Цезаря
def caesar(text, shift):
    result = ""
    for char in text:
        if char in UA_LOWER:
            idx = (UA_LOWER.index(char) + shift) % len(UA_LOWER)
            result += UA_LOWER[idx]
        elif char in UA_UPPER:
            idx = (UA_UPPER.index(char) + shift) % len(UA_UPPER)
            result += UA_UPPER[idx]
        elif char in EN_LOWER:
            idx = (EN_LOWER.index(char) + shift) % len(EN_LOWER)
            result += EN_LOWER[idx]
        elif char in EN_UPPER:
            idx = (EN_UPPER.index(char) + shift) % len(EN_UPPER)
            result += EN_UPPER[idx]
        else:
            result += char
    return result

# Зашифрування
def encrypt():
    try:
        shift = int(entry_shift.get())
        text = entry_text.get()
        entry_result.delete(0, tk.END)
        entry_result.insert(0, caesar(text, shift))
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Ключ має бути числом!")

# Розшифрування
def decrypt():
    try:
        shift = int(entry_shift.get())
        text = entry_text.get()
        entry_result.delete(0, tk.END)
        entry_result.insert(0, caesar(text, -shift))
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Ключ має бути числом!")

# Створення вікна
window = tk.Tk()
window.title("Шифр Цезаря")
window.geometry("400x300")

# Введення тексту
tk.Label(window, text="Введіть повідомлення:").pack(pady=(15, 0))
entry_text = tk.Entry(window, width=40)
entry_text.pack(pady=5)

# Введення ключа (зсуву)
tk.Label(window, text="Ключ (зсув):").pack(pady=(5, 0))
entry_shift = tk.Entry(window, width=10)
entry_shift.pack(pady=5)

# Кнопки дій
btn_encrypt = tk.Button(window, text="Зашифрувати", command=encrypt)
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(window, text="Розшифрувати", command=decrypt)
btn_decrypt.pack(pady=5)

# Поле результату (з нього зручно копіювати текст)
tk.Label(window, text="Результат:").pack(pady=(10, 0))
entry_result = tk.Entry(window, width=40)
entry_result.pack(pady=5)

window.mainloop()
