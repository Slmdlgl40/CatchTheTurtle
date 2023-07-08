import turtle
import time
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("dark blue")
turtle_screen.title("Catch The Turtle")
kaplumbaga = turtle.Turtle()
sayac = turtle.Turtle()
score = turtle.Turtle()
kaplumbaga.color("green")
sayac.color("yellow")
score.color("red")
def catch_turtle(saniye):
    def rastgele_konum():
        x = random.randint(-400, 400)
        y = random.randint(-250, 220)
        kaplumbaga.goto(x, y)

    yukseklik = turtle.window_height() // 2 - 100
    puan = 0
    sayac.up()
    kaplumbaga.up()
    score.up()
    score.hideturtle()
    sayac.hideturtle()
    kaplumbaga.shape("turtle")
    kaplumbaga.shapesize(2,2,1)

    def artir_score(x,y):
        nonlocal puan
        puan += 1
        score.clear()
        score.sety(yukseklik - 70)
        score.write("Score:" + str(puan), align="center", font=("Arial", 50, "normal"))

    kaplumbaga.onclick(artir_score)

    while saniye >= 0:
        sayac.clear()
        sayac.sety(yukseklik)
        sayac.write(str(saniye),align="center",font=("Arial", 70 ,"normal"))
        score.clear()
        score.sety(yukseklik - 70)
        score.write("Score:" + str(puan),align="center",font=("Arial", 50 ,"normal"))
        kaplumbaga.hideturtle()
        rastgele_konum()
        kaplumbaga.showturtle()
        time.sleep(1)
        saniye -= 1

    sayac.clear()
    sayac.write("Süre Bitti!", align='center', font=('Arial', 70, 'normal'))
    score.clear()
    score.write("Score:" + str(puan),align="center",font=("Arial", 50 ,"normal"))


catch_turtle(5)
turtle.mainloop()
