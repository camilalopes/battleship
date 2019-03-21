import random as rd
import os
from abc import ABC, abstractmethod

from board import Board

class Player(ABC):
    name = ""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def put_ships(self, board):
        pass

    @abstractmethod
    def try_hit(self, board):
        pass

    def get_name(self):
        return self.name


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


class Computer(Player):

    def __init__(self, name):
        super().__init__(name)

    @abstractmethod
    def try_hit(self, board):
        pass

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


class PC1(Computer):
    directions = [
        {"x": 0, "y": 1},
        {"x": 0, "y": -1},
        {"x": 1, "y": 0},
        {"x": -1, "y": 0}]

    def __init__(self, name):
        super().__init__(name)
        self.last_try = {"x": 0, "y": 0}
        self.last_direction = {"x": 0, "y": 1}
        self.hit_last_2 = [0, 0]
        self.last_feedback = 0

    def try_hit(self, board):
        valid = False

        while(valid == False):
            x = 0
            y = 0

            #Se o último tiro acertou um navio
            if self.hit_last_2[1] == 3:
                for _ in range(6):
                    x = self.last_try["x"] + self.last_direction["x"]
                    y = self.last_try["y"] + self.last_direction["y"]
                    if (board.is_valid_to_shoot(x, y, False)):
                        break

            #Se o último tiro acertou a água e o penúltimo acertou um navio
            elif self.hit_last_2[0] == 3 and self.hit_last_2[1] == 2:
                for _ in range(6):
                    x = self.last_try["x"] - self.last_direction["x"]
                    y = self.last_try["y"] - self.last_direction["y"]
                    if (board.is_valid_to_shoot(x, y, False)):
                        break

            #Nenhuma jogada válida foi encontrada
            if board.is_valid_to_shoot(x, y, False) == False:
                x = rd.randint(0, board.get_rows())
                y = rd.randint(0, board.get_cols())

            valid = board.check_coordinate(x, y, False)
            if valid:
                self.last_feedback = board.try_hit(x, y, False)
                valid = self.last_feedback != -1
                if valid:
                    self.hit_last_2[0] = self.hit_last_2[1]
                    self.hit_last_2[1] = self.last_feedback
                    self.last_try["x"] = x
                    self.last_try["y"] = y

    def put_ships(self, board):
        super().put_ships(board)

class PC2(Computer):
    directions = [
        {"x": 0, "y": 1},
        {"x": 0, "y": -1},
        {"x": 1, "y": 0},
        {"x": -1, "y": 0}]

    def __init__(self, name):
        super().__init__(name)
        self.last_try = {"x": 0, "y": 0}
        self.first_hit = {"x": 0, "y": 0}
        self.last_direction = {"x": 0, "y": 1}
        self.last_feedback = 0
        self.x2 = 0
        self.y2 = 0

    def try_hit(self, board):
        valid = False
        board2 = board.get_enemy_board()

        while(valid == False):
            x = 0
            y = 0
        
            x = self.last_try["x"]
            y = self.last_try["y"]

            if board2[x][y] == 3:
                inc = 1
                while board.check_coordinate(x, y+inc, False) and board2[x][y+inc] != 2:
                    inc = inc + 1
                    valid = self.try_(x, y+inc, board)
                    if valid: break
                    
                inc = 1
                while board.check_coordinate(x+inc, y, False) and board2[x+inc][y] != 2:
                    inc = inc + 1
                    valid = self.try_(x+inc, y, board)
                    if valid: break
                    
                inc = 1
                while board.check_coordinate(x-inc, y, False) and board2[x-inc][y] != 2:
                    inc = inc + 1
                    valid = self.try_(x-inc, y, board)
                    if valid: break
                    
                inc = 1
                while board.check_coordinate(x, y-inc, False) and board2[x][y-inc] != 2:
                    inc = inc + 1
                    valid = self.try_(x, y-inc, board)
                    if valid: break
                    
                  
            if board2[x][y] == 2:
                inc = 1
                while board.check_coordinate(x, y+inc, False) and board2[x][y+inc] == 3:
                    inc = inc + 1
                    valid = self.try_(x, y+inc, board)
                    if valid: break
                    
                inc = 1
                while board.check_coordinate(x+inc, y, False) and board2[x+inc][y] == 3:
                    inc = inc + 1
                    valid = self.try_(x+inc, y, board)
                    if valid: break
                    
                inc = 1
                while board.check_coordinate(x-inc, y, False) and board2[x-inc][y] == 3:
                    inc = inc + 1
                    valid = self.try_(x-inc, y, board) 
                    if valid: break           

                inc = 1
                while board.check_coordinate(x, y-inc, False) and board2[x][y-inc] == 3:
                    inc = inc + 1
                    valid = self.try_(x, y-inc, board)
                    if valid: break
                    
            for x in range(board.get_rows()):
                for y in range(board.get_cols()):
                    if board2[x][y] == 3:
                        if board2[x][y+1] == 0:
                            self.try_(x, y+1, board)
                        if board2[x][y-1] == 0:
                            self.try_(x, y-1, board)
                        if board2[x+1][y] == 0:
                            self.try_(x+1, y, board)
                        if board2[x-1][y] == 0:
                            self.try_(x-1, y, board)

            x = rd.randint(0, board.get_rows())
            y = rd.randint(0, board.get_cols())

            valid = board.check_coordinate(self.x2, self.y2, False)
            if valid:
                self.last_feedback = board.try_hit(self.x2, self.y2, False)
                valid = self.last_feedback != -1
                if valid:
                    self.last_try["x"] = self.x2
                    self.last_try["y"] = self.y2


    def put_ships(self, board):
        super().put_ships(board)

    def try_(self, x, y, board):
        if board.is_valid_to_shoot(x, y, False):
            self.x = x
            self.y = y
        return board.is_valid_to_shoot(x, y, False)


#Helper
def clear_screen():
    if os.name != "posix":
        os.system("cls")
    else:
        os.system("clear")
