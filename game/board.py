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

    def get_rows(self):
        return int(self.__row)
    def get_cols(self):
        return int(self.__col)

    def get_ships(self):
        return self.ships

    def find_ship(self, ship):
        for i in range(len(self.ships)):
            if self.ships[i] == ship:
                return i
        return 0

    def put_ship(self, ship, x, y, dir):
        if dir == 'v':
            direction = {"x": 0, "y": 1}
        else:
            direction = {"x": 1, "y": 0}

        x2 = x
        y2 = y

        i = self.find_ship(ship)
        for _ in range(self.ships[i]["size"]):
            if self.check_coordinate(x2, y2):
                if not self.is_valid_to_put(x2, y2):
                    return False, self
                x2 += direction["x"]
                y2 += direction["y"]
            else:
                return False, self

        if self.check_coordinate(x, y):
            while len(self.ships[i]["position"]) < self.ships[i]["size"]:
                self.ships[i]["position"].append((x, y))
                self.board[x][y] = 1
                x += direction["x"]
                y += direction["y"]
            return True, self

    def is_valid_to_put(self, x, y):
        """ Confere se a coordenada está vazia """
        if (self.board[x][y] != 0): 
            print ('Posição Inválida!')
            return False
        else:
             return True

    def is_valid_to_shoot(self, x, y):
        """ Confere se a coordenada pode receber tiro """
        if (self.board[x][y] == 0 or self.board[x][y] == 1): 
            return True
        else:
            print ('Posição Inválida!')
            return False

    def check_coordinate(self, x, y):
        """ Confere a validade da coordenada """
        if (x >= 0 and x < self.__row) and (y >= 0 and y < self.__col): #coordenada dentro do tabuleiro
            return True
        else:
            print ('Coordenada inválida!')
            return False
			
    def check_game_over(self):
        return len(self.ships) == 0
            
    def mark_coordinate(self, x, y):
        """ Marca a coordenada no tabuleiro """
        if self.board[x][y] == 0:
            print ('Tiro na água!')
            self.board[x][y] == 2
        else:
            if self.board[x][y] == 1:
                print ('Tiro acertou embarcação!')
                self.board[x][y] == 3

    def display_board(self, name):
        print("\n ======================== Tabuleiro do " + name + " =============================== \n" ,
            "0 = Nao jogado | 2 = Tiro na agua | 3 = Navio atingido",end="\n\n\t")
        for i in range(10):
            print(i," ", end='')
        print("\n")

        for row in range(self.get_rows()):
            for col in range(self.get_cols()):
                if col==0:
                    print(row, end='\t')
                print(self.board[row][col], " ", end='')
            print("")

    def display_enemy_board(self, name):
        print("\n ======================== Tabuleiro do " + name + " =============================== \n" ,
            "0 = Nao jogado | 2 = Tiro na agua | 3 = Navio atingido",end="\n\n\t")
        for i in range(10):
            print(i," ", end='')
        print("\n")

        for row in range(self.get_rows()):
            for col in range(self.get_cols()):
                if col==0:
                    print(row, end='\t')
                if self.board[row][col] != 1:
                    print(self.board[row][col], " ", end='')
                else:
                    print(0, " ", end='')

            print("")

    