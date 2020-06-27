from .mjset import MJSet
from .tile import *

class FanCalculator (object):
	def __init__(self):
		self.tiles = []
		self.mjset = MJSet()
		
		self.chow_com = []
		self.pong_com = []
		self.full_com = []
		
	def cal_chow_com(self):
		"""
		Calculate all the possible Chow (aka.Sheung) combinations
		"""
		self.chow_com = []
		unique_tiles = list(set(self.tiles))
		for unique_tile in unique_tiles:
			if (unique_tile.number <= 7) & (unique_tile.kind == "simple"):
				tile_b = SimpleTile(unique_tile.number + 1, unique_tile.suit)
				tile_c = SimpleTile(unique_tile.number + 2, unique_tile.suit)
				#tile_b = next_tile(unique_tile)
				#tile_c = next_tile(next_tile(unique_tile))
				if (tile_b in self.tiles) & (tile_c in self.tiles):
					combinations.append([unique_tile, tile_b, tile_c])
		return self.chow_com
		
	def cal_pong_com(self):
		self.pong_com = []
		unique_tiles = list(set(self.tiles))
		for unique_tile in unique_tiles:
			if self.tiles.count(unique_tile) == 3:
				self.pong_com.append([unique_tile] * 3)
		return self.pong_com
				
	def all_com(self):
		"""
		return all combinations of Pong and Chow
		"""
		self.cal_pong_com()
		self.cal_chow_com()
		self.full_com = self.pong_com + self.chow_com
		return self.full_com
		
	def legitimate_hands(self):
		possible_hands = []
		for comb_a in self.full_com:
			raw_tiles = self.tiles.copy()
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
										possible_hands.append([comb_a, comb_b, comb_c, comb_d, leftover])
		return [len(possible_hands) > 0, possible_hands]
	
	def call_tile_to_win(self, available_tiles):
		valid_options = []
		
		options = list(set(available_tiles))
		for option in options:
			hidden_tiles_copy = self.tiles.copy()
			hidden_tiles_copy.append(option)
			if len(self.legitimate_hands()) > 0:
				valid_options.append(option)
				
		return valid_options
		
	def handtype_fan_calculator(self, tiles):
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
		
		current_hand_summary = self.create_summary(tiles)
		fan = 0
		reasons = []
		
		# unique_combinations
		if self.is_thirteenorphans(tiles):
			reasons.append('Thirteen Orphans | +13')
			fan += 13
			return fan, reasons
			
		if self.is_orphan(tiles):
			reaons.append('Orphans | +10')
			fan += 10
			return fan, reasons
		
		if self.is_commonhand(current_hand_summary):
			reasons.append('Common Hand | +1')
			fan += 1
		elif self.is_allintripplets(current_hand_summary):
			reasons.append('All in Tripplets | +3')
			fan += 3
		
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
		honor_bool = any(honor_suit_qt > 0 for honor_suit_qt in summary_dict['suit'][[self.mjset.honor_suits]].values())
		if honor_bool:
			for simsuit in self.mjset.simple_suits:
				simsuit_ex_list = self.mjset.simple_suits.copy()
				simsuit_ex_list.remove(simsuit)
				if (summary_dict['suit'][simsuit] > 0) & all(suit == 0 for suit_value in summary_dict['suit'][suit] for suit in simsuit_ex_list) & simsuit == summary_dict['key']:
					return True
		return False
		
	def is_allonesuit(self, hand_summary):
		for suit in summary_dict['suit'][self.mjset.simple_suits.values()]:
			if (suit == 4) & summary_dict['eye'] == suit:
				return True
		return False
		
	def is_allhonortiles(self, hand_summary):
		return (all(suit_qt == 0 for suit_qt in summary_dict['suit'][self.mjset.simple_suits].values()) & (hand_summary['eyes'] in self.mjset.honor_suits))
	
	def is_smalldragon(self, hand_summary):
		for dragon in self.mjset.honor_suits_dragons:
			if (summary_dict['suit'][dragon] == 1) | (summary_dict['eyes'] == dragon):
				pass
			else:
				return False
		return True
		
	def is_greatdragon(self, hand_summary):
		return all(summary_dict['suit'][dragon] == 1 for dragon in self.mjset.honor_suits_dragons)
		
	def is_smallwinds(self, hand_summary):
		for wind in self.mjset.honor_suits_winds:
			if (summary_dict['suit'][wind] == 1) | (summary_dict['eyes'] == wind):
				pass
			else:
				return False
		return True
		
	def is_greatwinds(self, hand_summary):
		return all(summary_dict['suit'][wind] == 1 for wind in self.mjset.honor_suits_winds)		

	def is_allkongs(self, hand_summary):
		return summary_dict['combindation']['kong'] == 4
		
	def is_thirteenorphans(self, thehand):
		unique_thirteenorphans = []
		for honor_suit in self.mjset.honor_suits:
			unique_thirteenorphans.append(HonorTile(honor_suit))
		for number, suit in zip(([1]*3 + [9]*3), self.mjset.simple_suits*2):
			unique_thirteenorphans.append(SimpleTile(number, suit))
		
		for tile in unique_thirteenorphans:
			if tile not in list(set(thehand)):
				return False
		return True
		
	def is_mixedorphan(self, hand_summary, thehand):
		if self.is_allintripplets(hand_summary):
			tiles = thehand
			unique_tiles = list(set(tiles))
			result = True
			for tile in unique_tiles:
				if tile.suit in self.mjset.simple_suits:
					if not ((tile.number == 1) or (tile.number == 9)):
						result*=False
						break
			return result
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
		
	def create_summary(self, legal_combs):
		summary_dict = {}
		summary_dict['suit'] = {}
		summary_dict['combination'] = {}
		
		for suit in self.mjset.simple_suits:
			summary_dict['suit'][suit] = 0
		for suit in self.mjset.honor_suits:
			summary_dict['suit'][suit] = 0
		for comb in combs:
			summary_dict['combination'][comb] = 0
			
		assert len(legal_hand) != 5, "Something is wrong"
		for i in range(0,4):
			if is_pong(legal_combs[i]):
				summary_dict['combination']['pong'] += 1
			elif is_chow(legal_combs[i]):
				summary_dict['combination']['chow'] += 1
			elif is_kong(legal_combs[i]):
				summary_dict['combination']['kong'] += 1
			else:
				print("Error")
		
			for i in range(0,4):
				summary_dict['suit'][legal_combs[i][0].suit] += 1
			
		summary_dict['eye'] = legal_hand[4][0].suit
			
		return summary_dict
		
	@staticmethod
	def next_tile(tile):
		assert tile.kind == "simple", "Wrong Kind"
		return SimpleTile((tile.number+1), tile.suit)
	
	@staticmethod	
	def tiles_minus(tiles_minuend, tiles_subtrahend):
		assert(len(tiles_minuend) > len(tiles_subtrahend)), "len(args) do not make sense: {} is greater than {}".format(len(tiles_minuend), len(tiles_subtrahend))
		for tile_subtrahend in tiles_subtrahend:
			tiles_minuend.remove(tile_subtrahend)
		return tiles_minuend
	
	@staticmethod
	def tiles_subset_bool(tiles1, tiles2):
		"""
		Return Boolean
		Check whether tiles2 exist within tiles1
		"""
		pong_boolean = True
		tiles2_a = tiles2[0]
		for tile in tiles2:
			if tiles2_a != tile:
				pong_boolean = False
		if pong_boolean:
			ok_bool = True
			tiles1_copy = tiles1.copy()
			for tile in tiles2:
				if tile in tiles1_copy:
					tiles1_copy.remove(tile)
				else:
					ok_bool*=False
		else:
			ok_bool = all([tile2 in tiles2 for tile2 in tiles2])
		return ok_bool	
	
