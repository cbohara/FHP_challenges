import numpy as np

class RangeFilter:
	def __init__(self, range_min_value, range_max_value):
		self.range_min_value = range_min_value
		self.range_max_value = range_max_value

	def update(self, input_scan):
		filtered_scan = []
		for value in input_scan:
			if value < self.range_min_value:
				filtered_scan.append(self.range_min_value)
			elif value > self.range_max_value:
				filtered_scan.append(self.range_max_value)
			else:
				filtered_scan.append(value)
		return np.array(filtered_scan)
