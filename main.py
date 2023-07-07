import turtle
import time
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")
imlec = turtle.Turtle()
def catch_turtle(saniye):
    yukseklik = turtle.window_height() // 2 - 100
    turtle.up()
    imlec.up()
    turtle.hideturtle()
    imlec.shape("turtle")
    while saniye >= 0:
        turtle.clear()
        turtle.sety(yukseklik)
        turtle.write(str(saniye),align="center",font=("Arial", 70 ,"normal"))
        time.sleep(1)
        saniye -= 1
        imlec.hideturtle()
        rastgele_konum()
        imlec.showturtle()

    turtle.clear()
    turtle.sety(yukseklik)
    turtle.write("Süre Bitti!", align='center', font=('Arial', 70, 'normal'))

def rastgele_konum():
    x = random.randint(-400,400)
    y = random.randint(-250,220)
    imlec.goto(x,y)

catch_turtle(5)
turtle.mainloop()
