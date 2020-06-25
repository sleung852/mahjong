import random

class Dices (object):
	def __init__(self):
		self.total = 0
	
	def __repr__(self):
		if self.total == 0:
			return "The dices have not yet been rolled."
		else:
			return self.total
		
	def roll(self):
		self.total = random.randint(1,7) + random.randint(1,7) + random.randint(1,7)
		print("Dices rolled. The sum is {}".format(self.total))
		return self.total
