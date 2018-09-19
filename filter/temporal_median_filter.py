import numpy as np


class TemporalMedianFilter:
	def __init__(self, number_of_previous_scans):
		self.D = number_of_previous_scans
		self.input_scans = None

	def update(self, input_scan):
		if self.input_scans is None:
			self.input_scans = input_scan
			return self.input_scans

		self.input_scans = np.vstack((self.input_scans, input_scan))

		num_matrix_rows = np.shape(self.input_scans)[0]
		num_rows_to_include = self.D + 1
		if num_matrix_rows > num_rows_to_include:
			self.input_scans = np.delete(self.input_scans, 0, 0)

		return np.median(self.input_scans, axis=0)
