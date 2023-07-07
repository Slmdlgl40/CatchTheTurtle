import turtle
import time
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")
kaplumbaga = turtle.Turtle()
sayac = turtle.Turtle()
def catch_turtle(saniye):
    yukseklik = turtle.window_height() // 2 - 100
    sayac.up()
    kaplumbaga.up()
    sayac.hideturtle()
    kaplumbaga.shape("turtle")
    kaplumbaga.shapesize(2,2,1)
    while saniye >= 0:
        sayac.clear()
        sayac.sety(yukseklik)
        sayac.write(str(saniye),align="center",font=("Arial", 70 ,"normal"))
        time.sleep(1)
        saniye -= 1
        kaplumbaga.hideturtle()
        rastgele_konum()
        kaplumbaga.showturtle()

    sayac.clear()
    sayac.sety(yukseklik)
    sayac.write("Süre Bitti!", align='center', font=('Arial', 70, 'normal'))

def rastgele_konum():
    x = random.randint(-400,400)
    y = random.randint(-250,220)
    kaplumbaga.goto(x,y)

catch_turtle(5)
turtle.mainloop()
