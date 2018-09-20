import numpy as np


class RangeFilter:
	def __init__(self, range_min_value, range_max_value):
		"""
		Initialize RangeFilter object.

		Parameters
		----------
		range_min_value: int
			Minimum value to include in filtered array.
		range_max_value: int
			Maximum value to include in filtered array.
		"""
		self.range_min_value = range_min_value
		self.range_max_value = range_max_value

	def update(self, input_scan):
		"""
		Replace values out of range with boundary values.

		Replace values below range_min_value with range_min_value.
		Replace values above range_max_value with range_max_value.

		Parameters
		----------
		input_scan: numpy array
			Array of float values representing distance measurements.

		Returns
		-------
		numpy array
			Filtered array containing values within desired range.
		"""
		filtered_scan = []
		for value in input_scan:
			if value < self.range_min_value:
				filtered_scan.append(self.range_min_value)
			elif value > self.range_max_value:
				filtered_scan.append(self.range_max_value)
			else:
				filtered_scan.append(value)
		return np.array(filtered_scan)
