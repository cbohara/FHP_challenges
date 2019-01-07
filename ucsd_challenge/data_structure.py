import random

class DataStructure:
	def __init__(self, values=None):
		if values is None:
			self.values = []
		else:
			self.values = values

	def __str__(self):
		str_values = [str(x) for x in self.values]
		return ','.join(str_values)

	def insert(self, value):
		self.values.append(value)

	def remove(self, value):
		self.values = [x for x in self.values if x != value]

	def get_random(self):
		sorted_list = sorted(self.values)
		min_value = sorted_list[0]
		max_value = sorted_list[-1]
		return random.randint(min_value, max_value)
