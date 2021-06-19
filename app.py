from turtle import *
import math
import tkinter.messagebox
import winsound

tl = Turtle()
pos1db = []
pos2db = []

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
p1.goto(-300,300) #Move players to set location
p2.goto(-300,-300)
p1.pendown() #Make Trail visible
p2.pendown()
p1.speed(0) #Forces movement when turning
p2.speed(0)
speed = 1 #Player Speed

listen() #Listens for Keyboard Input
#Player 1 Controls
Screen().onkey(p1left, 'a')
Screen().onkey(p1right, 'd')
#Player 2 Controls
Screen().onkey(p2left, 'Left')
Screen().onkey(p2right, 'Right')

while True:
    #Retrieving Cords
    pos1 = (p1.xcor(), p1.ycor())
    pos2 = (p2.xcor(), p2.ycor())
    
    #Collision Detection | checks player position and see if its in the array
    if pos1 in pos1db:
        tkinter.messagebox.showinfo('Game Over', "Player 2 Wins!")
        mainloop()
    if pos2 in pos2db:
        tkinter.messagebox.showinfo('Game Over', "Player 1 Wins!")
        mainloop()
    if pos1 in pos2db:
        tkinter.messagebox.showinfo('Game Over', "Player 2 Wins!")
        mainloop()
    if pos2 in pos1db:
        tkinter.messagebox.showinfo('Game Over', "Player 1 Wins!")
        mainloop()

    #Window Boundaries
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

    p1.forward(speed) #Moves Player
    p2.forward(speed)

    pos1db.append(pos1) #Logs Player Positions to Array
    pos2db.append(pos2)