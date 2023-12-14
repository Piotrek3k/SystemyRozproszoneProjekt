class GameBoard:
    movecount = 0

    def __init__(self, nodes):
        self.nodes = nodes  # tablica węzłów

    @staticmethod
    def move(node1, node2):
        if node1.is_possible_to_move(node2):
            node2.color = node1.color
            node1.color = 12
            GameBoard.movecount += 1


class Node:
    def __init__(self, index, color):
        # Każdy węzeł ma numer (0 - 8) i kolor
        self.index = index
        self.color = color

    def is_possible_to_move(self, node):
        if self.color in (10, 11) and node.color == 12:  # Pole musi być puste
            if (
                self.index == node.index + 1
                or self.index == node.index - 1
                or self.index == node.index + 7
                or self.index == node.index - 7
                or node.index == 8
                or self.index == 8
            ):  # Pole do którego chcemy przenieść żeton musi sąsiadować z naszym polem
                return True
        return False

    def test(self, nodes, player):
        if self.index == 8:
            return True
        pos1 = self.index - 1
        pos2 = self.index + 1
        if pos1 == -1:
            pos1 = 7
        if pos2 == 8:
            pos2 = 0
        if player == 0 and self.color == 10:
            if nodes[pos1].color == 10 and nodes[pos2].color == 10:
                return False
        elif player == 1 and self.color == 11:
            if nodes[pos1].color == 11 and nodes[pos2].color == 11:
                return False
        return True

       







        
