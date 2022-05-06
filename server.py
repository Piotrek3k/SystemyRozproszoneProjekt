from concurrent.futures import thread
import socket as sc
from ssl import SOL_SOCKET
import threading
import sys

clients=set()

#wolny port od kubicy, tim robi na 8080 i w sumie w dokumentacji tez tak
PORT = 2223
#kubica dal 1024 ale po cholere tyle, 64 styknie jak u tima, a to ilosc bitow
BUF_SIZE = 64



# narazie lokalny, potem sie najwyzej zmieni
# pobiera z bomby twoje ip, zamiast recznie
SERVER = sc.gethostbyname(sc.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG="UTRACONO POŁĄCZENIE"



#tworzymy socket, AF_INET odpowiada za protokol IPV4, a SOCK_STREAM za streamowanie danych
server=sc.socket(sc.AF_INET,sc.SOCK_STREAM)
server.setsockopt(SOL_SOCKET,sc.SO_REUSEADDR,1)
# ustawiamy serwer, chyba za duzo tych commitow
server.bind(ADDR)



#ogarnia klienta
def handle_client(conn, addr):
    print("Klient dołączył na serwer, jego adres:",addr)
    connected = True
    while connected:
        msg_length = conn.recv(BUF_SIZE).decode(FORMAT) #odbieramy wiadomosc od klienta, z bajtow zmieniamy to w stringa
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # zeby bajty sie zgadzaly
            if msg == DISCONNECT_MSG:
                connected=False 
                conn.send(str.encode("Żegnam"))#wysyla klientowi siema
            print("Klient o adresie:",addr," wysłał wiadomość:",msg)
            for client in clients:
                client.send(str.encode(msg))
            #conn.sendall(str.encode(msg))#wysyla kazdemu wiadomosc
    conn.close() #wyrzucamy klienta z serwera




#listen oczekuje na polaczenie klientow
#accept(nowy klient) zwraca conn(to obiekt jak cos), czyli nowy socket ktory bedzie zwracal i otrzymywal dane,
# addr to adres ktory jest powiazany z socketem
#tworzy sie nowy watek jesli jakis klient dolaczy
def start():
    server.listen(2)#2 maksymalnie
    print("Serwer o adresie: ", SERVER ," wystartował")
    while True:
        conn, addr = server.accept()
        clients.add(conn)
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print("Klienci na serwerze:", threading.activeCount()-1) #-1 bo serwer to tez watek, watki w pythonie to tez chyba procesy, no yebac



start()