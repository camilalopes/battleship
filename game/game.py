from player import Human, Computer
from board import Board
import time

class Game(object):
	players = []
	boards = []
	player_turn = 0

	def __init__(self):
		self.players.append(Human("Jogador 1"))
		self.players.append(Computer("PC"))

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

	def main(self):
		''' Players put their ships '''
		for _ in self.players:
			self.players[self.player_turn].put_ships(self.boards[self.player_turn])
			print(self.player_turn, "\n", self.boards[self.player_turn].board)
			self.change_player()

		''' The game begins and not finish until a player win '''
		while(1):
			enemy = abs(self.player_turn-1)

			self.boards[enemy].display_enemy_board(self.players[enemy].get_name())
			#print(self.player_turn, "\n", self.boards[self.player_turn].board)
			self.players[self.player_turn].try_hit(self.boards[enemy])

			if (self.has_won(self.player_turn, enemy)):
				break

			time.sleep(5)
			self.change_player()

		'''
		while self.have_winner == False:
			player_name = self.players[self.player_turn].get_name()
			if player_name == "Jogador 1":
				self.boards[self.player_turn].display_board(player_name)
				self.boards[abs(self.player_turn-1)].display_enemy_board(player_name)

			self.players[self.player_turn].try_hit(self.boards[self.player_turn])
			self.change_player()
		'''

if __name__=="__main__":
	Game()
