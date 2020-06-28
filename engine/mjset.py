from .tile import Tile, SimpleTile, HonorTile, BonusTile
import numpy as np

class MJSet (object):
	def __init__(self):
		self.tiles = []
		self.simple_suits = ["Man", "Bamboo", "Circle"]
		simple_numbers = np.arange(1,10)
		self.honor_suits_winds = ["East", "South", "West", "North"]
		self.honor_suits_dragons = ["Red", "Green", "White"]
		self.honor_suits = self.honor_suits_winds + self.honor_suits_dragons
		self.bonus_suits = ["Flowers", "Seasons"]
		bonus_numbers = np.arange(1,5)
		
		for _ in range(4):
			for suit in self.simple_suits:
				for num in simple_numbers:
						self.tiles.append(SimpleTile(num, suit))
			for suit in self.honor_suits:
				self.tiles.append(HonorTile(suit))
		
		for suit in self.bonus_suits:
			for num in bonus_numbers:
				self.tiles.append(BonusTile(num, suit))
				
		print("MJ Set Initiated.\n")
		
	def shuffle(self):
		random.shuffle(self.tiles)
		print('The MJ set has been shuffled.')
		
	def draw_tile(self, no_of_tiles=1, clkwise=True):
		drawn_tiles = []
		if clkwise:
			for i in range(no_of_tiles):
				drawn_tiles.append(self.tiles.pop(0))
		else:
			for i in range(no_of_tiles):
				drawn_tiles.append(self.tiles.pop() ) #list.pop() defaults last element
		return drawn_tiles
		
	def prepare_wall_tiles(self, dice_results):
		"""
		dice_results [int]
		"""
		dice_relative_position_value = (dice_results%4 - 1)
		if dice_relative_position_value < 0:
			dice_relative_position_value += 4
		i_position = pile_multiplier * 36 + dice_results * 2 + 1
		self.tiles = self.tiles[i_position:144] + self.tiles[0:i_position]
		

