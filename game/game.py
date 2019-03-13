from . import player
from . import board

class Game(object):

	def __init__(self):
		player_turn = 0
		players = []
		players.append(Computer())
		players.append(Human())
		
		boards = []
		boards.append(Board())
		boards.append(Board())
		
		main()
		
	def change_player(self):
		self.player_turn = abs(self.player_turn - 1)
		
	def main(self):
		for _ in players:
			players[player_turn].put_ships(boards[player_turn])
			change_player()
		
		while have_winner == False:
			players[player_turn].try_hit(boards[player_turn])
			change_player()