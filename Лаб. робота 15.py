import tkinter as tk
import math

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            label_result.config(text="Коефіцієнт a не може дорівнювати 0")
            return

        d = b ** 2 - 4 * a * c

        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            label_result.config(text=f"D = {round(d, 2)}, два корені:\nx1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
        elif d == 0:
            x = -b / (2 * a)
            label_result.config(text=f"D = 0, один корінь:\nx = {round(x, 2)}")
        else:
            label_result.config(text=f"D = {round(d, 2)} < 0, дійсних коренів немає")
    except ValueError:
        label_result.config(text="Введіть коректні числа.")


# Створення вікна
window = tk.Tk()
window.title("Квадратне рівняння")
window.geometry("400x300")
window.configure(bg="green")

# Віджети для коефіцієнта a
tk.Label(window, text="Введіть a:", bg="green", fg="black").pack(pady=(10, 0))
entry_a = tk.Entry(window)
entry_a.pack()

# Віджети для коефіцієнта b
tk.Label(window, text="Введіть b:", bg="green", fg="black").pack(pady=(5, 0))
entry_b = tk.Entry(window)
entry_b.pack()

# Віджети для коефіцієнта c
tk.Label(window, text="Введіть c:", bg="green", fg="black").pack(pady=(5, 0))
entry_c = tk.Entry(window)
entry_c.pack()

# Кнопка обчислення
btn_calc = tk.Button(window, text="Обчислити", command=solve_quadratic)
btn_calc.pack(pady=10)

# Виведення результату
label_result = tk.Label(window, text="", bg="green", fg="black")
label_result.pack(pady=5)

window.mainloop()
