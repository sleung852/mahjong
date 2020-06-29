import itertools

from .mjset import MJSet
from .tile import *

class FanCalculator (object):
	def __init__(self):
		self.tiles = []
		self.mjset = MJSet()
		
		self.chow_com = []
		self.pong_com = []
		self.full_com = []
		
	def cal_chow_com(self, hiddentiles=None):
		"""
		Calculate all the possible Chow (aka.Sheung) combinations
		"""
		if hiddentiles is None:
			hiddentiles = self.tiles.copy()

		self.chow_com = []
		unique_tiles = list(set(hiddentiles))
		for unique_tile in unique_tiles:
			if (unique_tile.number <= 7) & (unique_tile.kind == "simple"):
				tile_b = SimpleTile(unique_tile.number + 1, unique_tile.suit)
				tile_c = SimpleTile(unique_tile.number + 2, unique_tile.suit)
				if (tile_b in self.tiles) & (tile_c in self.tiles):
					self.chow_com.append([unique_tile, tile_b, tile_c])
		return self.chow_com
		
	def cal_pong_com(self, hiddentiles=None):
		if hiddentiles is None:
			hiddentiles = self.tiles.copy()

		self.pong_com = []
		unique_tiles = list(set(hiddentiles))
		for unique_tile in unique_tiles:
			if self.tiles.count(unique_tile) == 3:
				self.pong_com.append([unique_tile] * 3)
		return self.pong_com
				
	def all_com(self, hiddentiles=None):
		"""
		return all combinations of Pong and Chow
		"""
		if hiddentiles is None:
			hiddentiles = self.tiles.copy()

		self.cal_pong_com(hiddentiles)
		self.cal_chow_com(hiddentiles)
		self.full_com = self.pong_com + self.chow_com
		return self.full_com

	def legitimate_hands(self, hiddentiles=None, thirteen=True):
		if hiddentiles is None:
			handtiles = self.tiles.copy()
		else:
			handtiles = hiddentiles.copy()

		self.all_com(hiddentiles=handtiles)

		possible_hands = []
		#create all combinations without order
		set_combinations_raw = list(itertools.combinations_with_replacement(self.full_com, 4))
		for set_combination_raw in set_combinations_raw:
		    four_trio_com = []
		    for combination_raw in set_combination_raw:
		    	for tile in combination_raw:
		        	four_trio_com.append(tile)
		    if self.tiles_subset_bool(handtiles, four_trio_com):
		    	leftover = self.tiles_minus(handtiles, four_trio_com)
		    	if leftover[0] == leftover[1]:
		    		possible_hands.append(list(set_combination_raw) + [leftover])
		    		print('good: {}'.format(possible_hands))

		# special hands
		if thirteen:
			raw_tiles = self.tiles.copy()
			if self.is_thirteenorphans():
				return 1, [self.tiles]
		return [len(possible_hands) > 0, possible_hands]

	def legitimate_hands_old2(self, hiddentiles=None, thirteen=True):
		if hiddentiles is None:
			handtiles = self.tiles.copy()
		else:
			handtiles = hiddentiles.copy()
		self.all_com(hiddentiles=handtiles)
		possible_hands = []
		# all normal hands
		for comb_a in self.full_com:
			for comb_b in self.full_com:
				for comb_c in self.full_com:
					for comb_d in self.full_com:
						temp_com = comb_a + comb_b + comb_c + comb_d
						if self.tiles_subset_bool(handtiles, temp_com):
							leftover = self.tiles_minus(handtiles, temp_com)
							if leftover[0] == leftover[1]:
								repeateds = []
								for possible_hand in possible_hands:
									repeated = []
									comb_ax, comb_bx, comb_cx, comb_dx, leftoverx = possible_hand										
									for comb in [comb_a, comb_b, comb_c, comb_d]:
										if comb in [comb_ax, comb_bx, comb_cx, comb_dx]:
											repeated.append(True)
										else:
											repeated.append(False)
									repeateds.append(all(repeated))
									#print([comb_a, comb_b, comb_c, comb_d], repeated)
								if not any(repeateds):
									possible_hands.append([comb_a, comb_b, comb_c, comb_d, leftover])
		# special hands
		if thirteen:
			raw_tiles = self.tiles.copy()
			if self.is_thirteenorphans():
				return 1, [self.tiles]
		return [len(possible_hands) > 0, possible_hands]
		
	def legitimate_hands_old1(self, hiddentiles=None, thirteen=True):
		if hiddentiles is None:
			handtiles = self.tiles.copy()
		else:
			handtiles = hiddentiles.copy()
		self.all_com(hiddentiles=handtiles)
		possible_hands = []
		# all normal hands
		for comb_a in self.full_com:
			if hiddentiles is None:
				raw_tiles = self.tiles.copy()
			else:
				raw_tiles = hiddentiles.copy()
			print('raw tiles: {}'.format(raw_tiles))
			leftover = self.tiles_minus(raw_tiles, comb_a)
			for comb_b in self.full_com:
				if self.tiles_subset_bool(leftover, comb_b):
					leftover = self.tiles_minus(leftover, comb_b)
					for comb_c in self.full_com:
						if self.tiles_subset_bool(leftover, comb_c):
							leftover = self.tiles_minus(leftover, comb_c)
							for comb_d in self.full_com:
								if self.tiles_subset_bool(leftover, comb_d):
									leftover = self.tiles_minus(leftover, comb_d)
									if leftover[0] == leftover[1]:
										repeateds = []
										for possible_hand in possible_hands:
											repeated = []
											comb_ax, comb_bx, comb_cx, comb_dx, leftoverx = possible_hand										
											for comb in [comb_a, comb_b, comb_c, comb_d]:
												if comb in [comb_ax, comb_bx, comb_cx, comb_dx]:
													repeated.append(True)
												else:
													repeated.append(False)
											repeateds.append(all(repeated))
											#print([comb_a, comb_b, comb_c, comb_d], repeated)
										if not any(repeateds):
											possible_hands.append([comb_a, comb_b, comb_c, comb_d, leftover])
		# special hands
		if thirteen:
			raw_tiles = self.tiles.copy()
			if self.is_thirteenorphans():
				return 1, [self.tiles]
		return [len(possible_hands) > 0, possible_hands]
	
	def call_tile_to_win(self, available_tiles):
		valid_options = []
		
		options = list(set(available_tiles))
		for option in options:
			hidden_tiles_copy = self.tiles.copy()
			hidden_tiles_copy.append(option)
			print(hidden_tiles_copy)
			valid_bool, options = self.legitimate_hands(hiddentiles=hidden_tiles_copy)
			if valid_bool:
				valid_options += options
				
		return valid_options
		
	def handtype_fan_calculator(self, hand_comb):
		"""
		return no. of fans of the winning hand
		
		functions still need to write:
			1. is 13 yiu
			2. summary function
			
		#Kind of Interuption of Play#
		Pong - three of the same kind
		Kong - four of the same kind
		Chow - three Simple tiles in sequence of the same Suit
		Eyes - two identical tiles in a winning hand
		
		#Scoring#
		##Type of Hand##
		Common Hand | Ping Wu 1
		All in Triplets | Deoi Deoi Wu 3
		Mixed in One Suit | Wan Jat Sik 3
		All One Suit | Cing Jat Sik 7
		All Honor Tiles | Zi Jat Sik 10
		Small Dragons | Siu Saam Jyun 5
		Great Gragons | Daai Saam Jyun 8
		Small Winds | Siu Sei Hei 10
		Great Winds | Dai Sei Hei 13
		Thirteen Orphans | Sap Saam Jiu 13
		All Kongs | Sap Baat Lo Hon 13
		Self Triplets | Kaan Kaan Wu 13
		Fan Ji Eyes of Orphans 8 fan? (Cedric)
		Orphans | Jiu Gau 10
		Nine Gates | Gau Zi Lin Waan 10
		
		##Winning Conditions##
		### + 1 fan###
		Fan Ji
		Mixed Orphan | Wun Yiu Gao
		Self-Pick | Zhi Mo
		Win from Wall | Mun Cin Cing?
		Robbing Kong | Coeng Gong
		Win by Last Catch | Hoi Dai Lau Jyut
		### +2 fan###
		Win by Kong | Gong Soeng Hoi Faa
		### +9 fan###
		Win by Double Kong | Gong Soeng Gong
		### +max fan###
		Heavenly Hand | Tin Wu
		Earthly Hand | Dei Wu
		"""
		fan = 0
		reasons = []
		# unique_combinations
		if self.is_thirteenorphans():
			reasons.append('Thirteen Orphans | +13')
			fan += 13
			return fan, reasons

		current_hand_summary = self.create_summary(hand_comb)
		
		# unique_combinations
		if self.is_orphan(current_hand_summary, self.tiles):
			reaons.append('Orphans | +10')
			fan += 10
			return fan, reasons
		
		if self.is_commonhand(current_hand_summary):
			reasons.append('Common Hand | +1')
			fan += 1
		elif self.is_allintripplets(current_hand_summary):
			reasons.append('All in Tripplets | +3')
			fan += 3

		if self.is_mixedorphan(current_hand_summary, self.tiles):
			reasons.append('Mixed Orphans | +1')
			fan += 1
		
		if self.is_mixedinonesuit(current_hand_summary):
			reasons.append('Mixed in One Suit | +3')
			fan += 3
		elif self.is_allonesuit(current_hand_summary):
			reasons.append('All One Suit | +7')
			fan += 7
		elif self.is_allhonortiles(current_hand_summary):
			reasons.append('All Honor Tiles | +10')
			fan += 10
			
		if self.is_smalldragon(current_hand_summary):
			reasons.append('Small Dragon | +5')
			fan += 5		
		elif self.is_greatdragon(current_hand_summary):
			reasons.append('Great Dragon | +8')
			fan += 8
		elif self.is_containdragon(hand_comb)[0]:
			for dragon in self.is_containdragon(hand_comb)[1]:
				reasons.append('Dragon - {} | +1'.format(dragon))
				fan += 1
		
		if self.is_smallwinds(current_hand_summary):
			reasons.append('Small Winds | +10')
			fan += 10			
		elif self.is_greatwinds(current_hand_summary):
			reasons.append('Great Winds | + 13')
			fan += 13
			
		return fan, reasons
		
		
	def is_commonhand(self, hand_summary):
		if hand_summary['combination']['chow'] == 4:
			return True
		else:
			return False
	
	def is_allintripplets(self, hand_summary):
		if hand_summary['combination']['pong'] + hand_summary['combination']['kong'] == 4:
			return True
		else:
			return False
			
	def is_mixedinonesuit(self, hand_summary):
		# checking whether any honor tiles exist

		honor_bool = []
		for honor_suit in self.mjset.honor_suits:
			honor_bool.append(hand_summary['suit'][honor_suit]>0)
		honor_bool = any(honor_bool)

		# if so, check whether there are only one kind of simple suit
		zerocount = 0
		for simsuit in self.mjset.simple_suits:
			if hand_summary['suit'][simsuit] == 0:
				zerocount += 1
		if (zerocount == 2) & (honor_bool):
			return True
		else:
			return False

	def is_allonesuit(self, hand_summary):
		#print("Checking All-One-Suit")
		for simplesuit in self.mjset.simple_suits:
			simplecomb_count = hand_summary['suit'][simplesuit]
			if (simplecomb_count == 4) & (hand_summary['eye'] == simplesuit):
				return True
		return False
		
	def is_allhonortiles(self, hand_summary):
		
		# firstly if allhonortiles, it must be all tripplets
		if not self.is_allintripplets(hand_summary):
			return False

		# create a bool for checking whether there are not simplesuits at all
		nosimplesuit_bools = []
		for simplesuit in self.mjset.simple_suits:
			nosimplesuit_bools.append(hand_summary['suit'][simplesuit] == 0)
		nosimplesuit_bool = all(nosimplesuit_bools)

		# cross check there is nosimplesuit and the eye is also an honor_suits
		if nosimplesuit_bool & (hand_summary['eye'] in self.mjset.honor_suits):
			return True
		return False
	
	def is_smalldragon(self, hand_summary):
		for dragon in self.mjset.honor_suits_dragons:
			if (hand_summary['suit'][dragon] == 1) | (hand_summary['eye'] == dragon):
				pass
			else:
				return False
		return True
		
	def is_greatdragon(self, hand_summary):
		return all(hand_summary['suit'][dragon] == 1 for dragon in self.mjset.honor_suits_dragons)
		
	def is_smallwinds(self, hand_summary):
		for wind in self.mjset.honor_suits_winds:
			if (hand_summary['suit'][wind] == 1) | (hand_summary['eye'] == wind):
				pass
			else:
				return False
		return True
		
	def is_greatwinds(self, hand_summary):
		return all(hand_summary['suit'][wind] == 1 for wind in self.mjset.honor_suits_winds)		

	def is_allkongs(self, hand_summary):
		return hand_summary['combination']['kong'] == 4
		
	def is_thirteenorphans(self):
		unique_thirteenorphans = []
		for honor_suit in self.mjset.honor_suits:
			unique_thirteenorphans.append(HonorTile(honor_suit))
		for number, suit in zip(([1]*3 + [9]*3), self.mjset.simple_suits*2):
			unique_thirteenorphans.append(SimpleTile(number, suit))
		
		for tile in unique_thirteenorphans:
			if tile not in self.tiles:
				return False
		return True
		
	def is_mixedorphan(self, hand_summary, thehand):
		if self.is_allintripplets(hand_summary):
			simpletiles = []
			for tile in list(set(thehand)):
				if tile.kind == "Simple":
					simpletiles.append(tile)
			for tile in simpletiles:
				if not ((tile.number == 1) or (tile.number == 9)):
					return False
			return True
		return False
		
	def is_orphan(self, hand_summary, thehand):
		if self.is_allintripplets(hand_summary):
			tiles = thehand
			unique_tiles = list(set(tiles))
			result = True
			for tile in unique_tiles:
				if tile.suit in self.mjset.simple_suits:
					if not((tile.number == 1) or (tile.number == 9)):
						result=False
						break
				else:
					result=False
					break
		return False

	def is_containdragon(self, hand_comb):
		dragon_suits = []
		for i in range(4):
			if hand_comb[i][0].suit in self.mjset.honor_suits_dragons:
				dragon_suits.append(hand_comb[i][0].suit)
		if len(dragon_suits) > 0:
			return True, dragon_suits
		else:
			return False, None

		
	def create_summary(self, legal_combs):
		summary_dict = {}
		summary_dict['suit'] = {}
		summary_dict['combination'] = {}
		
		for suit in self.mjset.simple_suits:
			summary_dict['suit'][suit] = 0
		for suit in self.mjset.honor_suits:
			summary_dict['suit'][suit] = 0
		combs = ['kong', 'pong', 'chow']
		for comb in combs:
			summary_dict['combination'][comb] = 0
		
		#print('Creating Hand Summary')
		#print(legal_combs)
		assert len(legal_combs) == 5, "Something is wrong"
		
		for i in range(0,4):
			if len(legal_combs[i]) == 4:
				summary_dict['combination']['kong'] += 1
			elif self.is_pong(legal_combs[i]):
				summary_dict['combination']['pong'] += 1
			elif self.is_chow(legal_combs[i]):
				summary_dict['combination']['chow'] += 1
			else:
				print("Error")
		
		for i in range(0,4):
			summary_dict['suit'][legal_combs[i][0].suit] += 1
			
		summary_dict['eye'] = legal_combs[4][0].suit
		
		#print(summary_dict)
		return summary_dict

	def is_chow(self, comb):
		for tile_a in comb:
			tile_b = SimpleTile(tile_a.number + 1, tile_a.suit)
			tile_c = SimpleTile(tile_a.number + 2, tile_a.suit)
			if (tile_b in comb) & (tile_c in comb):
				return True
			else:
				return False

	def is_pong(self, comb):
		tile_a, tile_b, tile_c = comb
		return tile_a == tile_b == tile_c

	def is_kong(self, comb):
		pass
		
	@staticmethod
	def next_tile(tile):
		assert tile.kind == "simple", "Wrong Kind"
		return SimpleTile((tile.number+1), tile.suit)
	
	@staticmethod	
	def tiles_minus(tiles_minuend, tiles_subtrahend):
		assert(len(tiles_minuend) > len(tiles_subtrahend)), "len(args) do not make sense: {} is greater than {}".format(len(tiles_minuend), len(tiles_subtrahend))
		print('successfully removing {} from {}'.format(tiles_subtrahend, tiles_minuend))
		for tile_subtrahend in tiles_subtrahend:
			tiles_minuend.remove(tile_subtrahend)
		return tiles_minuend

	def tiles_subset_bool(self, tiles_minuend, tiles_subtrahend, laststage = False):
		print('tried removing {} from {}'.format(tiles_subtrahend, tiles_minuend))
		tiles_minuendx = tiles_minuend.copy()
		tiles_subtrahendx = tiles_subtrahend.copy()
		tiles_bool = []
		for tile in tiles_subtrahend:
			if tile in tiles_minuendx:
				tiles_bool.append(True)
				tiles_minuendx.remove(tile)
			else:
				tiles_bool.append(False)
		if not laststage:
			return all(tiles_bool)
		else:
			tiles_minuend = self.tiles_minus(tiles_minuend, tiles_subtrahend)
			if tiles_minuend[0] == tiles_minuend[1]:
				return all(tiles_bool) * True
			else:
				return False

	
