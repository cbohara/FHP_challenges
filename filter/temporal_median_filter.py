import numpy as np


class TemporalMedianFilter:
	def __init__(self, number_of_previous_scans):
		self.D = number_of_previous_scans
		self.all_input_scans = None

	def update(self, input_scan):
		if self.all_input_scans is None:
			self.all_input_scans = input_scan
			return self.all_input_scans

		self.all_input_scans = np.vstack((self.all_input_scans, input_scan))

		num_matrix_rows = np.shape(self.all_input_scans)[0]
		num_rows_to_include = self.D + 1
		if num_matrix_rows > num_rows_to_include:
			self.all_input_scans = np.delete(self.all_input_scans, 0, 0)

		return np.median(self.all_input_scans, axis=0)
