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
    def put_ships(self):
        pass

    #@abstractmethod
    def try_hit(self):
        pass

    def get_name(self):
        return self.name

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def try_hit(self):
        valid = False
        while(valid == False):
            x = rd.randint(0, self.board.get_rows()-1)
            y = rd.randint(0, self.board.get_cols()-1)
            valid = self.board.check_coordinate(x, y)
            if valid:
                valid = self.board.is_valid_to_shoot(x, y)

    def put_ships(self):
        for ship in self.board.get_ships():
            valid = False
            while(valid == False):       
                x = rd.randint(0, self.board.get_rows()-1)
                y = rd.randint(0, self.board.get_cols()-1)
                direction = 'v' if rd.randint(0, 2) == 0 else 'h'
                valid = self.board.check_coordinate(x, y)
                if valid:
                    valid, self.board = self.board.put_ship(ship, x, y, direction)
        return self.board

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def try_hit(self):
        valid = False
        while(valid == False):
            x = int(input('Coordenada X: '))
            y = int(input('Coordenada Y: '))
            valid = self.board.check_coordinate(x, y)
            if valid:
                valid = self.board.is_valid_to_shoot(x, y)


    def put_ships(self):
        for ship in self.board.get_ships():
            valid = False
            while(valid == False):
                print('Posicione o seu ', ship['ship'])
                x = int(input('Coordenada inicial X: '))
                y = int(input('Coordenada inicial Y: '))
                direction = input('Orientação (v / h): ')

                valid = self.board.check_coordinate(x, y)
                if valid:
                    valid, self.board = self.board.put_ship(ship, x, y, direction)
            self.board.display_board(self.get_name())
        return self.board
