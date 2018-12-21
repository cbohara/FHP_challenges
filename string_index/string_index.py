def string_diff_index(string1, string2):
	"""
	Determine the index where two strings diverge if they are different
	Return -1 if the strings are the same
	"""
	for index, char in enumerate(zip(string1, string2)):
		if char[0] != char[1]:
			return index

	string_len_diff = len(string1) - len(string2)
	if string_len_diff > 0:
		return len(string2)
	elif string_len_diff < 0:
		return len(string1)
	else:
		return -1

def list_diff_index(list1, list2):
	"""
	Compare lists of strings
	Determine the index where two lists diverge if they are different
	Determine the index where two strings diverge if they are different
	Return a tuple with the two indexes
	The first value represents where the lists diverge
	The second value represents where the strings diverge
	Return (-1, -1) if the two lists contain all the same strings
	"""
	for index, strings in enumerate(zip(list1, list2)):
		string_diff = string_diff_index(strings[0], strings[1])
