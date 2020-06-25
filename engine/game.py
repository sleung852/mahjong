from .mjset import MJSet
from .dices import Dices

class Game (object):
	"""
	Hand, Round & Match is the hierarchy of a MJ Game
	Usually one Match has four Rounds and each Round has four Hands.
	
	Flow of a Hand of a MJ Game
	(1) Shuffle a set of honor tiles: East, South, West, North #
	(2) Roll a dice to see how sits in which position #set Player's position
	(3) position 1 player roll dice again
	(4) setup the draw_tiles 
	(5) reset positions again
	(6) drawing tiles (with player position 1 drew 2 tiles at the end)
	(7) replace Flowers starting from players position 1
	(8) player position 1 dispose 1 tile
	(9) starting from here, all players draw 1 tile and dispose 1 tile
	(9a) until there is an interuption of play
	(10) until one player wins or no tiles left from the draw_tiles
	"""
	def __init__(self):
		self.firsthand = True
		self.draw_tiles = MJSet()
		self.exposed_tiles = [] #rename to disposed_tiles please
		self.players = []
		self.dices = Dices()
		
		for i in range(1,5):
			self.players.append(Player(i, i))
			
	def roll_dice_to_set_seating_order(self):
		"""
		(1) Shuffle a set of honor tiles: East, South, West, North #
		(2) Roll a dice to see how sits in which position #set Player's position
		"""
		position_list = list(np.arange(1,5))
		random.shuffle(position_list) # 1 denotes East etc.
		dice_result = self.dices.roll()
		for i in range(4):
			self.players[i].position = position_list[i]
			
	def sort_players_by_position(self):
		self.players = sorted(self.players, key=lambda x: x.position)
		
	def hand_setup(self):
		"""
		hand_setup function is to setup all the tiles for each player in
		in order to kick start a Hand.
		"""
		self.dices.roll()
		if self.firsthand:
			#need to reset position based on the dice results only on first hand
			relative_pos_val = self.dices.total % 4
			if relative_pos_val == 0:
				relative_pos_val += 4
			positions = np.append(np.arange(relative_pos_val,5),np.arange(1,relative_pos_val))
			for player, position in zip(self.players, positions):
				player.position = position
			self.sort_players_by_position()
			self.firsthand = False

		# the set of MJ should be started to be distributed to player in pos 1
		self.draw_tiles.prepare_wall_tiles(self.dices.total)
		for _ in range(3):
			for player in self.players:
				player.hiddentiles += self.draw_tiles.draw_tile(4)
		for player in self.players:
			player.hiddentiles += self.draw_tiles.draw_tile(1)
		self.players[0].hiddentiles += self.draw_tiles.draw_tile(1)
		
		#now its time to replace Flowers
		bonus_tiles_counter = 0 #how many players have bonus tiles
		bonus_tiles_bool = True
		while bonus_tiles_bool:
			for player in self.players:
				bonus_tiles_ids = player.check_suits_in_hidden_tiles(self.draw_tiles.bonus_suits)
				bonus_tiles = []
				for ind in bonus_tiles_ids:
					bonus_tiles.append(player.hiddentiles[ind])
				for bonus_tile in bonus_tiles:
					player.bonustiles.append(bonus_tile)
					player.hiddentiles.remove(bonus_tile)
				player.hiddentiles += self.draw_tiles.draw_tile(len(bonus_tiles),clkwise=False)
				if len(player.check_suits_in_hidden_tiles(self.draw_tiles.bonus_suits)) > 0:
					bonus_tiles_counter += 1
			if bonus_tiles_counter == 0:
				bonus_tiles_bool = False
				
		print("The MJ Hand is ready.")
		
		def hand_start(self):
			for player in self.players:
				if player.advisor.legitimate_hand(player.hidden_tiles)[0]:
					print("Player {} has a legitimate_hand".format(player.id))
				else:
					player.discard_tile()
