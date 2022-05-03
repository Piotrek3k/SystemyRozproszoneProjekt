from cgitb import text
from tkinter import *
from turtle import *
import math
from PIL import Image, ImageTk
from gamelogic import *

image1 = Image.open('blackbadgefixed2.png')
image2 = Image.open('whitebadgefixed2.png')
image3 = Image.open('neutralbadgefixed2.png')

N0 = Node(0,1)
N1 = Node(1,1)
N2 = Node(2,1)
N3 = Node(3,1)
N4 = Node(4,2)
N5 = Node(5,2)
N6 = Node(6,2)
N7 = Node(7,2)
N8 = Node(8,0)

nodes=[N0,N1,N2,N3,N4,N5,N6,N7,N8]

mutorere_Board=GameBoard([N0,N1,N2,N3,N4,N5,N6,N7,N8])

class Button(Button):
    def changeColor(self,pos):
        node=nodes[pos]
        color=node.color
        for i in range(len(nodes)):
            if nodes[i].color==0:
               GameBoard.move(node,nodes[i])
               self.configure(image=neutral_badge)
               turtle_buttons[i].configure(image=black_badge)
               if color==1:
                   turtle_buttons[i].configure(image=black_badge)
               elif color==2:
                   turtle_buttons[i].configure(image=white_badge)
               break


def play():
    turtle_window=Toplevel(root,bg='#d9b38c')
    turtle_canvas=Canvas(turtle_window,width=600, height=600)
    turtle_canvas.pack()
    turtle_screen=TurtleScreen(turtle_canvas)
    turtle_screen.bgcolor("#d9b38c")
    turtle = RawTurtle(turtle_screen)

    global turtle_button0
    global turtle_button1
    global turtle_button2
    global turtle_button3
    global turtle_button4
    global turtle_button5
    global turtle_button6
    global turtle_button7
    global turtle_button8
    global turtle_buttons



    turtle_button0 = Button(turtle_window,bd=0, image=black_badge,borderwidth=0)
    turtle_button0.configure(command=lambda:turtle_button0.changeColor(0))
    turtle_button0.place(x=209,y=96,height=26,width=26)  
    
    turtle_button1 = Button(turtle_window,bd=0, image=black_badge,borderwidth=0)
    turtle_button1.configure(command=lambda:turtle_button1.changeColor(1))
    turtle_button1.place(x=96,y=209,height=26,width=26) 

    turtle_button2 = Button(turtle_window,bd=0, image=black_badge,borderwidth=0)
    turtle_button2.configure(command=lambda:turtle_button2.changeColor(2))
    turtle_button2.place(x=96,y=370,height=26,width=26) 

    turtle_button3 = Button(turtle_window,bd=0, image=black_badge,borderwidth=0)
    turtle_button3.configure(command=lambda:turtle_button3.changeColor(3))
    turtle_button3.place(x=209,y=483,height=26,width=26)  

    turtle_button7 = Button(turtle_window,bd=0, image=white_badge,borderwidth=0)
    turtle_button7.configure(command=lambda:turtle_button7.changeColor(7))
    turtle_button7.place(x=370,y=96,height=26,width=26)  

    turtle_button6 = Button(turtle_window,bd=0, image=white_badge,borderwidth=0)
    turtle_button6.configure(command=lambda:turtle_button6.changeColor(6))
    turtle_button6.place(x=483,y=209,height=26,width=26) 

    turtle_button5 = Button(turtle_window,bd=0, image=white_badge,borderwidth=0)
    turtle_button5.configure(command=lambda:turtle_button5.changeColor(5))
    turtle_button5.place(x=483,y=370,height=26,width=26) 

    turtle_button4 = Button(turtle_window,bd=0, image=white_badge,borderwidth=0)
    turtle_button4.configure(command=lambda:turtle_button4.changeColor(4))
    turtle_button4.place(x=370,y=482,height=26,width=26)  

    turtle_button8 = Button(turtle_window,bd=0, image = neutral_badge,borderwidth=0)
    turtle_button8.configure(command=lambda:turtle_button8.changeColor(8))
    turtle_button8.place(x=289,y=289,height=26,width=26)  

    turtle_buttons=[turtle_button0,turtle_button1,turtle_button2,turtle_button3,turtle_button4,turtle_button5,turtle_button6,turtle_button7,turtle_button8]
    turtle.pensize(5)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.right(90)
    turtle.fd((160*(1+math.sqrt(2)))/2)
    turtle.right(90)
    turtle.fd(60)
    turtle.left(180)
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
        turtle.fd((160*math.sqrt(4+2*math.sqrt(2))/2)-40)
        turtle.right(90)
        turtle.circle(20)
        turtle.left(270)
        turtle.fd((160*math.sqrt(4+2*math.sqrt(2))/2)-40)
        turtle.penup()
        turtle.fd(20)
        turtle.left(112.5)
        turtle.fd(20)
        turtle.pendown()
    turtle_window.mainloop()#zobaczymy dziala bez

root = Tk()
root.title("Mū tōrere")

black_badge= ImageTk.PhotoImage(image1)
white_badge= ImageTk.PhotoImage(image2)
neutral_badge=ImageTk.PhotoImage(image3)

canvas = Canvas(root, height = 500, width = 400)
canvas.pack()

frame = Frame(root, bg = "#d9b38c")
frame.place(relheight=1,relwidth=1)


play_button = Button(frame, text = "Zagraj",command=play)
play_button.place(x=160,y=150,height=40,width=80)

exit_button = Button(frame, text = "Wyjdź",command=root.destroy)
exit_button.place(x=160,y=250,height=40,width=80)

mutorere_text = Text(frame,fg="#ff4d4d",bg = "#d9b38c",font=20,bd=0)
mutorere_text.insert(INSERT,"Mū tōrere")
mutorere_text.place(x=160,y=50,height=40,width=200)

root.mainloop()