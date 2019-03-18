import random as rd
import os
from abc import ABC, abstractmethod

from board import Board

class Player(ABC):
    name = ""
    #board = None

    def __init__(self, name):
        self.name = name
        #self.board = Board()

    @abstractmethod
    def put_ships(self, board):
        pass

    @abstractmethod
    def try_hit(self, board):
        pass

    def get_name(self):
        return self.name

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def try_hit(self, board):
        valid = False
        while(valid == False):
            x = rd.randint(0, board.get_rows())
            y = rd.randint(0, board.get_cols())

            valid = board.check_coordinate(x, y, False)
            if valid:
                valid = board.try_hit(x, y, False)

    def put_ships(self, board):
        for ship in board.get_ships():
            valid = False
            while(valid == False):
                x = rd.randint(0, board.get_rows())
                y = rd.randint(0, board.get_cols())
                direction = 'v' if rd.randint(0, 2) == 0 else 'h'

                valid = board.check_coordinate(x, y, False)
                if valid:
                    valid = board.put_ship(ship, x, y, direction, False)

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def try_hit(self, board):
        valid = False
        while(valid == False):
            x = int(input('Coordenada X: '))
            y = int(input('Coordenada Y: '))

            valid = board.check_coordinate(x, y, True)
            if valid:
                valid = board.try_hit(x, y, True)

    def put_ships(self, board):
        for ship in board.get_ships():
            valid = False
            while(valid == False):
                print('Posicione o seu ', ship['ship'])
                x = int(input('Coordenada inicial X: '))
                y = int(input('Coordenada inicial Y: '))
                direction = input('Orientação (v / h): ')

                clear_screen()
                valid = board.check_coordinate(x, y, True)
                if valid:
                    valid = board.put_ship(ship, x, y, direction, True)

        board.display_board(self.get_name())


#Helper
def clear_screen():
    if os.name != "posix":
        os.system("cls")
    else:
        os.system("clear")