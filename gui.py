from cgitb import text
from tkinter import *
from turtle import *
import math

def clear():
    #play_button.destroy()#narazie destroy bo forget cos odpierdala
    #exit_button.destroy()#dobra jednak inaczej to bedzie trzeba bo zolwik niszczy troche
    turtle = Turtle()
    turtle.getscreen().bgcolor("#d9b38c")
    turtle.pensize(5)
    turtle.penup()
    turtle.right(90)
    turtle.fd(120)
    turtle.left(90)
    turtle.pendown()
    for i in range(8):
        turtle.forward(120)
        turtle.right(90)      
        turtle.circle(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(20)
        turtle.left(112.5)
        turtle.forward(20)
        turtle.pendown()
        #turtle.fd(120*math.sqrt(4+2*math.sqrt(2)))
        turtle.fd((160*math.sqrt(4+2*math.sqrt(2))/2)-40)
        turtle.right(90)
        turtle.circle(20)
        turtle.left(270)
        turtle.fd((160*math.sqrt(4+2*math.sqrt(2))/2)-40)
        #turtle.fd(120*math.sqrt(4+2*math.sqrt(2)))
        turtle.penup()
        turtle.fd(20)
        turtle.left(112.5)
        turtle.fd(20)
        turtle.pendown()
        
    #frame.destroy()
    #canvas.create_line(0,100,300,100, fill='red')
    #canvas.pack()

#Dobra tutaj zalezy czy idziemy pod tkintera czy zolwia
root = Tk()
root.title("Mū tōrere")


canvas = Canvas(root, height = 500, width = 400)
canvas.pack()

frame = Frame(root, bg = "#d9b38c")
frame.place(relheight=1,relwidth=1)


play_button = Button(frame, text = "Zagraj",command=clear)
play_button.place(x=160,y=150,height=40,width=80)

exit_button = Button(frame, text = "Wyjdź",command=root.destroy)
exit_button.place(x=160,y=250,height=40,width=80)

mutorere_text = Text(frame,fg="#ff4d4d",bg = "#d9b38c",font=20,bd=0)
mutorere_text.insert(INSERT,"Mū tōrere")#Ta wiem biednie wyglada, uroki tkintera
mutorere_text.place(x=160,y=50,height=40,width=200)

root.mainloop()