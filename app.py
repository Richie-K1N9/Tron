from turtle import *
import math
import tkinter.messagebox
import winsound

tl = Turtle()

#Window Setup
Screen().setup(750, 750)
Screen().bgcolor('black')

#Music
winsound.PlaySound('music.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )

#Player Control
def p1left():
    p1.left(90)

def p1right():
    p1.right(90)

def p2left():
    p2.left(90)

def p2right():
    p2.right(90)

#Player Setup
p1 = Turtle() #Generate Turtle
p2 = Turtle()
p1.hideturtle() #Hides Turtle
p2.hideturtle()
p1.color('blue') #Sets Colour
p2.color('red')
p1.penup() #Hides Trail
p2.penup()
p1.goto(-300,0) #Move players to set location
p2.goto(300,0)
p2.left(180) #Rotates Player 2
p1.pendown() #Make Trail visible
p2.pendown()
p1.speed(0) #Forces movement when turning
p2.speed(0)
speed = 1

listen()
#Player 1 Controls
Screen().onkey(p1left, 'a')
Screen().onkey(p1right, 'd')
#Player 2 Controls
Screen().onkey(p2left, 'Left')
Screen().onkey(p2right, 'Right')

while True:
    p1.forward(speed)
    p2.forward(speed)

    if p1.xcor() > 375 or p1.xcor() < -375:
        tkinter.messagebox.showinfo('Game Over', "Player 2 Wins!")
        mainloop()

    if p1.ycor() > 375 or p1.ycor() < -375:
        tkinter.messagebox.showinfo('Game Over', "Player 2 Wins!")
        mainloop()

    if p2.xcor() > 375 or p2.xcor() < -375:
        tkinter.messagebox.showinfo('Game Over', "Player 1 Wins!")
        mainloop()

    if p2.ycor() > 375 or p2.ycor() < -375:
        tkinter.messagebox.showinfo('Game Over', "Player 1 Wins!")
        mainloop()