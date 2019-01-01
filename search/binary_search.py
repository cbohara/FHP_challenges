def binary_search(sequence, target):
	"""Use binary search to find target value in a sorted sequence"""
	while not found:
		middle = len(sequence)//2
		if sequence[middle] > target:
			sequence = sequence[:middle]
		elif sequence[middle] < target:
			sequence = sequence[middle:]
		else:
			found = True
	return found
