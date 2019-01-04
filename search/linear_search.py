def linear_search(iterable, target):
	"""Determine if target value is in iterable"""
	for current in iterable:
		if current == target:
			return True
	return False
