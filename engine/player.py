from .fancalculator import FanCalculator
from operator import attrgetter

class Player (object):
	def __init__(self, player_id, position, isbot=True):
		"""
		self.id - int between 1 and 4
		self.position indicates the seat of relative to the East position
		int between 1 and 4
		
		
		"""
		self.id = player_id
		self.position = position
		self.hiddentiles = []
		self.showntiles = []
		self.bonustiles = []
		self.adviser = FanCalculator()
		self.cash = 0
		self.maxfan = 0
		self.minfan = 0
		self.isbot = isbot
		self.record = []
		
	def __repr__(self):
		return "Player {} | Position {} | Cash {}".format(self.player_id, self.position, self.cash)
	
	def sort_hand(self):
		self.hiddentiles = sorted(self.hiddentiles, key=attrgetter('suit','number'))
		return self.hiddentiles
		
	def discard_tile(self):
		if isbot:
			pass
		else:
			count = 0
			while count < 3:
				try:
					tile_id = input("Please enter the id of the hidden tiles you would like to remove")
				except:
					print("Please try again")
					count += 3
		
		
	def check_suits_in_hidden_tiles(self, suit_types):
		"""
		The purpose of this function is to return the index of tiles' suits that
		matches suit_types (a list)
		to refine: input can be list or not
		"""
		bonus_tiles_id = []
		for i in range(len(self.hiddentiles)):
			if self.hiddentiles[i].suit in suit_types:
				bonus_tiles_id.append(i)
		return bonus_tiles_id
