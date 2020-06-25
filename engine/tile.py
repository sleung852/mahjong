class Tile (object):
	def __init__(self, kind, number, suit):
		self.kind = kind
		self.suit = suit
		self.number = number
		
	def __repr__(self):
		return (str(self.number) + self.suit)
		
	def __eq__(self,other):
		return (self.suit == other.suit) & (self.number == other.number)
		
	def __ne__(self,other):
		return (self.suit != other.suit) | (self.number != other.number)
	

class SimpleTile (Tile):
	def __init__(self, number, suit):
		super().__init__('simple', number, suit)
		#self.kind = 'simple'
		
	def next_tile(self, int_input):
		assert (int_input < 3 & int_input > 0), "Incorrect Input"
		pass
		
	@classmethod
	def create_from_str(cls, tilestr):
		assert len(tilestr) <= 2, "Incorrect Format"
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
		super().__init__(suit)
		self.kind = 'honor'
		self.number = 0
		
	def __repr__(self):
		return self.suit
		
class BonusTile (Tile):
	"""
	These are tiles like Flowers and Seasons
	"""
	def __init__(self, kind, number, suit):
		super().__init__(number, suit)
		self.kind = 'bonus'
