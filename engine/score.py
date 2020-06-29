class ScoringSystem (object):
	def __init__(self, max_fan, max_value, min_fan=3):
		self.max_fan = max_fan
		self.min_fan = min_fan
		self.max_value = max_value
		self.scoresys = {}

		for fan in range(max_fan + 1, min_fan,  -1):
			pass