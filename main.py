import turtle

import pygame

pygame.mixer.init()
pygame.mixer.music.load('indian_national_anthem.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)

obj=turtle.Turtle()


obj.speed(1)

obj.penup()

obj.goto(-100,200)

obj.pendown()

obj.begin_fill()
obj.fillcolor("orange")

obj.forward(300)

obj.setheading(270)

obj.forward(60)

obj.setheading(180)

obj.forward(300)

obj.setheading(90)

obj.forward(60)

obj.end_fill()


obj.setheading(270)

obj.forward(120)

obj.setheading(360)

obj.forward(300)

obj.begin_fill()
obj.fillcolor("green")

obj.setheading(90)

obj.forward(120)


obj.setheading(270)
obj.forward(180)
obj.setheading(180)
obj.forward(300)
obj.setheading(90)
obj.forward(60)

obj.end_fill()

obj.setheading(360)

obj.forward(300)

obj.setheading(90)


obj.setheading(180)
obj.forward(150)


obj.color('blue')
obj.circle(-30)


obj.setheading(90)

obj.forward(30)

obj.setheading(360)




for i in range(24):
    obj.forward(30)
    obj.bk(30)
    obj.left(15)

obj.color('black')

obj.setheading(180)
obj.penup()
obj.forward(150)
obj.pendown()

obj.begin_fill()
obj.fillcolor('gray')



obj.setheading(90)
obj.forward(130)


obj.setheading(180)
obj.forward(25)
obj.setheading(270)
obj.forward(450)

obj.setheading(180)
obj.forward(60)

obj.setheading(270)
obj.forward(30)
obj.setheading(360)
obj.forward(150)

obj.setheading(90)
obj.forward(30)

obj.setheading(180)
obj.forward(65)
obj.setheading(90)
obj.forward(450)
obj.end_fill()

obj.hideturtle()

turtle.done()