def insertion_sort(input_list):
	for index in range(1, len(input_list)):
		current_value = input_list[index]
		position = index
		while position > 0 and input_list[position - 1] > current_value:
			input_list[position] = input_list[position - 1]
			position -= 1
		input_list[position] = current_value
