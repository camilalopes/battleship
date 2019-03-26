# -*- coding: utf-8 -*-
import time
import os

from player import PC1, PC2
from board import Board


class Game(object):
    players = []
    boards = []
    player_turn = 0

    def __init__(self):
        self.players.append(PC1("Giovani"))
        self.players.append(PC2("Camila"))

        self.boards.append(Board())
        self.boards.append(Board())

        self.main()

    def change_player(self):
        self.player_turn = abs(self.player_turn - 1)

    def has_won(self, player, enemy):
	if(self.boards[enemy].check_game_over()):
	    self.cls()
	    print(self.players[player].get_name() + " venceu a partida!")

            print("\n Tabuleiro do(a) " + self.players[player].get_name() + ":\n")
            self.boards[self.player_turn].display_board()

	    print("\n ----------------------------------------------------------------------------------------------------------------- \n")

	    print("\n Tabuleiro do(a) " + self.players[enemy].get_name() + ":\n")
			self.boards[enemy].display_board()

	    return True
	else:
	    return False

    def cls(self):
	if os.name != "posix":
            os.system("cls")
	else:
	    os.system("clear")

	def main(self):
		''' Players put their ships '''
		for _ in self.players:
			self.players[self.player_turn].put_ships(self.boards[self.player_turn])
			time.sleep(1)
			self.cls()
			self.change_player()

		''' The game begins and not finish until a player wins the game '''
		while True:
			enemy = abs(self.player_turn-1)

			self.cls()
			print("\n ==================================================== Vez do(a) " + self.players[self.player_turn].get_name() + " ====================================================  ")
			print("\t. = Desconhecido | o = Tiro na Água | X = Navio Atingido | + = Navio Intacto")

			print("\n Seu Tabuleiro ("+self.players[self.player_turn].get_name()+"):\n")
			self.boards[self.player_turn].display_board()

			print("\n ----------------------------------------------------------------------------------------------------------------- \n")

			print("\n Tabuleiro do Inimigo ("+self.players[enemy].get_name()+"):\n")
			self.boards[enemy].display_enemy_board()
			self.players[self.player_turn].try_hit(self.boards[enemy])

			if(self.has_won(self.player_turn, enemy)):
                            open("results.txt", "a").write(self.players[self.player_turn].get_name() + "\n")
			    break
			time.sleep(5)
			
			self.change_player()

if __name__ == "__main__":
	Game()
