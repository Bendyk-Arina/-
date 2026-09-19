n = int(input("Введіть трицифрове число: "))
a = n // 100
b = (n // 10) % 10
c = n % 10
average = (a + b + c) / 3
print("Середнє арифметичне цифр:", average)