def binary_search(iterable, target):
	"""Determine if target value is in sorted iterable containing numbers"""
	sorted_iterable = sorted(iterable)
	low = 0
	high = len(sorted_iterable) - 1
	while low <= high:
		midpoint = (high + low) // 2
		if sorted_iterable[midpoint] == target:
			return True
		elif sorted_iterable[midpoint] > target:
			high = midpoint - 1
		elif sorted_iterable[midpoint] < target:
			low = midpoint + 1
	return False
