class Tile (object):
	def __init__(self, kind, number, suit):
		self.kind = kind
		self.suit = suit
		self.number = number
		
	def __repr__(self):
		return (str(self.number) + self.suit)
		
	def __eq__(self, other):
		return (self.suit == other.suit) & (self.number == other.number)
		
	def __ne__(self,other):
		return (self.suit != other.suit) | (self.number != other.number)

	def __hash__(self):
		return hash(str(self))
	
class SimpleTile (Tile):
	def __init__(self, number, suit):
		super().__init__('simple', number, suit)
		#self.kind = 'simple'
		
	def next_tile(self, int_input):
		assert (int_input < 3 & int_input > 0), "Incorrect Input"
		
		
	@classmethod
	def from_str(cls, tilestr):
		assert len(tilestr) == 2, "Incorrect Format"
		char_to_str_suit = {
			'm': "Man",
			'c': "Circle",
			'b': "Bamboo"
		}
		number = tilestr[0]
		suitchar = tilestr[1].lower()
		return cls('Simple', number, char_to_str_suit[suitchar])
	
class HonorTile (Tile):
	"""
	These are tiles like Winds (ie. East, South...)
	and Dragons (Red aka. Red Middle, Green aka. Fortune...)
	"""
	def __init__(self, suit):
		super().__init__('honor', 0, suit)
		
	def __repr__(self):
		return self.suit

	@classmethod
	def from_str(cls, tilestr):
		assert (len(tilestr) == 1) | (len(tilestr) == 2), "Incorrect Format: Wrong Input Format"
		suitchar = tilestr.lower()

		char_to_str_suit = {
			'g': "Green",
			'r': "Red",
			'wh': "White",
			'e': "East",
			's': "South",
			'we': "West",
			'n': "North"
		}
		assert suitchar in char_to_str_suit.keys(), "Incorrect Format: Wrong Input Format"
		return cls(char_to_str_suit[suitchar])
		
class BonusTile (Tile):
	"""
	These are tiles like Flowers and Seasons
	"""
	def __init__(self, number, suit):
		super().__init__('bonus', number, suit)
