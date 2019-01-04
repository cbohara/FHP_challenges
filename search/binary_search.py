def binary_search(iterable, target):
	"""Determine if target value is in sorted iterable containing numbers"""
	while not found:
		middle = len(sequence)//2
		if sequence[middle] > target:
			sequence = sequence[:middle]
		elif sequence[middle] < target:
			sequence = sequence[middle:]
		else:
			found = True
	return found
