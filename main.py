import turtle
import time
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")

def sayac(saniye):
    yukseklik = turtle.window_height() // 2 - 200
    turtle.up()
    turtle.hideturtle()
    while saniye >= 0:
        turtle.clear()
        turtle.sety(yukseklik)
        turtle.write(str(saniye),align="center",font=("Arial", 100 ,"normal"))
        time.sleep(1)
        saniye -= 1

    turtle.clear()
    turtle.sety(yukseklik)
    turtle.write("Süre Bitti!", align='center', font=('Arial', 100, 'normal'))

def rastgele_konum():
    x = random.randint(-300,300)
    y = random.randint(-200,200)
    turtle.goto(x,y)

def yer_degistir():
    turtle.hideturtle()
    rastgele_konum()
    turtle.showturtle()

turtle.shape("turtle")
sayac(5)
turtle.mainloop()
