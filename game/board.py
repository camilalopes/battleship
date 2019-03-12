
import numpy as np

class Board(object):
    __row = 10
    __col = 10

    def __init__(self):
        self.board = np.zeros((self.__row,self.__col), dtype=np.int)
