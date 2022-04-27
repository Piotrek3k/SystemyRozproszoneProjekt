from cgitb import text
from tkinter import *
from turtle import *
import math
from PIL import Image, ImageTk

image1 = Image.open('blackbadgefixed2.png')
image2 = Image.open('whitebadgefixed2.png')


class Button(Button):
    def changeColor(self):
        self.configure(image=white_badge)
def clear():
    turtle_window=Toplevel(root,bg='#d9b38c')
    turtle_canvas=Canvas(turtle_window,width=600, height=600)
    turtle_canvas.pack()
    turtle_screen=TurtleScreen(turtle_canvas)
    turtle_screen.bgcolor("#d9b38c")
    turtle = RawTurtle(turtle_screen)

    turtle_button1 = Button(turtle_window,bd=0, image=black_badge,borderwidth=0)
    turtle_button1.configure(command=turtle_button1.changeColor)
    turtle_button1.place(x=205,y=90,height=36,width=36)  
    
    turtle_button2 = Button(turtle_window,bd=0, image=black_badge,borderwidth=0)
    turtle_button2.configure(command=turtle_button2.changeColor)
    turtle_button2.place(x=93,y=205,height=36,width=36) 

    turtle_button3 = Button(turtle_window,bd=0, image=black_badge,borderwidth=0)
    turtle_button3.configure(command=turtle_button3.changeColor)
    turtle_button3.place(x=93,y=365,height=36,width=36) 

    turtle_button4 = Button(turtle_window,bd=0, image=black_badge,borderwidth=0)
    turtle_button4.configure(command=turtle_button4.changeColor)
    turtle_button4.place(x=205,y=477,height=36,width=36)  

    turtle_button5 = Button(turtle_window,bd=0, image=white_badge,borderwidth=0)
    turtle_button5.configure(command=turtle_button5.changeColor)
    turtle_button5.place(x=366,y=90,height=36,width=36)  

    turtle_button6 = Button(turtle_window,bd=0, image=white_badge,borderwidth=0)
    turtle_button6.configure(command=turtle_button6.changeColor)
    turtle_button6.place(x=478,y=205,height=36,width=36) 

    turtle_button7 = Button(turtle_window,bd=0, image=white_badge,borderwidth=0)
    turtle_button7.configure(command=turtle_button7.changeColor)
    turtle_button7.place(x=478,y=365,height=36,width=36) 

    turtle_button8 = Button(turtle_window,bd=0, image=white_badge,borderwidth=0)
    turtle_button8.configure(command=turtle_button8.changeColor)
    turtle_button8.place(x=366,y=477,height=36,width=36)  

    turtle_button9 = Button(turtle_window,bd=0, bg='#d9b38c',borderwidth=0)
    turtle_button9.configure(command=turtle_button8.changeColor)
    turtle_button9.place(x=285,y=285,height=36,width=36)  

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

canvas = Canvas(root, height = 500, width = 400)
canvas.pack()

frame = Frame(root, bg = "#d9b38c")
frame.place(relheight=1,relwidth=1)


play_button = Button(frame, text = "Zagraj",command=clear)
play_button.place(x=160,y=150,height=40,width=80)

exit_button = Button(frame, text = "Wyjdź",command=root.destroy)
exit_button.place(x=160,y=250,height=40,width=80)

mutorere_text = Text(frame,fg="#ff4d4d",bg = "#d9b38c",font=20,bd=0)
mutorere_text.insert(INSERT,"Mū tōrere")
mutorere_text.place(x=160,y=50,height=40,width=200)

root.mainloop()