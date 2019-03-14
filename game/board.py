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

    def is_valid(self, x, y):
        if (self.board[x][y] == 2) or (self.board[x][y] == 3): #jogada já foi efetuada antes
            return False
        else:
             return True

    def check_coordinate(self, x, y):
        """ Confere a validade da coordenada """
        if (x >= 0 and x < self.__row) and (y >= 0 and y < self.__col): #coordenada dentro do tabuleiro
            if not self.is_valid(x,y):
                print ('Jogada repetida!')
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
