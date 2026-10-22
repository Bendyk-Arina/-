import array

N = int(input("Введіть ціле число N: "))

# Створюємо порожній масив
masiv = array.array('i')

# Шукаємо дільники
for i in range(1, abs(N) + 1):
    # Перевірка чи N ділиться на i без остачі
    if N % i == 0:
        masiv.append(i)

print("Початковий масив дільників:", masiv.tolist())

# Перевірка чи в масиві є хоча б 2 числа для видалення
if len(masiv) >= 2:
    min_val = min(masiv) # Найменше завжди 1
    max_val = max(masiv)   # Найбільше саме число N)
    
    # Видаляємо найменше та найбільше значення з масиву
    masiv.remove(min_val) 
    masiv.remove(max_val)  
    
    print("Масив після видалення дільників:", masiv.tolist())
else:
    print("Масив занадто малий.")