import turtle                     

def decode(text):     # Процедура декодування команд
    for letter in text:          
        if letter == "F":
            turtle.forward(50)    
        elif letter == "L":
            turtle.right(90)
        elif letter == "R":
            turtle.left(90)
        elif letter == "U":
            turtle.penup()
        elif letter == "D":
            turtle.pendown()

turtle.shape("turtle")
turtle.speed(2)

commands = input("Введіть команди: ")
decode(commands)

turtle.done()      # Залишаємо вікно відкритим