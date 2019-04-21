def con_runs(input_list):
	"""
	Find runs of 3 consecutive numbers that increase of decrease by 1
	:param input_list: list of integers
	:return: list indices of the first element of each run
			if there are no consecutive runs, return None
	"""
	if len(input_list) < 3:
		return None

	con_list = []
	for index in range(2, len(input_list)):
		current_value = input_list[index]
		prev_index = index - 1
		order = 0

		while prev_index >= (index - 2):
			previous_value = input_list[prev_index]
			if order == 0:
				if current_value - previous_value == 1:
					order = 1
				elif current_value - previous_value == -1:
					order = -1
				else:
					break
			else:
				if (current_value - previous_value == 1) and order == 1:
					con_list.append(prev_index)
				elif (current_value - previous_value == -1) and order == -1:
					con_list.append(prev_index)
				else:
					break
			current_value = previous_value
			prev_index -= 1

	if not con_list:
		return None
	else:
		return con_list
