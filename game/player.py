import random as rd
from abc import ABC, abstractmethod

from board import Board

class Player(ABC):
    name = ""
    board = None
    
    def __init__(self, name):
        self.name = name
        self.board = Board()

    #@abstractmethod
    def put_ships(self, board):
        pass

    #@abstractmethod
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
            x = rd.randint(0, board.get_rows()-1)
            y = rd.randint(0, board.get_cols()-1)
            valid = board.check_coordinate(x, y)
            if valid:
                valid = board.is_valid_to_shoot(x, y)

    def put_ships(self, board):
        for ship in board.get_ships():
            valid = False
            while(valid == False):       
                x = rd.randint(0, board.get_rows()-1)
                y = rd.randint(0, board.get_cols()-1)
                direction = 'v' if rd.randint(0, 2) == 0 else 'h'
                valid = board.check_coordinate(x, y)
                if valid:
                    valid = board.put_ship(ship, x, y, direction)

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def try_hit(self, board):
        valid = False
        while(valid == False):
            x = int(input('Coordenada X: '))
            y = int(input('Coordenada Y: '))
            valid = board.check_coordinate(x, y)
            if valid:
                valid = board.is_valid_to_shoot(x, y)


    def put_ships(self, board):
        for ship in board.get_ships():
            valid = False
            while(valid == False):
                print('Posicione o seu ', ship['ship'])
                x = int(input('Coordenada inicial X: '))
                y = int(input('Coordenada inicial Y: '))
                direction = input('Orientação (v / h): ')

                valid = board.check_coordinate(x, y)
                if valid:
                    valid = board.put_ship(ship, x, y, direction)
            board.display_board(self.get_name())
