from cgitb import text
from threading import Thread
from tkinter import *
from turtle import *
import math
from unicodedata import numeric
from PIL import Image, ImageTk
from gamelogic import *
import socket as sc


# dane do połączenia z serwerem
PORT = 2223
BUF_SIZE = 1024
SERVER = sc.gethostbyname(sc.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG="UTRACONO POŁĄCZENIE"


winner=-1

client=sc.socket(sc.AF_INET,sc.SOCK_STREAM)
#laczymy sie z serwerem
client.connect(ADDR)

#uporzadkowanie adresow otrzymanych z serwera
def oneAddress(msg):
    address=[]
    addrs=""
    x=10
    if(len(msg)==5):      
        x=5
    for i in range(x):
        addrs=addrs+msg[i]
        if(i==4 or i==9):
            address.append(addrs)
            addrs=""
    return address

# wysyla wiadomosc na serwer
def send(msg):
    new_msg = msg.encode(FORMAT) #string -->bajty
    msg_length=len(new_msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (BUF_SIZE - len(send_length)) #3ba dodac blanki zeby bylo 64
    client.send(send_length)
    client.send(new_msg)#troche dzike 

#ustala graczy
def start():
    global player 
    player = -1
    msg=client.recv(BUF_SIZE).decode()  
    addresses=oneAddress(msg)           
    if(len(addresses)==1):
        player=0
    else:
        player=1

start()



# odbiera i dekoduje wiadomosc z serwera
def recvMsg():
    counter=0
    tmp=0
    while True:
        msg=client.recv(BUF_SIZE).decode()
        if len(msg)==0:
            break
        if len(msg)!=10 and len(msg)!=5: 
            # dzieli wiadomosc na czesci            
            x=msg[0]
            int_msg1=int(x)
            x=msg[1]
            int_msg2=int(x)
            x=msg[2]+msg[3]
            int_msg3=int(x)
            turtle_buttons[int_msg1].configure(image=neutral_badge)
            tmp=nodes[int_msg1].color
            nodes[int_msg1].color=12
            counter+=1
            if tmp==10:
                turtle_buttons[int_msg2].configure(image=black_badge)
                nodes[int_msg2].color=10
            elif tmp==11:
                turtle_buttons[int_msg2].configure(image=white_badge)
                nodes[int_msg2].color=11
            tmp=0
            GameBoard.movecount=int_msg3
            number_of_moves.config(text="Liczba posunięć: "+ str(GameBoard.movecount - 16))
            #Sprawdzanie warunkow konca gry
            black_move=hasAnyMoves(0)
            white_move=hasAnyMoves(1)
            if black_move!=white_move:
                
                if (black_move==True and player==0):
                    status.configure(text="Wygrałeś")
                elif (white_move==True and player==1):
                    status.configure(text="Wygrałeś")
                else:
                    status.configure(text="Przegrałeś")
            if GameBoard.movecount>=99:
                status.configure(text="Remis")

            

                


#watek odpowiadajacy za odbieranie wiadmosci

recvThread=Thread(target=recvMsg)
recvThread.daemon=True
recvThread.start()




#obrazki zetonow oraz tekstu

image1 = Image.open('blackbadgefixed2.png')
image2 = Image.open('whitebadgefixed2.png')
image3 = Image.open('neutralbadgefixed2.png')
img = Image.open("Opis.png")
img1 = Image.open("Zasady.png")
img2 = Image.open("Plansza.png")

# inicjacja wezlow
N0 = Node(0,10)
N1 = Node(1,10)
N2 = Node(2,10)
N3 = Node(3,10)
N4 = Node(4,11)
N5 = Node(5,11)
N6 = Node(6,11)
N7 = Node(7,11)
N8 = Node(8,12)

nodes=[N0,N1,N2,N3,N4,N5,N6,N7,N8]
#inicjacja planszy
mutorere_Board=GameBoard([N0,N1,N2,N3,N4,N5,N6,N7,N8])
GameBoard.movecount=16

#modyfikacja klasy button w celu zmiany koloru (obrazu) przycisku
#implementacja ruchu 
class Button(Button): 
    def changeColor(self,pos):
        node=nodes[pos]
        ugabuga=node.test(nodes,player)
        if ugabuga==True:
            if(player==0 and GameBoard.movecount==16):
                node=nodes[pos]
                str_pos=str(pos)
                if(pos == 0 or pos == 3):
                    for i in range(len(nodes)):
                        if nodes[i].color==12:
                            possibility =node.is_possible_to_move(nodes[i],player)
                            if possibility==True:            
                                GameBoard.movecount+=1
                                turn=GameBoard.movecount
                                msg=str_pos+str(i)+str(turn)
                                str(send(str(msg)))
            elif player==0 and GameBoard.movecount%2==0:
                    node=nodes[pos]
                    str_pos=str(pos)
                    for i in range(len(nodes)):
                        if nodes[i].color==12:
                            possibility =node.is_possible_to_move(nodes[i],player)
                            if possibility==True:            
                                GameBoard.movecount+=1
                                turn=GameBoard.movecount
                                msg=str_pos+str(i)+str(turn)
                                str(send(str(msg)))
            elif player==1 and GameBoard.movecount%2!=0:
                    node=nodes[pos]
                    str_pos=str(pos)
                    for i in range(len(nodes)):
                        if nodes[i].color==12:
                            possibility =node.is_possible_to_move(nodes[i],player)
                            if possibility==True:                        
                                GameBoard.movecount+=1
                                turn=GameBoard.movecount
                                msg=str_pos+str(i)+str(turn)
                                str(send(str(msg)))
#sprawdzanie możliwosci wykonania ruchu (dla wszystkich węzłow)
def hasAnyMoves(player):
    for i in range (len(nodes)):
        if(player == 0 and nodes[i].color == 10):
            for j in range (len(nodes)):
                if(nodes[i].is_possible_to_move(nodes[j],player)):
                    return True         
        elif(player == 1 and nodes[i].color == 11):
            for j in range (len(nodes)):
                if(nodes[i].is_possible_to_move(nodes[j],player)):
                    return True         
    return False



# okno z rozgrywką
def play():

    play_button.destroy()

    turtle_window=Toplevel(root,bg='#d9b38c')
    turtle_canvas=Canvas(turtle_window,width=600, height=600)
    turtle_canvas.pack()
    turtle_screen=TurtleScreen(turtle_canvas)
    turtle_screen.bgcolor("#d9b38c")
    turtle = RawTurtle(turtle_screen)

    global number_of_moves
    number_of_moves = Label(turtle_window,bg = "#d9b38c", font = 14, text = "Liczba posunięć: "+ str(GameBoard.movecount - 16))
    number_of_moves.place(x = 40,y = 570)  
    global status
    status = Label(turtle_window,bg = "#d9b38c", font = 30, text = "")
    status.place(x = 300,y = 20) 

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

    #implementacja żetonów jako przycisków   

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

    #rysowanie planszy z wykorzystaniem turtle
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
    turtle_window.resizable(False,False)
    turtle_window.mainloop()



# Okienko instrukcji i informacji
def gameInfo():
    gameinfo=Toplevel(root,bg='#d9b38c')
    gameinfocanvas=Canvas(gameinfo,bg='#d9b38c',width=672, height=804)
    gameinfocanvas.pack()

    desImg = ImageTk.PhotoImage(img)
    boardImg=ImageTk.PhotoImage(img1)
    rulesImg=ImageTk.PhotoImage(img2)
    #Informacje dotyczace gry wyswietlone za pomoca obrazkow
    desLabel = Label(gameinfocanvas, image = desImg,bg='#d9b38c')
    desLabel.place(y=100)

    rulesLabel = Label(gameinfocanvas, image = rulesImg,bg='#d9b38c')
    rulesLabel.place(y=330)

    boardLabel = Label(gameinfocanvas, image = boardImg,bg='#d9b38c')
    boardLabel.place(y=514)

    description_text = Text(gameinfocanvas,fg="#ff4d4d",bg = "#d9b38c",font=20,bd=0)
    description_text.insert(INSERT,"Opis gry")
    description_text.place(x=300,y=50,height=40,width=80)

    board_text = Text(gameinfocanvas,fg="#ff4d4d",bg = "#d9b38c",font=20,bd=0)
    board_text.insert(INSERT,"Plansza")
    board_text.place(x=300,y=280,height=40,width=80)

    rules_text = Text(gameinfocanvas,fg="#ff4d4d",bg = "#d9b38c",font=20,bd=0)
    rules_text.insert(INSERT,"Zasady")
    rules_text.place(x=300,y=450,height=40,width=80)

    exit_button = Button(gameinfocanvas, text = "Wyjdź",command=gameinfo.destroy)
    exit_button.place(x=290,y=754,height=40,width=80)

    gameinfo.mainloop()

def destroy():
    str(send(DISCONNECT_MSG))
    root.destroy()



# Okienko menu 
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

exit_button = Button(frame, text = "Wyjdź",command=lambda:destroy())
exit_button.place(x=160,y=350,height=40,width=80)

description_button = Button(frame, text = "Opis gry",command=gameInfo)
description_button.place(x=160,y=250,height=40,width=80)


mutorere_text = Text(frame,fg="#ff4d4d",bg = "#d9b38c",font=20,bd=0)
mutorere_text.insert(INSERT,"Mū tōrere")
mutorere_text.place(x=160,y=50,height=40,width=200)

root.mainloop()