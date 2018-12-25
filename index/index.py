def diff_index(item1, item2):
	"""
	Return the index where two iterables diverge in length, or -1 if they are equal
	"""
	len_diff = len(item1) - len(item2)
	if len_diff > 0:
		return len(item2)
	elif len_diff < 0:
		return len(item1)
	else:
		return -1

def string_diff_index(string1, string2):
	"""
	Determine the index of the character where two strings diverge if they are different
	Return -1 if the strings are the same
	"""
	for index, char in enumerate(zip(string1, string2)):
		if char[0] != char[1]:
			return index
	return diff_index(string1, string2)

def list_diff_index(list1, list2):
	"""
	Compare lists of strings
	Determine the index where two lists diverge if they contain different strings
	Determine the character where the two strings diverge
	Return a tuple with the two indexes
	The first value represents where the lists diverge
	The second value represents where the strings diverge
	Return (-1, -1) if the two lists contain all the same strings
	"""
	for list_index, strings in enumerate(zip(list1, list2)):
		char_index = string_diff_index(strings[0], strings[1])
		if char_index != -1:
			return (list_index, char_index)
	return (diff_index(list1, list2), -1)
