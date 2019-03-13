
import numpy as np

class Board(object):
    __row = 10
    __col = 10

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
                return false
            else:
                return true
        else:
            print ('Coordenada inválida!')
            return false

    def mark_coordinate(self, x, y):
        """ Marca a coordenada no tabuleiro """
        if self.board[x][y] == 0:
            print ('Tiro na água!')
            self.board[x][y] == 2
        else:
            if self.board[x][y] == 1:
                print ('Tiro acertou embarcação!')
                self.board[x][y] == 3
