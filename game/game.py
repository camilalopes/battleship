import time
import os

from player import Human, Computer
from board import Board

class Game(object):
	players = []
	boards = []
	player_turn = 0

	def __init__(self):
		self.players.append(Computer("PC"))
		self.players.append(Human("Jogador 1"))

		self.boards.append(Board())
		self.boards.append(Board())

		self.main()

	def change_player(self):
		self.player_turn = abs(self.player_turn - 1)

	def has_won(self, player, enemy):
		if(self.boards[enemy].check_game_over()):
			print(self.players[player].get_name() + " venceu a partida!")
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
			time.sleep(3)
			self.cls()
			self.change_player()

		''' The game begins and not finish until a player wins the game '''
		
		while True:
			enemy = abs(self.player_turn-1)

			self.cls()
			self.boards[enemy].display_enemy_board(self.players[self.player_turn].get_name())
			self.players[self.player_turn].try_hit(self.boards[enemy])

			if(self.has_won(self.player_turn, enemy)):
				break
			time.sleep(1)
			self.change_player()

if __name__=="__main__":
	Game()
