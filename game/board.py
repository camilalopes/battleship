import numpy as np

class Board(object):
    __row = 10
    __col = 10
	
    ships = [ 
    {"ship" : "Aircraft", "size" : 5, "position": []},
    {"ship" : "Battleship", "size" : 4, "position": []},
    {"ship" : "Cruiser", "size" : 3, "position": []},
    {"ship" : "Destroyer", "size" : 2, "position": []},
    {"ship" : "Destroyer", "size" : 2, "position": []},
    {"ship" : "Submarine", "size" : 1, "position": []},
    {"ship" : "Submarine", "size" : 2, "position": []}]

    def __init__(self):
        self.board = np.zeros((self.__row,self.__col), dtype=np.int)

    def get_row(self):
        return self.__row
    def get_col(self):
        return self.__col

    def get_ships(self):
        return self.ships

    def put_ship(self, ship,  x, y, dir):
        if dir == 'v':
            direction = {"x": 0, "y": 1}
        else:
            direction = {"x": 1, "y": 0}

        x2 = x
        y2 = y
        for i in range(self.ships[ship].size):
            if not is_valid(x2, y2):
                return False
            x2 += direction.x
            y2 += direction.y

        if self.check_coordinate(x, y):
            while len(self.ships[ship].position) < self.ships[ship].size:
                self.ships[ship].position.append((x, y))
                x += direction.x
                y += direction.y

    def is_valid(self, x, y):
        """ Confere se a coordenada está vazia """
        if (self.board[x][y] != 0): 
            return False
        else:
             return True

    def check_coordinate(self, x, y):
        """ Confere a validade da coordenada """
        if (x >= 0 and x < self.__row) and (y >= 0 and y < self.__col): #coordenada dentro do tabuleiro
            if not self.is_valid(x,y):
                print ('Posição Inválida!')
                return False
            else:
                return True
        else:
            print ('Coordenada inválida!')
            return False
			
    def check_game_over(self):
        if len(ships) == 0:
            return True
        return False

    def mark_coordinate(self, x, y):
        """ Marca a coordenada no tabuleiro """
        if self.board[x][y] == 0:
            print ('Tiro na água!')
            self.board[x][y] == 2
        else:
            if self.board[x][y] == 1:
                print ('Tiro acertou embarcação!')
                self.board[x][y] == 3

    def display_board(self):
        print(end="\t")
        for i in range(10):
            print(i," ", end='')
        print("\n")

        for row in range(self.get_row()):
            for col in range(self.get_col()):
                if col==0:
                    print(row, end='\t')
                print(self.board[row][col], " ", end='')
            print("")
