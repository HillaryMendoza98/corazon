import turtle

# Configuración de la pantalla y el turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(1)
t.hideturtle()

# Dibujar el corazón
t.penup()
t.goto(0, -10)
t.pendown()
t.pensize(5)
t.color("purple")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(178)
t.end_fill()

# Escribir el texto centrado en el corazón
t.penup()
t.goto(-11, 150)  # Ajuste de posición para centrar el texto
t.pendown()
t.color("white")
t.write("I love you satoru", font=("Verdana", 14, "bold"), align="center")

# Mantener la ventana abierta
turtle.done()
