from abc import ABC, abstractmethod
import random as rd

class Player(ABC):
    def __init__(self, nome):
        self.nome = nome

    #@abstractmethod
    def put_ships(board):
        pass

    #@abstractmethod
    def try_hit(board):
        pass

class Computer(Player):
    def __init__(self, nome):
        super().__init__(nome)

    def try_hit(board):
        valida = false
        while(valida == false):
            x = rd.randint(0, board.get_row)
            y = rd.randint(0, board.get_col)
            valida = board.check_coordinate(x, y)

        board.mark_coordinate(x, y)


class Human(Player):
    def __init__(self, nome):
        super().__init__(nome)

    def try_hit(board):
        valida = false
        while(valida == false):
            x = input('Coordenada X: ')
            y = input('Coordenada Y: ')
            valida = check_coordinate(x, y)

        board.mark_coordinate(x, y)
