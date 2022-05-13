class   GameBoard:
    movecount = 0
    def __init__(self,nodes):
        self.nodes = nodes  # tablica węzłów
    def move(node1,node2):
        if(node1.is_possible_to_move(node2)):
            node2.color = node1.color
            node1.color = 12
            
            GameBoard.movecount += 1

class   Node:
    def __init__(self,index,color):
        # Każdy węzeł ma numer (0 - 8) i kolor
        self.index=index
        self.color=color

    def is_possible_to_move(self,node,player):
        if(player == 0 and self.color==10):
            if node.color == 12: # Pole musi być puste
                if self.index == node.index + 1 or self.index == node.index - 1: # Pole do którego chcemy przenieść żeton musi sąsiadować z naszym polem
                    return True
                elif self.index == node.index + 7 or self.index == node.index - 7: # Szczególny przypadek
                    return True
                elif node.index == 8 or self.index == 8:   # Albo być w środku
                    return True
            
        if(player == 1 and self.color==11):
             if node.color == 12: # Pole musi być puste
                if self.index == node.index + 1 or self.index == node.index - 1: # Pole do którego chcemy przenieść żeton musi sąsiadować z naszym polem
                    return True
                elif self.index == node.index + 7 or self.index == node.index - 7: # Szczególny przypadek
                    return True
                elif node.index == 8 or self.index == 8:   # Albo być w środku
                    return True
        return False
       







        
