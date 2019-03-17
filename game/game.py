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

	def have_winner(self):
		if self.boards[0].check_game_over():
			print(self.players[1].get_name() + " venceu a partida!")
		else:
			print(self.players[0].get_name() + " venceu a partida!")
		
	def main(self):
		for _ in self.players:
			self.players[self.player_turn].put_ships(self.boards[self.player_turn])
			self.change_player()
			print("A\n", self.boards[self.player_turn].board)
		
		while self.have_winner == False:
			player_name = self.players[self.player_turn].get_name()
			if player_name == "Jogador 1":
				self.boards[self.player_turn].display_board(player_name)
				self.boards[abs(self.player_turn-1)].display_enemy_board(player_name)

			self.players[self.player_turn].try_hit(self.boards[self.player_turn])
			self.change_player()	

if __name__=="__main__":
	Game()