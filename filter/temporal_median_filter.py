import numpy as np


class TemporalMedianFilter:
	def __init__(self, number_of_previous_scans):
		"""
		Initialize TemporalMedianFilter object.

		Parameters
		----------
		number_of_previous_scans: int
			Number of previous input scans to include for median calculation.
		"""
		self.D = number_of_previous_scans
		self.input_scans = None

	def update(self, input_scan):
		"""
		Determine the median of the current and the previous scans.

		The median is calculated for each element in the array.
		The TemporalMedianFilter object previous D scans parameter
		determines how many previous input scans to include when
		calculating the median of each element.

		Parameters
		----------
		input_scan: numpy array
			Single array of float values representing distance measurements.

		Returns
		-------
		numpy array
			Filtered array containing median value of each element from previous D scans.
		"""
		if self.input_scans is None:
			self.input_scans = input_scan
			return self.input_scans

		self.input_scans = np.vstack((self.input_scans, input_scan))

		num_matrix_rows = np.shape(self.input_scans)[0]
		num_rows_to_include = self.D + 1
		if num_matrix_rows > num_rows_to_include:
			self.input_scans = np.delete(self.input_scans, 0, 0)

		return np.median(self.input_scans, axis=0)
