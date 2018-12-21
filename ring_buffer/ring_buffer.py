from collections import deque


class RingBuffer:
	"""FIFO ring buffer"""

	def __init__(self, queue, max_buffer_len):
		"""Deque object initialized left-to-right with data from iterable, setting max buffer length"""
		self.queue = deque(queue, maxlen=max_buffer_len)

	def add_value(self, value):
		"""Add single value - removes oldest value off left end if at max capacity"""
		self.queue.append(value)

	def add_values(self, values):
		"""Add multiple values - removes oldest values off left end if at max capacity"""
		self.queue.extend(values)
