import socket as sc



PORT = 2223
BUF_SIZE = 64
SERVER = sc.gethostbyname(sc.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG="UTRACONO POŁĄCZENIE"



client=sc.socket(sc.AF_INET,sc.SOCK_STREAM)
#laczymy sie z serwerem
client.connect(ADDR)

def send(msg):
    new_msg = msg.encode(FORMAT) #string -->bajty
    msg_length=len(new_msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (BUF_SIZE - len(send_length)) #3ba dodac blanki zeby bylo 64
    client.send(send_length)
    client.send(new_msg)#troche dzike 


send("Jest Wysoko")
send(DISCONNECT_MSG)


#Dobra chyba działa, ogolnie kazdy z graczy odpala skrypt client.py i potem cyk laczysz
#sie, teraz musimy zrobic logike mutorere potem wydaje mi sie ze najprosciej bedzie
# wysylac wiadomosci w 123 itd gdzie ruch idzie, a serwer wysyla do klientow wiadomosc
#zeby gui sie zmienilo, ew klient wysyla do klienta wiadomosc no nw co bedzie prostsze 
#i lepsze, i tak to tyle gorzej bedzie tylko polaczyc to wszystko w calosc