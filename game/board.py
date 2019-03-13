import numpy as np

class Board(object):
    __row = 10
    __col = 10
	
	ships = [ 
	{"ship" : "Aircraft", "size" : 5, "quantity": 1},
	{"ship" : "Battleship", "size" : 4, "quantity": 1},
	{"ship" : "Cruiser", "size" : 3, "quantity": 1},
	{"ship" : "Destroyer", "size" : 2, "quantity": 2},
	{"ship" : "Submarine", "size" : 1, "quantity": 2}]
	

    def __init__(self):
        self.board = np.zeros((self.__row,self.__col), dtype=np.int)

    def get_row(self):
        return self.__row
    def get_col(self):
        return self.__col

    def check_coordinate(self, x, y):
        """ Confere a validade da coordenada """
        if (x >= 0 and x < self.__row) and (y >= 0 and y < self.__col): #coordenada dentro do tabuleiro
            if (self.board[x][y] == 2) or (self.board[x][y] == 3): #jogada já foi efetuada antes
                print ('Jogada repetida!')
                return False
            else:
                return True
        else:
            print ('Coordenada inválida!')
            return False
			
	def check_end_game(self):
		if len(ships) == 0
			return True
		
		for row in range(__row)
			for col in range(__col)
				if check_coordinate(row, col):
					return False
		
		return True

    def mark_coordinate(self, x, y):
        """ Marca a coordenada no tabuleiro """
        if self.board[x][y] == 0:
            print ('Tiro na água!')
            self.board[x][y] == 2
        else:
            if self.board[x][y] == 1:
                print ('Tiro acertou embarcação!')
                self.board[x][y] == 3
