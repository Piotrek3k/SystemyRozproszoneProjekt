from concurrent.futures import thread
import socket as sc
from ssl import SOL_SOCKET
import threading
import sys

#zbior klientow
clients=set()
players=[]

#inicjacja parametrow
PORT = 2223
BUF_SIZE = 1024



#Tworzenie lokalnego serwera
SERVER = sc.gethostbyname(sc.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG="UTRACONO POŁĄCZENIE"



#Socket, AF_INET odpowiada za protokol IPV4, a SOCK_STREAM za streamowanie danych
server=sc.socket(sc.AF_INET,sc.SOCK_STREAM)
server.setsockopt(SOL_SOCKET,sc.SO_REUSEADDR,1)
server.bind(ADDR)



#Zarzadza klientem, pobiera oraz wysyla wiadomosci
def handle_client(conn, addr):
    print("Klient dołączył na serwer, jego adres:",addr)
    msg3=""
    #Pobiera adres oraz wysyla w celu przyporzadkownia gracza
    for obj in players:
        tmp=obj.__getaddr__()[1]
        msg3=msg3+str(tmp)
    for client in clients:
        client.send(str.encode(msg3))
    connected = True
    #Odbiera ruchy gracza
    while connected:
        msg_length = conn.recv(BUF_SIZE).decode(FORMAT) 
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) 
            #Usuwa gracza z serwera jesli kliknie wyjdz
            if msg == DISCONNECT_MSG:
                connected=False 
                clients.remove(conn)
                players.clear()
                break
            print("Klient o adresie:",addr," wysłał wiadomość:",msg)
            for client in clients:
                client.send(str.encode(msg)) 
    conn.close() 




#Funkcja startowa, ktora tworzy osobny watek kazdemu klientowi
def start():
    server.listen(2)#2 maksymalnie
    print("Serwer o adresie: ", SERVER ," wystartował")
    while True:
        conn, addr = server.accept()
        players.append(Player(addr))
        clients.add(conn)
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print("Klienci na serwerze:", threading.activeCount()-1)
        

#Otrzymanie adresu klienta
class    Player:
    def __init__(self, addr):
        self.addr = addr
    def __getaddr__(self):
        return self.addr

start()