class   GameBoard:
    movecount = 0
    def __init__(self,nodes):
        self.nodes = nodes  # tablica węzłów
    def move(node1,node2):
        if(node1.is_possible_to_move(node2)):
            node2.color = node1.color
            node1.color = 0

            GameBoard.movecount += 1
    def get_move_count(self):
        return GameBoard.movecount
    def play(self):
        if GameBoard.movecount >= 200:
            return ("Game over")
        if GameBoard.movecount % 2 == 0:
            return
            # Ruch czarnego
        else:
            return
            # Ruch białego
# Zajebałem sie pisząc te funkcje wyżej, chyba najłatwiej będzie to zrobić po zrobieniu gui
# W gui też byśmy zrobili jakąś formę weryfikacji czy ten żeton można ruszyć
# Albo nie wiem inaczej to 
# No generalnie to propozycja tylko 

class   Node:
    def __init__(self,index,color,button):
        # Każdy węzeł ma numer (0 - 8) i kolor
        self.index=index
        self.color=color
        self.button=button

    def is_possible_to_move(self,node):
        if node.color == 0: # Pole musi być puste
            if self.index == node.index + 1 or self.index == node.index - 1: # Pole do którego chcemy przenieść żeton musi sąsiadować z naszym polem
                return True
            elif self.index == node.index + 7 or self.index == node.index - 7: # Szczególny przypadek
                return True
            elif node.index == 8 or self.index == 8:   # Albo być w środku
                return True
        return False
    # def change_color(self):
    #     if self.color == 1 or self.color == 2:
    #         self.color=0
    #         button=Button(turtle_window,bd=0, bg='#d9b38c',borderwidth=0)
    #     else
       







        
